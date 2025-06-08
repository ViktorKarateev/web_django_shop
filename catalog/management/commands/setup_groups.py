from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" и назначает права'

    def handle(self, *args, **kwargs):
        group_name = 'Модератор продуктов'
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            self.stdout.write(f'Группа "{group_name}" создана')
        else:
            self.stdout.write(f'Группа "{group_name}" уже существует')

        content_type = ContentType.objects.get_for_model(Product)

        permissions = [
            Permission.objects.get(codename='can_unpublish_product', content_type=content_type),
            Permission.objects.get(codename='delete_product', content_type=content_type),
        ]

        for perm in permissions:
            group.permissions.add(perm)
            self.stdout.write(f'Добавлено разрешение: {perm.codename}')

        self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" готова к использованию'))
