Overview

# Meme Generator

The Meme Generator is a Python application that allows users to generate memes .

The application takes an image, a quote body, and an author name as inputs, and generates a new image 
with the quote overlaid on top.



## Dependencies

The Meme Generator requires the following dependencies:

- Python 3.6 or later

- pandas
- python-docx
- Flask
- Pillow
- requests

You can install these dependencies using pip:
```commandline
pip install pandas  python-docx Flask Pillow requests
```


## Installation

To install the Meme Generator, clone the repository to your local machine:

git clone https://github.com/sureshvenkatesan/meme-generator.git


Then, navigate to the repository directory and install the dependencies:

```commandline
cd meme-generator
pip install -r requirements.txt
```


## Usage

To use the Meme Generator, run the `app.py` script as:
a)
```commandline
python app.py


```

This will start the Flask application on `http://localhost:5000`. You can then access the application 
in your web browser by navigating to that URL.


By default the application will render a random meme image with a quote ( along with the author) overlayed on top.
You will see 2 options "Random" and "Creator".

If you click on "Random" it will generate a new random meme.
If you click on "Creator"  you can  specify an image url and enter a quote body and author name.
Once you submit the form, the application will generate a new meme image ( for the specified image) 
with the quote overlaid on top and display it on the page.

or

b)
```commandline
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
```
This will start the Flask application on `http://localhost:3000`. You can then access the application 
in your web browser by navigating to that URL.

This application uses the following packages : 
# QuoteEngine
This has python modules to ingest files in  different file formats like csv, docx, pdf , txt .
These files containing quote(s) and their authors . The QuoteEngine implements a Strategy pattern to ingest
any of these file types and  return a list of QuoteModel objects.
QuoteModel  represent a quote with a body and author.

Common file exceptions are handled and  human-readable error messages are displayed.

The **"tests"** folders has some python programs that test the **QuoteModel** and **Ingestor** .
To become familiar with how to do relative import of Modules from another package ( and modify the Python Search path)
please refer to :
https://stackoverflow.com/questions/71215741/how-to-resolve-relative-import
https://itsmycode.com/importerror-attempted-relative-import-with-no-known-parent-package/

# MemeGenerator
This module creates a meme with specified dimensions by adding text and author to an image .


It can be tested using the **meme.py** a python program that can  run from commandline takes three OPTIONAL arguments:

A string quote body
A string quote author
An image path

Common file exceptions are handled and  human-readable error messages are displayed.

## example usage:
```commandline
python meme.py --body "This is a quote" --author "Author Name"
python meme.py --path "/meme-generator/_data/photos/dog/xander_4.jpg"
python meme.py --path "/meme-generator/_data/photos/dog/xander_4.jpg" --body "to be or not to be" --author "shakespeare"
```
After the meme is created it returns the path to the meme image.
