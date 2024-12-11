from time import sleep
from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB 🕐 ")

        db_connection = None
        time_count = 0

        while not db_connection:
            try:
                db_connection = connections['default']
            except OperationalError:
                time_count += 1
                self.stdout.write(f"Database unavailable, Retry {time_count}s")
                sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available !'))
