from django.core.management.base import BaseCommand

class commands_welcome_all_user(BaseCommand):
    help = 'Welcome all  email users'
    def handle(self, *args, **options):
        email