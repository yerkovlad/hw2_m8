# load_data.py
from mongoengine import connect
from models import Author, Quote
import json

# Підключення до MongoDB
connect('your_database_name', host='your_mongodb_connection_string')

# Завантаження даних з authors.json
with open('authors.json', 'r') as file:
    authors_data = json.load(file)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()

# Завантаження даних з quotes.json
with open('quotes.json', 'r') as file:
    quotes_data = json.load(file)

for quote_data in quotes_data:
    author_name = quote_data.pop('author')
    author = Author.objects(fullname=author_name).first()
    quote_data['author'] = author
    quote = Quote(**quote_data)
    quote.save()
