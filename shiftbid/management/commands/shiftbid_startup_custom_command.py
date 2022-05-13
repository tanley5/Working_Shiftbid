from django.core.management.base import BaseCommand, CommandError
import schedule

from shiftbid.models import Shiftbid, Seniority, Shift

class Command(BaseCommand):
    help = 'My custom startup command'

    def handle(self, *args, **kwargs):
        try:
            print("Started At Startup")
            sb = Shiftbid.objects.all()
            for i in sb:
                print(i)
        except:
            raise CommandError('Initalization failed.')