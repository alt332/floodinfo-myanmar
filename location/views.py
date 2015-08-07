from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Location


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def state_list(request):
    data = Location.objects.order_by('state').values('state').distinct('state').all()

    if data:
        states = []
        [states.append(v['state']) for v in data]
        return JSONResponse(states)
    else:
        return HttpResponse(status=204)

@csrf_exempt
def township_list_of_state(request, state):
    data = Location.objects.filter(state__icontains=state).order_by('township').values(
        'district',
        'township',
        'latitude',
        'longitude',
        'status',
        'state',
        'description',
        'total_male',
        'total_female',
        'urban_total_male',
        'urban_total_female',
        'rural_total_male',
        'rural_total_female',
    ).all()

    if data:
        return JSONResponse(data)
    else:
        return HttpResponse(status=204)
