from django.urls import path
from .views import CatsView, CatDetailView

urlpatterns = [
  path('', CatsView.as_view(), name='cats'),
  path('<int:pk>/', CatDetailView.as_view(), name='cats'),
]