import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',"Project_two.settings")

import django
django.setup()

import random
from AppTwo.models import User_data
from faker import Faker

fake = Faker()

def populate(N=5):

    for entry in range(N):
                
        fake_firstName = fake.first_name()
        fake_lastName=fake.last_name()
        fake_email = fake.ascii_email()

        userData = User_data.objects.get_or_create(first_name=fake_firstName, last_name=fake_lastName, e_mail = fake_email)[0]

        

if __name__ == '__main__':
    print("populating user!")
    populate(10)
    print("populating complete!")    



    