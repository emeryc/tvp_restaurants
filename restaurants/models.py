from django.db import models
from django.contrib.localflavor.us.models import *
from django.contrib.auth.models import User
from django.utils import simplejson
from datetime import datetime
import callbacks
from tagging.fields import TagField
import urllib
from django.contrib.comments.models import Comment
from tagging.models import Tag

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    address1 = models.CharField("Address Line 1", max_length=50)
    address2 = models.CharField("Address Line 2", max_length=50, blank=True)
    city = models.CharField(max_length=60)
    # state = USStateField(default="OR")
    zipcode = models.CharField(blank=True, max_length=10)
    phone = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    user = models.ForeignKey(User)
    last_mod = models.DateTimeField(auto_now=True)
    lat = models.FloatField(blank=True, default=0)
    long = models.FloatField(blank=True, default=0)
    
    def text(self):
        text = self.address1 + " " + self.address2 + " " + self.city + " "
        text += " ".join([c.comment for c in Comment.objects.filter(object_pk=self.pk)]) + " "
        text += " ".join([tag.name for tag in Tag.objects.get_for_object(self)]) + " "
        text += " ".join([item.text() for item in self.menuitem_set.all()])
        return  text
    
    def get_rating(self):
        scores = [x.score for x in self.rating_set.all()]
        if len(scores) == 0:
            return 0
        return sum(scores)/(len(scores)*1.0)
    
    def get_menu_item_count(self):
        return len(self.menuitem_set.all())
    
    
    def get_comment_count(self):
        return len(Comment.objects.filter(object_pk=self.pk))
    
    def get_int_rating(self):
        return int(self.get_rating() + .5)
        
    def get_stars(self):
        star_names = [
        "Terrible",
        "Average",
        "Good",
        "Great",
        "The Best",
        "Not Rated"
        ]
        stars = ""
        rating = self.get_int_rating()
        stars += '<span id="rateStatus">%s</span>\n<div id="rateMe" title="Rate Me!">\n'%(star_names[rating-1], )
        for i in xrange(0, 5):
            if i < rating:
                c = "on"
            else:
                c = "off"
            stars += '<a id="%s" title="%s" class="%s"> </a>\n'%(i+1, star_names[i], c)
        stars += "</div>"
        return stars
    
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
        if len(all_hours) == 0:
            return []
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
        mDays = []
        lastDay = MultiDay(ordered_days.pop(0))
        mDays.append(lastDay)
        for day in ordered_days:
            if lastDay.hours == day.hours:
                lastDay.add_day(day)
            else:
                lastDay = MultiDay(day)
                mDays.append(lastDay)
        return mDays
    
    def save(self):
        if self.lat == 0 and self.long == 0:
            address = "http://maps.google.com/maps/geo?q=%s&key=%s&output=json&oe=utf8&sensor=false"
            tmp = address%(urllib.quote_plus(self.address1 + " " + self.city +" OR"), "ABQIAAAAS-5gBFgwAFQUtVAJt6dALBQLe2pAG1dPDIKxYeUNHIP8NTaN5xQ-9s8j_PpGRMwn52s44b93IVD70Q")
            goog = urllib.urlopen(tmp)
            json = simplejson.loads(goog.read())
            ll = json['Placemark'][0]["Point"]["coordinates"]
            self.lat = ll[0]
            self.long = ll[1]
        super(Restaurant, self).save()
    

DAY_CHOICES = (
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thu", "Thursday"),
    ("fri", "Friday"),
    ("sat", "Saturday"),
    ("sun", "Sunday"),
)

class MultiDay(object):
    def __init__(self, day):
        self.startDay = day.day
        self.hours = day.hours
        
    def add_day(self, day):
        self.endDay = day.day
        

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
    
    def __lt__(self, other):
        return self.open_time < other.open_time
    
    def __eq__(self, other):
        return self.open_time == other.open_time and self.close_time == other.close_time
    
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
    
    def text(self):
        return self.name + " " + self.category + " " + self.description
    
    def __unicode__(self):
        return self.name
    
    

class Rating(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    score = models.IntegerField()
