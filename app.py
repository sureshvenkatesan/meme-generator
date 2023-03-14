import random
import requests
from flask import Flask, render_template, abort, request

# @TODO Completed: Import your Ingestor and MemeEngine classes
# add the following code to your Flask app to add the current directory to the Python path:
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Completed -> Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote in quote_files:
        quotes.extend(Ingestor.parse(quote))


    images_path = "_data/photos/dog/"

    # TODO: Completed -> Use the pythons standard library os class to find all
    # images within the images images_path directory
    # Get a list of all files and directories within the images_path directory
    files = os.listdir(images_path)

    # Filter the list to include only files with image file extensions
    imgs = [os.path.join(images_path, file) for file in files if os.path.splitext(file)[1].lower() == '.jpg']

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO: Completed
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO: Completed
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    image_url = request.form['image_url']
    r = requests.get(image_url, verify=False)

    img_path = f'./tmp/{random.randint(0, 100000000)}.png'
    with open(img_path, 'wb') as img:
        img.write(r.content)

    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(img_path, body, author)

    # 3. Remove the temporary saved image.
    os.remove(img_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
