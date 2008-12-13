from django.contrib import admin
from models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Restaurant, RestaurantAdmin)