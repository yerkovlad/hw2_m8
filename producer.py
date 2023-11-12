import pika
from faker import Faker
from mongoengine import connect
from models import Contact

connect('test', host='mongodb+srv://yerkovlad:02012009@atlascluster.qwykxm4.mongodb.net/')

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
