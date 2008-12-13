from models import Restaurant
from django.forms import ModelForm
from django import forms
from django.contrib.localflavor.us.forms import *

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ("slug",)
