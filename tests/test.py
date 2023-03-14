import sys
import os
# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)+ '/..'))

from QuoteEngine import Ingestor



print(Ingestor.parse('../_data/SimpleLines/SimpleLines.csv'))
print(Ingestor.parse('../_data/SimpleLines/SimpleLines.docx'))
print(Ingestor.parse('../_data/SimpleLines/SimpleLines.pdf'))
print(Ingestor.parse('../_data/SimpleLines/SimpleLines.txt'))

print(Ingestor.parse('../_data/DogQuotes/DogQuotesCSV.csv'))
print(Ingestor.parse('../_data/DogQuotes/DogQuotesDOCX.docx'))
print(Ingestor.parse('../_data/DogQuotes/DogQuotesPDF.pdf'))
print(Ingestor.parse('../_data/DogQuotes/DogQuotesTXT.txt'))