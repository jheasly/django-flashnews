from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from flashnews.views import last_twelve_hours, last_twelve_hours_roads, test_last_twelve_hours
from flashnews.models import Emergency

amtrak_dict = {
    'queryset': Emergency.objects.filter(participant__org_name='Amtrak'),
    'template_name': 'flashnews/amtrak_emergency_list.html',
}

emergency_dict = {
    'queryset': Emergency.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', last_twelve_hours, dict(template_name='flashnews/emergency_archive.html')),
    (r'^test/$', test_last_twelve_hours, dict(template_name='flashnews/participant_archive.html')),
    (r'^front/$', last_twelve_hours, dict(template_name='flashnews/emergency_archive_front.html')),
    (r'^roads/front/$', last_twelve_hours_roads, dict(template_name='flashnews/emergency_roads_archive_front.html')),
    (r'^roads/$', last_twelve_hours_roads, dict(template_name='flashnews/emergency_roads_archive.html')),
    (r'^service/$', object_list, amtrak_dict),
    (r'^(?P<slug>[-\w]+)/$', 'django.views.generic.list_detail.object_detail', emergency_dict),
)
