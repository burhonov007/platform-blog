from django.core.management.base import BaseCommand
from user.models import CustomUser
from faker import Faker


class Command(BaseCommand):
    help = 'Запольняет базу данных пользователями'
    
    def handle(self, *args, **options):
        
        fake = Faker()
        
        for _ in range(20):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            password = "qwerty1234"
            CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            
        CustomUser.objects.create_user(first_name="Jack", last_name="Adams", email="jackadams@example.com", password="qwerty1234")
        CustomUser.objects.create_superuser(email="admin@example.com", password="admin", first_name="Andrew", last_name="Martinez")
        
        self.stdout.write(self.style.SUCCESS('Пользователи успешно созданы'))
    