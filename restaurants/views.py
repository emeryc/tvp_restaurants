from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from forms import RestaurantForm, MenuItemForm
from models import Restaurant, MenuItem, Rating
from django.contrib.auth.decorators import login_required
from django.contrib import comments
from django.contrib.comments.forms import CommentForm
from django.template.defaultfilters import slugify
from tagging.utils import parse_tag_input
from tagging.models import Tag
import simplejson
from django.template import RequestContext

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


@login_required
def tag(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    tags = parse_tag_input(request.GET["tags"])
    for tag in tags:
        Tag.objects.add_tag(restaurant, tag + ",")
    to_return = {}
    to_return["tags"] = getTags(restaurant)
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")


sizeClass = ["", "tiny", "small", "medium", "big"]
def getTags(restaurant):
    tags = Tag.objects.get_for_object(restaurant)
    cloud = Tag.objects.cloud_for_model(Restaurant)
    tag_html = []
    for tag in cloud:
        if tag in tags:
            tag_html.append('<a class="' + sizeClass[tag.font_size] + '" href="../tags/' + tag.name + '">' + tag.name +'</a>')

    # for tag in tags:
    #         tag_html.append('<a href="../tags/' + tag.name + '">' + tag.name +'</a>')
    return tag_html

@login_required
def rate(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    score = request.GET["value"]
    ratings = Rating.objects.filter(restaurant=restaurant).filter(user=request.user)
    if len(ratings) > 0:
        ratings[0].score = int(score)
        ratings[0].save()
    else:
        newRating = Rating(restaurant=restaurant, user=request.user, score=int(score))
        newRating.save()
    newScore = restaurant.get_int_rating()
    to_return = {"score":newScore}
    serialized = simplejson.dumps(to_return)
    return HttpResponse(serialized, mimetype="application/json")


def restaurant(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    mform = MenuItemForm()
    cform = comments.get_form()(restaurant)
    
    if request.method == "POST":
        if request.GET["type"] == "menu":
            mform = MenuItemForm(request.POST, auto_id="menu_id_%s")
            if mform.is_valid():
                model = mform.save(commit=False)
                model.user = request.user
                model.restaurant = restaurant
                model.is_available = True
                model.save()
                mform = MenuItemForm()
        else :
            cform = comments.get_form()(restaurant, data=request.POST.copy())
            if cform.is_valid():
                comment = cform.get_comment_object()
                comment.ip_address = request.META.get("REMOTE_ADDR", None)
                if request.user.is_authenticated():
                    comment.user = request.user
                comment.save()
                cform = comments.get_form()(restaurant)
    
    mform.prefix = "menu"
    del cform.fields['honeypot']
    del cform.fields['url']  
    return render_to_response("restaurants/restaurant_detail.html", {'menu_form': mform, 'comment_form': cform, 'object': restaurant, 'tags':getTags(restaurant)}, context_instance=RequestContext(request))