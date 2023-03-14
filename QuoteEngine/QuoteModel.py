class QuoteModel():
    """A class representing a quote with a body and author.

    Attributes:
        body (str): The body of the quote.
        author (str): The author of the quote.

    """
    def __init__(self, body, author):
        """Initialize a QuoteModel object with a body and author.

        Args:
            body (str): The body of the quote.
            author (str): The author of the quote.

        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Return a string representation of the QuoteModel object.

        Returns:
            str: A string representation of the QuoteModel object.
        """
        # return f'<{self.body} , {self.author}>'

        return f'"{self.body}" - {self.author}'