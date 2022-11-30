from django.urls import path
from . import views

urlpatterns = [
    # empty string represents "home"
    path('', views.index, name='index')
]