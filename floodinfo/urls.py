"""floodinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from donation_groups import views as donation_group_views
from newsfeed import views as newsfeed_views
from location import views as location_views
from django.contrib import admin


urlpatterns = [
    url(r'^api/donation_groups$', donation_group_views.donation_group_list),
    url(r'^api/(?P<version>\w+)/donation_groups$', donation_group_views.donation_group_list),
    url(r'^api/newsfeeds$', newsfeed_views.newsfeed_list),
    url(r'^api/(?P<version>\w+)/newsfeeds$', newsfeed_views.newsfeed_list),
    url(r'^api/newsfeeds/(?P<pk>[0-9]+)/report_as_spam$', newsfeed_views.newsfeed_report),
    url(r'^api/v2/newsfeeds/(?P<pk>[0-9]+)/report_as_spam$', newsfeed_views.newsfeed_report),
    url(r'^api/v2/states$', location_views.state_list),
    url(r'^api/v2/states/(?P<state>\w+)/townships$', location_views.township_list_of_state),
    url(r'^admin/', include(admin.site.urls)),
]
