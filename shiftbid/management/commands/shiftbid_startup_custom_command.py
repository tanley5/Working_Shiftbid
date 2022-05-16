from django.core.management.base import BaseCommand, CommandError
import schedule
import time
from shiftbid.models import Shiftbid, Seniority, Shift

def scheduled_task():
    print("Started At Startup")
    sb = Shiftbid.objects.all()
    for i in sb:
        print(i)

class Command(BaseCommand):
    help = 'My custom startup command'

    def handle(self, *args, **kwargs):
        try:
            schedule.every(1).minutes.do(scheduled_task)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except:
            raise CommandError('Initalization failed.')