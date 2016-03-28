from django.conf.urls import patterns, url
from booker import views

urlpatterns = [
    url(r'^$', views.index, name='booker'),
    url(r'^stallowner/$', views.stallowner, name='stallowner'),
    url(r'^marketowner/$', views.marketowner, name='marketowner'),
    url(r'^application/$', views.application, name='application')
    ]