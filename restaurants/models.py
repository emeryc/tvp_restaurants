from django.db import models
from django.contrib.localflavor.us.models import *
from django.contrib.auth.models import User
import callbacks

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    address1 = models.CharField("Address Line 1", max_length=50)
    address2 = models.CharField("Address Line 2", max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state = USStateField(default="OR")
    zipcode = models.CharField(max_length=10)
    phone = PhoneNumberField()
    website = models.URLField(blank=True)
    user = models.ForeignKey(User)
    
    @models.permalink
    def get_absolute_url(self):
        return ('restaurant_details', (), {'slug': self.slug })
    
    def __unicode__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User)
    is_available = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant)
    bad_info = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name