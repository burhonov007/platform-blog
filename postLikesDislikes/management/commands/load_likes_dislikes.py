from django.core.management.base import BaseCommand
from faker import Faker
import random
from postLikesDislikes.models import PostLikesDislikes
from posts.models import Post
from user.models import CustomUser


fake = Faker()

class Command(BaseCommand):
    help = 'Заполняет базу данных случайными данными для лайков и дизлайков'

    def handle(self, *args, **options):
        num_likes_dislikes = 200 
        users = CustomUser.objects.all()  
        posts = Post.objects.all()  

        for _ in range(num_likes_dislikes):
            user = random.choice(users)
            post = random.choice(posts)
            type = random.choice(['like', 'dislike'])
            date = fake.past_datetime(start_date='-30d', tzinfo=None)

            PostLikesDislikes.objects.create(
                user=user,
                post=post,
                type=type,
                date=date
            )

        self.stdout.write(self.style.SUCCESS('Лайки и дизлайки успешно созданы'))
