
from django.urls import path 
from . import views
urlpatterns = [

    path('', views.hp , name="homepage"),
    path('bye', views.bye, name="bye"),
    path('basic', views.basic, name="basic"),
]
