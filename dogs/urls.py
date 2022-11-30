from django.urls import path
from .views import DogsView, DogDetailView

urlpatterns = [
  path('', DogsView.as_view(), name='dogs'),
  path('<int:pk>/', DogDetailView.as_view(), name='dogs'),
]