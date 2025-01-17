from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.core.management import BaseCommand
from apps.core.tasks import expire_at_advertise


class Command(BaseCommand):
    help = 'Setup periodic tasks'

    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB 🕐 ")
        expire_at_advertise.delay()
        schedule, created = CrontabSchedule.objects.get_or_create(
            minute="*/3",
            hour="*",
            day_of_week="*",
            day_of_month="*",
            month_of_year="*"
        )

        PeriodicTask.objects.update_or_create(task='apps.core.tasks.expire_at_advertise',crontab=schedule,args='[]',kwargs={})
        print('hamidreza')