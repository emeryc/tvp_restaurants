from models import Restaurant
from views import add, not_available, bad_info, tag, rate, restaurant
from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from tagging.views import tagged_object_list

urlpatterns = patterns('',
   (r'^$', object_list, {"queryset":Restaurant.objects.all().order_by("name")}),
   (r'^add/$', add),
   (r'^tags/(?P<tag>.+)/$', tagged_object_list, {'queryset_or_model':Restaurant}),
   (r'^\S+/(?P<item_id>\d+)/not_available/$', not_available),
   (r'^\S+/(?P<item_id>\d+)/wrong/$', bad_info),
   (r'^(?P<slug>\S+)/tag/$', tag),
   (r'^(?P<slug>\S+)/rating/$', rate),
   (r'^(?P<slug>\S+)/$', restaurant, {},'restaurant_details'),
   
   
   
)