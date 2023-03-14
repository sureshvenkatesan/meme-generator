from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """A class that implements the IngestorInterface to parse TXT files.

    This class can ingest files with the '.txt' extension.

    Attributes:
        allowed_extensions (List[str]): A list of file extensions that can be ingested by this class.

    """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .txt file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the file.

        Raises:
            Exception: If the file cannot be ingested or an error occurs during parsing.
        """
        # Check if the file can be ingested
        if not cls.can_ingest(path):
            raise Exception('cannot ingest - extension is not txt')

        # Create an empty list to hold the quotes
        quotes = []

        try:

            # Open the file for reading
            with open(path, 'r') as file:
                # Iterate over each line in the file
                for line in file:
                    # Check if the line is not empty
                    if line != "":
                        # Split the line into a list of items using "-"
                        items = line.strip().split('-')

                        # Check if the list has at least two items
                        if len(items) > 1:
                            # Extract the quote body and author
                            body = items[0].strip().replace('"', '')
                            author = items[1].strip()

                            # Create a new QuoteModel object
                            new_quote = QuoteModel(body, author)

                            # Add the new quote to the list
                            quotes.append(new_quote)
        except Exception as e:
            # Handle all other exceptions during file opening and reading
            raise Exception(f"Could not read file: {path}. Error: {e}")

        # Return the list of quotes
        return quotes

