from mongoengine import connect
from models import Author, Quote
import json

connect('test', host='mongodb+srv://yerkovlad:02012009@atlascluster.qwykxm4.mongodb.net/')

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
