from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import RestaurantForm

def add(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)        
        if form.is_valid():
            model = form.save()
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = RestaurantForm()
    return render_to_response("restaurants/add.html", {'form': form})