from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


"""
Class Ingestor implements a Strategy pattern to select the appropriate helper for a given file based on filetype.
Then uses the helper to parse the file and return a list of QuoteModel objects
"""

class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the file.

        Raises:
            Exception: If the file cannot be ingested or an error occurs during parsing.
        """
        try:
            for ingestor in cls.ingestors:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
            raise Exception(f"File type not supported: {path}")
        except Exception as e:
            print(f"Error while parsing {path}: {e}")
            return []