from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import DonationGroup
from .serializers import DonationGroupSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def donation_group_list(request):
    donation_groups = DonationGroup.objects.select_related().all()

    paginator = Paginator(donation_groups, 20)
    page = request.GET.get('page')

    if page is not None:
        try:
            donation_groups = paginator.page(page)
        except:
            return HttpResponse(status=204)

    serializer = DonationGroupSerializer(donation_groups, many=True)

    if donation_groups:
        return JSONResponse(serializer.data)
    else:
        return HttpResponse(status=204)
