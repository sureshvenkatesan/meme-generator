import subprocess
import random

import docx
import csv


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)+ '/..'))
from QuoteEngine import QuoteModel


def process_pdf(path):
    # Run pdftotext command via subprocess call
    output = subprocess.check_output(['pdftotext', '-layout', path, '-'])

    # Decode the output bytes to a string
    text = output.decode('utf-8')

    # Split the text into lines and convert each line to a list of items
    lines = [line.strip().split('-') for line in text.split('\n')]
    # print(lines)

    for line in lines:
        if len(line) > 1:
            # print(line)
            body = line[0].strip().replace('"','')
            author = line[1].strip()
            print(f'{body} and {author}')


def process_csv(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # print(f'{row["body"]} and {row["author"]}')
            quote = QuoteModel(row["body"],row["author"])
            print(quote)

def process_docx(path):
    doc = docx.Document(path)

    for para in doc.paragraphs:
        if para.text != "":
            # Split the para text to a list of items
            items = para.text.strip().split('-')
            if len(items) > 1:
                body = items[0].strip().replace('"', '')
                author = items[1].strip()
                print(f'{body} and {author}')

def process_txt(path):
    with open(path, 'r') as file:
        for line in file:
            if line != "":
                # Split the para text to a list of items
                items = line.strip().split('-')
                if len(items) > 1:
                    body = items[0].strip().replace('"', '')
                    author = items[1].strip()
                    print(f'{body} and {author}')


if __name__ == "__main__":
    process_pdf('../_data/SimpleLines/SimpleLines.pdf')
    process_txt('../_data/SimpleLines/SimpleLines.txt')
    process_docx('../_data/SimpleLines/SimpleLines.docx')
    process_csv('../_data/SimpleLines/SimpleLines.csv')
