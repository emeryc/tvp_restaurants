from django.db import models
from django.contrib.localflavor.us.models import *

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    address1 = models.CharField("Address Line 1", max_length=50)
    address2 = models.CharField("Address Line 2", max_length=50, blank=True)
    city = models.CharField(max_length=60)
    state = USStateField(default="OR")
    zipcode = models.CharField(max_length=10)
    phone = PhoneNumberField()
    website = models.URLField(blank=True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('restaurant_details', (), {'slug': self.slug })
    
    def __unicode__(self):
        return self.name
