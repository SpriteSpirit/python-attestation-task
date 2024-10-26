from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Создание администратора с полными правами доступа'

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@localhost',
            first_name='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password('admin')
        user.save()
        print("Администратор admin@localhost создан")
