# Create your views here.

from datetime import datetime, timedelta
from flashnews.models import Category, Participant, Emergency
from django.db.models import Q, Max
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404

HOURS_BACK = 1

def half_day_ago():
    half_day_ago_diff = timedelta(hours = HOURS_BACK)
    half_day_ago = datetime.today() - half_day_ago_diff
    return half_day_ago

def last_twelve_hours(request, template_name):
    return list_detail.object_list(
        request,
        queryset = Emergency.objects.filter(effective_date__gt=half_day_ago()).filter(participant__category__name__in=[
            "Courts",
            "Benton Co. Schools",
            "Colleges & Universities",
            "Coos Co. Schools",
            "Douglas Co. Schools",
            "Lane Co. Schools",
            "Linn Co. Schools",
            "No. Ore. Coast Schools",
            "Organizations",
            "Parks and Recreation",
            "Private & Charter Schools",
            "Public Colleges & Universities",
            "State",
        ]).exclude(participant__org_name__in=[
            "Albany Christian School",
            "Greater Albany",
            "Lebanon",
            "Mission Mill Museum",
            "OMSI",
            "Ore. DMV",
            "Oregon Dept. of Forestry",
            "Salem Police Dept.",
            "Scio",
            "Southern Ore. Schools",
            "St. Mary's School Albany",
            "UCAN Head Start",
            "Umpqua Valley Chrisitian Schools",
        ]),
        template_name = template_name,
    )

# 
# the_latest = Participant.objects.annotate(latest_post=Max('emergency__effective_date')).filter(latest_post__gt='2010-11-10 00:00').order_by('org_name')
# 
# for org in the_latest:
#     print org.org_name, org.emergency_set.latest('effective_date').effective_date
# 

def test_last_twelve_hours(request, template_name):
    queryset = Participant.objects.annotate(latest_post=Max('emergency__effective_date')).filter(latest_post__gt=half_day_ago()),
#     filtered_queryset = [item.emergency_set.filter(effective_date=item.latest_post) for item in queryset]
    
    queryset = queryset[0][0].emergency_set.filter(effective_date=queryset[0][0].latest_post)
    
    return list_detail.object_list(
        request,
        # queryset = Participant.objects.annotate(latest_post=Max('emergency__effective_date')).filter(latest_post__gt=half_day_ago()),
        queryset = queryset,
        template_name = template_name,
    )

def last_twelve_hours_roads(request, template_name):
    return list_detail.object_list(
        request,
        queryset = Emergency.objects.filter(effective_date__gt=half_day_ago()).filter(Q(participant__category__name='Transportation') | Q(participant__category__name='Police & Fire')).exclude(participant__org_name__in=[
            "Lebanon Fire Dist.",
            "ODOT",
#             "ODOT Region 1",
            "ODOT Region 4",
            "ODOT Region 5",
            "ODOT/Eastern Oregon",
            "ODOT/East. Ore.",
            "Salem Fire Dept.",
            "Salem Police Dept.",
            ]),
        template_name = template_name,
    )
