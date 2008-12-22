from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from forms import RestaurantForm, MenuItemForm
from models import Restaurant, MenuItem
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from tagging.utils import parse_tag_input
from tagging.models import Tag
import simplejson

@login_required
def add(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)        
        if form.is_valid():
            model = form.save(commit=False)
            model.slug = slugify(model.name)
            model.user = request.user
            model.save()
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = RestaurantForm()
    return render_to_response("restaurants/add.html", {'form': form})


@login_required
def add_item(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    if request.method == "POST":
        form = MenuItemForm(request.POST)        
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.restaurant = restaurant
            model.is_available = True
            model.save()
            return HttpResponseRedirect("../")
    else:
        form = MenuItemForm()
    return render_to_response("restaurants/add_item.html", {'form': form})


@login_required
def not_available(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    item.is_available = False
    item.save()
    return HttpResponseRedirect("../../")


@login_required
def bad_info(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    item.bad_info = True
    item.save()
    return HttpResponseRedirect("../../")


def tag(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    tags = parse_tag_input(request.GET["tags"])
    for tag in tags:
        Tag.objects.add_tag(restaurant, tag + ",")
    to_return = {}
    tags = Tag.objects.get_for_object(restaurant)
    tag_names = []
    for tag in tags:
        tag_names.append('<a href="../tags/' + tag.name + '">' + tag.name +'</a>')
    to_return["tags"] = tag_names
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")
    
    
