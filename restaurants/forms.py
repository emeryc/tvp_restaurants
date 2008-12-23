from models import Restaurant, MenuItem
from django.forms import ModelForm
from django import forms
from django.contrib.localflavor.us.forms import *

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ("slug","user",'last_mod')


class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        exclude = ("restaurant","user","is_available", "bad_info",'last_mod')