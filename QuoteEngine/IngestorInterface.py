from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """An abstract base class for file ingestor classes.

    Subclasses of this class must implement the `parse` method.

    Attributes:
        allowed_extensions (List[str]): A list of file extensions that can be ingested by subclasses.

    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if a file can be ingested by this class ( based only on the file extension).

            Args:
                path (str): The file path to check.

            Returns:
                bool: True if the file can be ingested by this class, False otherwise.
            """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from the file.

        Raises:
            Exception: If the file cannot be ingested or an error occurs during parsing.
        """
        pass
