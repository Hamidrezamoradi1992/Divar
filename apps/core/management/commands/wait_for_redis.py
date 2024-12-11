import redis
from time import sleep
from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for Redis 🕐 ")
        time_count = 0

        if not settings.DEBUG:
            redis_connection = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
            redis_state = False

            while not redis_state:
                try:
                    redis_connection.client_list()
                except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
                    time_count += 1
                    self.stdout.write(f"Redis service unavailable, waiting: (Retry: {time_count}s)")
                    sleep(1)
                    continue

                redis_state = True
            self.stdout.write(self.style.SUCCESS('Redis available '))
        else:
            self.stdout.write("Redis check passed !")