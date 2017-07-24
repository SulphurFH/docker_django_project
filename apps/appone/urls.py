# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^first-api/?$', views.first_api_view, name='first_api'),
]

