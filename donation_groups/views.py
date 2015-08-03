from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FormParser
from .models import DonationGroup
from .serializers import DonationGroupSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def donation_group_list(request, version=""):
    if request.method == 'GET':
        donation_groups = DonationGroup.objects.order_by('-id')

        paginator = Paginator(donation_groups, 10)

        if request.GET.get('page'):
            page = request.GET.get('page')
        else:
            page = 1

        if page is not None:
            try:
                donation_groups = paginator.page(page)
            except:
                return HttpResponse(status=204)

        serializer = DonationGroupSerializer(donation_groups, many=True)

        if donation_groups:
            if version == 'v2':
                return JSONResponse({
                    'meta': {
                        'total_count': paginator.count,
                        'page_count': paginator.num_pages,
                        'current_page': page
                    },
                    'data': serializer.data
                })
            else:
                return JSONResponse(serializer.data)
        else:
            return HttpResponse(status=204)


    elif request.method == 'POST':
        data = FormParser().parse(request)
        serializer = DonationGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
