from django.urls import path
from .views import app, index_view

urlpatterns = [
    path('app/', app, name='app'),
    path('index/', index_view, name='index'),
]