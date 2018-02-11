from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #index, return view.index, lempar varibale name isi 'index'
    url(r'^contact/$', views.contact, name='contact'),
]