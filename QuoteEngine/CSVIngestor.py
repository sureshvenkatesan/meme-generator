from typing import List
import csv
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd

class CSVIngestor(IngestorInterface):
    """A class that implements the IngestorInterface to parse CSV files.

    This class can ingest files with the '.csv' extension.

    Attributes:
        allowed_extensions (List[str]): A list of file extensions that can be ingested by this class.

    """
    allowed_extensions = ['csv']

    @classmethod
    def parse1(cls, path: str) -> List[QuoteModel]:
        """Parse a .csv file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the file.

        Raises:
            Exception: If the file cannot be ingested or an error occurs during parsing.
        """
        # Check if the file can be ingested
        if not cls.can_ingest(path):
            raise Exception('cannot ingest - extension is not csv')

        # Create an empty list to hold the quotes
        quotes = []

        try:
            # Open the file for reading
            with open(path, 'r') as file:
                # Use csv.DictReader to read the file
                reader = csv.DictReader(file)

                # Iterate over each row in the CSV file
                for row in reader:
                    # Create a new QuoteModel object using the "body" and "author" fields
                    new_quote = QuoteModel(row['body'], row['author'])

                    # Add the new quote to the list
                    quotes.append(new_quote)

        except Exception as e:
            # Handle all other exceptions during file opening and reading
            raise Exception(f"Could not read file: {path}. Error: {e}")

        # Return the list of quotes
        return quotes

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .csv file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the file.

        Raises:
            Exception: If the file cannot be ingested or an error occurs during parsing.
        """
        # Check if the file can be ingested
        if not cls.can_ingest(path):
            raise Exception('cannot ingest - extension is not csv')

        quotes = []
        try:
            # Read the CSV file using pandas
            df = pd.read_csv(path)

            # Loop through the rows of the DataFrame and create a QuoteModel object for each row
            for index, row in df.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)

        except Exception as e:
            # Handle all other exceptions during file opening and reading
            raise Exception(f"Could not read file: {path}. Error: {e}")

        # Return the list of quotes
        return quotes