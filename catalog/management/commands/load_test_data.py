from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Удаляет все данные и загружает фикстуры"

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаление всех товаров и категорий...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Загрузка фикстур из initial_data.json...")
        call_command('loaddata', 'catalog/fixtures/initial_data.json')

        self.stdout.write(self.style.SUCCESS(" Данные успешно загружены!"))