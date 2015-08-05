from django.core.management.base import BaseCommand, CommandError
from newsfeed.converter import is_zawgyi, uni512zg1, zg12uni51
from newsfeed.models import Newsfeed


class Command(BaseCommand):
    help = 'Prune existing zg content in db into unicode'

    def handle(self, *args, **options):
        pass
