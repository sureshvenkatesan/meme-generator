from typing import List
import subprocess
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """A class that implements the IngestorInterface to parse PDF files.

    This class can ingest files with the '.pdf' extension.

    Attributes:
        allowed_extensions (List[str]): A list of file extensions that can be ingested by this class.

    """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .pdf file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the file.

        Raises:
            Exception: If the file cannot be ingested or an error occurs during parsing.
        """
        # Check if the file can be ingested
        if not cls.can_ingest(path):
            raise Exception('cannot ingest - extension is not pdf')

        # Create an empty list to hold the quotes
        quotes = []

        try:

            """
            Use the subprocess.check_output() function to run the pdftotext command with the -layout option
            to preserve the original layout of the PDF file, and the - option to output the result to stdout. 
            The resulting output is captured in the output variable as bytes.
            """
            output = subprocess.check_output(['pdftotext', '-layout', path, '-'])

            # Decode the output bytes to a string
            text = output.decode('utf-8')

            # Split the text into lines and convert each line to a list of items
            lines = [line.strip().split('-') for line in text.split('\n')]

            # Iterate over each line in the lines list
            for line in lines:
                # Check if the line has at least two items
                if len(line) > 1:
                    # Extract the quote body and author from the line
                    body = line[0].strip().replace('"', '')
                    author = line[1].strip()

                    # Create a new QuoteModel object using the extracted body and author
                    new_quote = QuoteModel(body, author)

                    # Add the new quote to the list of quotes
                    quotes.append(new_quote)
        except Exception as e:
            # Handle all other exceptions during file opening and reading
            raise Exception(f"Could not read file: {path}. Error: {e}")

        # Return the list of quotes
        return quotes
