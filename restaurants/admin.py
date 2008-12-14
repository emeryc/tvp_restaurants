from django.contrib import admin
from models import Restaurant, MenuItem

class RestaurantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'user')
    search_fields = ('name',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'bad_info', 'is_available', 'user', 'restaurant')
    list_filter = ('bad_info', 'is_available', 'restaurant')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(MenuItem, MenuItemAdmin)