from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
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
def newsfeed_list(request, version=""):
    if request.method == 'GET':
        newsfeeds = Newsfeed.objects.values('id', 'title', 'description', 'posted_time').exclude(show_hide=True).order_by('-id')

        paginator = Paginator(newsfeeds, 10)
        if request.GET.get('page'):
            page = request.GET.get('page')
        else:
            page = 1

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
                        'current_page': int(page)
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


@csrf_exempt
def newsfeed_report(request, pk):
    try:
        newsfeed = Newsfeed.objects.get(pk=pk)
    except:
        return HttpRespose(stauts=404)

    newsfeed.spam_report_count += 1
    newsfeed.save()

    return JSONResponse({ 'message': 'Successfully Reported.' },status=200)


@csrf_exempt
def filter_by_township(request, township):
    newsfeeds = Newsfeed.objects.filter(township__icontains=township).exclude(show_hide=True).order_by('-id')

    paginator = Paginator(newsfeeds, 10)
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1

    if page is not None:
        try:
            newsfeeds = paginator.page(page)
        except:
            return HttpResponse(status=204)

    serializer = NewsfeedSerializer(newsfeeds, many=True)

    if newsfeeds:
        return JSONResponse({
            'meta': {
                'total_count': paginator.count,
                'page_count': paginator.num_pages,
                'current_page': int(page)
            },
            'data': serializer.data
        })
    else:
        return HttpResponse(status=204)

@csrf_exempt
def filter_by_state(request, state):
    newsfeeds = Newsfeed.objects.filter(state__icontains=state).exclude(show_hide=True).order_by('-id')

    paginator = Paginator(newsfeeds, 10)
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1

    if page is not None:
        try:
            newsfeeds = paginator.page(page)
        except:
            return HttpResponse(status=204)

    serializer = NewsfeedSerializer(newsfeeds, many=True)

    if newsfeeds:
        return JSONResponse({
            'meta': {
                'total_count': paginator.count,
                'page_count': paginator.num_pages,
                'current_page': int(page)
            },
            'data': serializer.data
        })
    else:
        return HttpResponse(status=204)

@csrf_exempt
def search(request, query):
    newsfeeds = Newsfeed.objects.filter(Q(state__icontains=query) | Q(township__icontains=query) | Q(title__contains=query) | Q(description__icontains=query)).exclude(show_hide=True).order_by('-id')

    paginator = Paginator(newsfeeds, 10)
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1

    if page is not None:
        try:
            newsfeeds = paginator.page(page)
        except:
            return HttpResponse(status=204)

    serializer = NewsfeedSerializer(newsfeeds, many=True)

    if newsfeeds:
        return JSONResponse({
            'meta': {
                'total_count': paginator.count,
                'page_count': paginator.num_pages,
                'current_page': int(page)
            },
            'data': serializer.data
        })
    else:
        return HttpResponse(status=204)
