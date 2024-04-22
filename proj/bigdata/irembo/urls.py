from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL to the index view
]
