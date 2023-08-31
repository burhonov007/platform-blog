from django.core.management.base import BaseCommand
from categories.models import Category
import random
from faker import Faker


class Command(BaseCommand):
    help = 'Заполняет базу данных категориями'
    def handle(self, *args, **options):
        fake = Faker()
        category_names = [
            "Технологии", "Наука", "Искусство", "Спорт", "Путешествия",
            "Здоровье", "Еда", "Мода", "Психология", "Финансы",
            "Музыка", "Кино", "Литература", "Игры", "Политика",
            "Образование", "Экология", "Дом и семья", "Религия", "Юмор",
            "Авто", "Дизайн", "Фотография", "Красота", "Дети",
            "Животные", "Садоводство", "Наука о земле", "Маркетинг", "Языки",
            "Ремесла", "Садоводство", "Бизнес", "Путешествия", "Мода",
            "Медицина", "Психология", "Спорт", "История", "Культура",
            "Гастрономия", "Архитектура", "Туризм", "Танцы", "Волонтерство",
            "Экономика", "Право", "Наука о здоровье", "Фотография", "Музыка"
        ]
        
        for name in category_names:
            category = Category.objects.create(
                name=name,
                description=fake.text(), 
            )            
        self.stdout.write(self.style.SUCCESS('Категории успешно созданы'))    