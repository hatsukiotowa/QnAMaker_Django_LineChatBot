from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^callback/', views.callback),
]