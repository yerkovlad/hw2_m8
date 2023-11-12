from mongoengine import connect
from models import Quote, Author

connect('your_database_name', host='your_mongodb_connection_string')

def search_quotes(query):
    if 'name' in query:
        author_name = query['name']
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            return [quote.to_json() for quote in quotes]

    elif 'tag' in query:
        tag = query['tag']
        quotes = Quote.objects(tags=tag)
        return [quote.to_json() for quote in quotes]

    elif 'tags' in query:
        tags = query['tags']
        quotes = Quote.objects(tags__in=tags)
        return [quote.to_json() for quote in quotes]

    return []

if __name__ == "__main__":
    while True:
        user_input = input("Enter command: ")
        command, value = user_input.split(':', 1)

        if command == 'name':
            result = search_quotes({'author.fullname': value.strip()})
            print(result)

        elif command == 'tag':
            result = search_quotes({'tags': value.strip()})
            print(result)

        elif command == 'tags':
            tags = [tag.strip() for tag in value.split(',')]
            result = search_quotes({'tags__in': tags})
            print(result)

        elif command == 'exit':
            break

        else:
            print("Invalid command. Try again.")
