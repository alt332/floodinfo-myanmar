from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FormParser
from .models import Newsfeed
from .serializers import NewsfeedSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def newsfeed_list(request, version):
    if request.method == 'GET':
        newsfeeds = Newsfeed.objects.values('id', 'title', 'description', 'posted_time').exclude(show_hide=True).order_by('-id').all()

        paginator = Paginator(newsfeeds, 10)
        page = request.GET.get('page')

        if page is not None:
            try:
                newsfeeds = paginator.page(page)
            except:
                return HttpResponse(status=204)

        serializer = NewsfeedSerializer(newsfeeds, many=True)

        if newsfeeds:
            if version == 'v2':
                return JSONResponse({
                    'meta': {
                        'total_count': paginator.count,
                        'page_count': paginator.num_pages,
                        'current_page': page if page else 1,
                    },
                    'data': serializer.data
                })
            else:
                return JSONResponse(serializer.data)
        else:
            return HttpResponse(status=204)
    elif request.method == 'POST':
        data = FormParser().parse(request)
        serializer = NewsfeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


def newsfeed_report(request, pk):
    try:
        newsfeed = Newsfeed.objects.get(pk=pk)
    except:
        return HttpRespose(stauts=404)

    newsfeed.spam_report_count += 1
    newsfeed.save()

    return JSONResponse({ 'message': 'Successfully Reported.' },status=200)
