import pika
from faker import Faker
from mongoengine import connect
from models import Contact

connect('your_database_name', host='your_mongodb_connection_string')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='contacts')

fake = Faker()
for _ in range(10):
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number()
    )
    contact.save()

    channel.basic_publish(exchange='',
                          routing_key='contacts',
                          body=str(contact.id))

print("Contacts sent to RabbitMQ")
connection.close()
