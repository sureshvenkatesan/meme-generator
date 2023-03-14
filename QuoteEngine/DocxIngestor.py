from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """A class that implements the IngestorInterface to parse .docx files.

    This class can ingest files with the '.docx' extension.

    Attributes:
        allowed_extensions (List[str]): A list of file extensions that can be ingested by this class.

    """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .docx file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the file.

        Raises:
            Exception: If the file cannot be ingested or an error occurs during parsing.
        """
        # Check if the file can be ingested
        if not cls.can_ingest(path):
            raise Exception('cannot ingest - extension is not docx')

        # Create an empty list to hold the quotes
        quotes = []

        try:
            # Open the docx file using the python-docx library
            doc = docx.Document(path)

            # Iterate over each paragraph in the document
            for para in doc.paragraphs:
                # Check if the paragraph is not empty
                if para.text != "":
                    # Split the paragraph into a list of items using "-" as the separator
                    items = para.text.strip().split('-')

                    # Check if the list has at least two items
                    if len(items) > 1:
                        # Extract the quote body and author from the list of items
                        body = items[0].strip().replace('"', '')
                        author = items[1].strip()

                        # Create a new QuoteModel object using the extracted body and author
                        new_quote = QuoteModel(body, author)

                        # Add the new quote to the list of quotes
                        quotes.append(new_quote)
        except Exception as e:
            # Handle all other exceptions during file opening and reading
            raise Exception(f"Could not read file: {path}. Error: {e}")

        # Return the list of quotes
        return quotes
