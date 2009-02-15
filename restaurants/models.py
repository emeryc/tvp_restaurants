from django.db import models
from django.contrib.localflavor.us.models import *
from django.contrib.auth.models import User
from datetime import datetime
import callbacks
from tagging.fields import TagField

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    address1 = models.CharField("Address Line 1", max_length=50)
    address2 = models.CharField("Address Line 2", max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state = USStateField(default="OR")
    zipcode = models.CharField(blank=True, max_length=10)
    phone = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    user = models.ForeignKey(User)
    last_mod = models.DateTimeField(auto_now=True)
    
    def get_rating(self):
        scores = [x.score for x in self.rating_set.all()]
        if len(scores) == 0:
            return 0
        return sum(scores)/(len(scores)*1.0)
    
    def get_int_rating(self):
        return int(self.get_rating() + .5)
    
    def get_num_raters(self):
        return len(self.rating_set.all())
    
    def updated(self):
        menu_item = max(Restaurant.objects.all()[0].menuitem_set.all(), key=lambda x: x.last_mod)
        last_updated = max(menu_item, self, key=lambda x: x.last_mod)
        return last_updated.last_mod
    
    @models.permalink
    def get_absolute_url(self):
        return ('restaurant_details', (), {'slug': self.slug })
    
    def __unicode__(self):
        return self.name

    def hours(self):
        all_hours = self.hours_set.all()
        days = {}
        for hour in all_hours:
            hour_list = days.get(hour.day, Day(hour.day))
            hour_list.add_hour(hour)
            days[hour.day] = hour_list
        ordered_days = []
        for day_name in DAY_CHOICES:
            for day in days.values():
                if day.day == day_name[1]:
                    ordered_days.append(day)
        return ordered_days
    

DAY_CHOICES = (
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thu", "Thursday"),
    ("fri", "Friday"),
    ("sat", "Saturday"),
    ("sun", "Sunday"),
)


class Day(object):
    def __init__(self, day):
        self.day = dict(DAY_CHOICES)[day]
        self.hours = []
    
    def add_hour(self, hour):
        self.hours.append(hour)
        self.hours.sort()


class Hours(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    open_time = models.TimeField()
    close_time = models.TimeField()
    
    def __unicode__(self):
        return self.day + " " + str(self.open_time) + " - " + str(self.close_time)

class MenuItem(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User)
    is_available = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant)
    bad_info = models.BooleanField(default=False)    
    last_mod = models.DateTimeField(default=datetime.now(), auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    

class Rating(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    score = models.IntegerField()
