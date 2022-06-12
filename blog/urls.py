from django.urls import path
from . import views

urlpatterns = [
    path('muller', views.post_list, name='post_list'),
    path('', views.interactions, name='interactions'),
]
