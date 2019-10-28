from django.core.management.base import BaseCommand, CommandError
from shortener.models import RmtURL

class Command(BaseCommand):
    help = 'Refreshes all RmtURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        print(options)
        return RmtURL.objects.refresh_codes(items=options['items'])