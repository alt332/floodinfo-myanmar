import urllib, json

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from location.models import Location


class Command(BaseCommand):
    locations = json.load( urllib.urlopen('http://doe:eff04a96bd@kunyi.asia/api/locations.json') )

    data_to_save = []

    for l in locations:
        if not l['demographic']:
            l['demographic'] = {}
            l['demographic']['district'] = ''
            l['demographic']['total_male'] = 0
            l['demographic']['total_female'] = 0
            l['demographic']['urban_total_male'] = 0
            l['demographic']['urban_total_female'] = 0
            l['demographic']['rural_total_male'] = 0
            l['demographic']['rural_total_female'] = 0

        data_to_save.append(
            Location(
                township=l['township'],
                state=l['state'],
                status=l['status'],
                description=l['description'],
                latitude=l['lat'],
                longitude=l['lon'],
                district=l['demographic']['district'],
                total_male=l['demographic']['total_male'],
                total_female=l['demographic']['total_female'],
                urban_total_male=l['demographic']['urban_total_male'],
                urban_total_female=l['demographic']['urban_total_female'],
                rural_total_male=l['demographic']['rural_total_male'],
                rural_total_female=l['demographic']['rural_total_female'],
            )
        )
    
    Location.objects.bulk_create(data_to_save)
    print "Saved!"

    def handle(self, *args, **options):
        translation.deactivate()
