from django.core.management.base import BaseCommand
from teamapp.models import Role


class Command(BaseCommand):
    help = "Create default Admin and Regular roles"

    def handle(self, *args, **options):
        Role.objects.get_or_create(role='Admin')
        Role.objects.get_or_create(role='Regular')
        self.stdout.write(self.style.SUCCESS('Successfully created roles'))
        return
