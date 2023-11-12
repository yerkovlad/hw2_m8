from mongoengine import connect
from models import Author, Quote
import json

connect('your_database_name', host='your_mongodb_connection_string')

with open('authors.json', 'r') as file:
    authors_data = json.load(file)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()

with open('quotes.json', 'r') as file:
    quotes_data = json.load(file)

for quote_data in quotes_data:
    author_name = quote_data.pop('author')
    author = Author.objects(fullname=author_name).first()
    quote_data['author'] = author
    quote = Quote(**quote_data)
    quote.save()
