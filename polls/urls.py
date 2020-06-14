from django.urls import path

from .views import *
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
  url(r'^mainpage', mainpage, name='mainpage')
]
