from django.conf.urls import patterns, url
from stally import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^market/$', views.markets, name='markets'),
    url(r'^market/(?P<market_name_slug>[\w\-]+)/$', views.market, name='market'),
    url(r'^stall/$', views.stalls, name='stalls'),
    url(r'^stall/(?P<stall_name_slug>[\w\-]+)/$', views.stall, name='stall'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    ]