from django.core.management.base import BaseCommand
from posts.models import Post
from comments.models import Comment
from user.models import CustomUser
import random
from faker import Faker


class Command(BaseCommand):
    help = 'Заполняет базу данных категориями'
    def handle(self, *args, **options):
        fake = Faker()
        users = CustomUser.objects.all()
        posts = Post.objects.all()
        for _ in range(100):
            text = fake.text()
            author = random.choice(users)
            post = random.choice(posts)

            Comment.objects.create(
                text=text,
                author=author,
                post=post
            ) 
        self.stdout.write(self.style.SUCCESS('Комментарии успешно созданы'))    