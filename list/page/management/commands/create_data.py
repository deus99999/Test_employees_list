from django_seed import Seed
from django.core.management.base import BaseCommand
from faker import Faker
import random
from ...models import Employee



class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker()


seeder = Seed.seeder()


# create director
def create_ceo():
    seeder.add_entity(Employee, 1, {
        'name': "Timothy Donald Cook",
        'email': lambda x: seeder.faker.email(),
        'position': 'CEO',
        'parent_id': None,
    })
    seeder.execute()


def create_employees():
    seeder.add_entity(Employee, 500, {
        'name': lambda x: seeder.faker.name(),
        'email': lambda x: seeder.faker.email(),
        'position': lambda x: seeder.faker.job(),
        })
    seeder.execute()

#create_ceo()
create_employees()