from django.conf.urls import url
from .views import *  # Views'in icindeki butun view'leri iceri aktardik

urlpatterns = [
    url(r'^index/$', post_index),
    url(r'^detail/$', post_detail),
    url(r'^create/$', post_create),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]

# Buradaki url'leri blog/urls.py icinde include etmek gerekiyor
