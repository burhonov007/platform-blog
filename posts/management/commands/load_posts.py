from django.core.management.base import BaseCommand
from faker import Faker
import random
from user.models import CustomUser
from posts.models import Post
from categories.models import Category

users = CustomUser.objects.all()
categories = Category.objects.all()

fake = Faker()

class Command(BaseCommand):
    help = 'Заполняет базу данных случайными данными для блога'

    def handle(self, *args, **options):
        for _ in range(100):
            title = fake.sentence()
            content = fake.paragraphs(10)
            creator = random.choice(users)
            publish_date = fake.past_datetime(start_date='-30d', tzinfo=None)
            category = random.choice(categories)
            views = random.randint(0, 1000)
            image = fake.image_url()
            video = fake.image_url()
            gif = fake.image_url()

            post = Post.objects.create(
                title=title,
                content=content,
                creator=creator,
                publish_date=publish_date,
                category=category,
                views=views,
                image=image,
                video=video,
                gif=gif
            )

        self.stdout.write(self.style.SUCCESS('Посты успешно созданы'))
