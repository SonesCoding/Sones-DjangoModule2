from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from .forms import Shop


# Create your views here.

def hp(request):

    if request.method == "POST":
        form = Shop(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/bye/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Shop()
    return render(request,'starshop/hp.html', {"form": form})
    
def bye(request):
    return render(request,'starshop/bye.html')

def basic(request):
     return render(request,'starshop/basic.html')
 

     