import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mtvproj.settings')
django.setup()

from first_app.models import User

def populate(n=3):
    fake = Faker()
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        User.objects.create(first_name=first_name, last_name=last_name, email=email)

if __name__ == '__main__':
    print("Populating the database...please wait.")
    populate(20)
    print("Populating complete.")