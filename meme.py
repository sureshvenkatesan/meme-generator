import os
import random


# @TODO Completed: Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
import argparse
import sys
from typing import Optional


def generate_meme(path: Optional[str] = None, body: Optional[str] = None, author: Optional[str] = None) -> str:
    """Generate a meme given a path to an image and a quote.

    Args:
        path (str, optional): The path to the image file. If None, a random image will be selected.
        body (str, optional): The body of the quote. If None, a random quote will be selected from a set of pre-defined quote files.
        author (str, optional): The author of the quote. Required if body is used.

    Returns:
        str: The file path of the generated meme.

    Raises:
        Exception: If the author is not provided when body is used.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        # img = path[0]
        img = path

    if body is None:
        # quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
        #                './_data/DogQuotes/DogQuotesDOCX.docx',
        #                './_data/DogQuotes/DogQuotesPDF.pdf',
        #                './_data/DogQuotes/DogQuotesCSV.csv']
        quote_files = ['./_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Completed: Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    # make the path parameter optional and require the author parameter only if the body parameter is specified
    parser = argparse.ArgumentParser(description='Generate a meme by adding a quote and author to an image.')

    parser.add_argument('--path', type=str, help='path to the image file', required=False)
    parser.add_argument('--body', type=str, help='quote body to add to the image', required=False)
    parser.add_argument('--author', type=str, help='quote author to add to the image', required=False)

    # Check if body is specified, and if so, require author
    if 'body' in sys.argv and 'author' not in sys.argv:
        parser.error('--author is required when --body is specified')

    args = parser.parse_args()

# example usage:
# python meme.py --body "This is a quote" --author "Author Name"
# python meme.py --path "/Users/sureshv/PycharmProjects/pythonProject/cropimage/src/_data/photos/dog/xander_4.jpg"
# python meme.py --path "/Users/sureshv/PycharmProjects/pythonProject/cropimage/src/_data/photos/dog/xander_4.jpg" --body "to be or not to be" --author "shakes"
    print(generate_meme(args.path, args.body, args.author))
