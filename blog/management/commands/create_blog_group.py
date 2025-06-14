from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from blog.models import BlogPost
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Создаёт группу Контент-менеджер с нужными правами'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Контент-менеджер')

        content_type = ContentType.objects.get_for_model(BlogPost)
        permission = Permission.objects.get(
            codename='can_manage_blog',
            content_type=content_type
        )

        group.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('Группа "Контент-менеджер" создана и права назначены.'))
