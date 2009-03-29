from models import Restaurant, MenuItem, Hours
from django.forms import ModelForm
from django import forms
from django.contrib.localflavor.us.forms import *
from tools.betterDateTime import ParseTimeField

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ("slug","user",'last_mod', 'lat', 'long')
        # prefix = "menu"


class HourForm(ModelForm):
    open_time = ParseTimeField()
    close_time = ParseTimeField()
    
    class Meta:
        model = Hours
        exclude = ("restaurant", )

class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        exclude = ("restaurant","user","is_available", "bad_info",'last_mod')