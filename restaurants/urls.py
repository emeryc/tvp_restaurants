from models import Restaurant
from views import add
from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail

urlpatterns = patterns('',
   (r'^$', object_list, {"queryset":Restaurant.objects.all()}),
   (r'^add/$', add),
   (r'^(?P<slug>\S+)/$', object_detail, {"queryset":Restaurant.objects.all()}, 'restaurant_details')
)