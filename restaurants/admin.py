from django.contrib import admin
from models import Restaurant, MenuItem, Hours

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 3


class HoursInline(admin.StackedInline):
    model = Hours
    extra = 3

class RestaurantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'user')
    search_fields = ('name',)
    inlines = [MenuItemInline, HoursInline]


admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(MenuItem, MenuItemAdmin)