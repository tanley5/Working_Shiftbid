from ctypes import util
from django.core.management.base import BaseCommand, CommandError
import schedule
import time
from shiftbid.models import Shiftbid, Seniority, Shift
from utils.shiftbid.background import BackgroundTaskFunction

def scheduled_task():
    print("Scheduled")
    BackgroundTaskFunction()

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