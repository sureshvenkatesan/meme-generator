Overview

# Meme Generator

The Meme Generator is a Python application that allows users to generate memes .

The application takes an image, a quote body, and an author name as inputs, and generates a new image 
with the quote overlaid on top.



## Dependencies

The Meme Generator requires the following dependencies:

- Python 3.6 or later
- Flask
- Pillow
- pandas

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

The application has a simple user interface that allows you to upload an image and enter a quote body and author name.
Once you submit the form, the application will generate a new image with the quote overlaid on top, 
and display it on the page.

or

b)
```commandline
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
```
This will start the Flask application on `http://localhost:3000`. You can then access the application 
in your web browser by navigating to that URL.
