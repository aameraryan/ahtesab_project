from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='portal/login.html'), name='login'),
    url(r'^daily/$', views.daily, name='daily'),
    url(r'^day/add/$', views.day_add, name='day_add'),
    url(r'^day/update/(?P<u_day>[0-9]+)/(?P<u_month>[0-9]+)/(?P<u_year>[0-9]{4})/$', views.day_update,
        name='day_update'),

    url(r'^weekly/$', views.weekly, name='weekly'),
    url(r'^week/add/$', views.week_add, name='week_add'),

    url(r'^monthly/$', views.monthly, name='monthly'),
    url(r'^month/add/$', views.month_add, name='month_add'),
    url(r'^month/update/(?P<u_month>[0-9]+)/(?P<u_year>[0-9]+)/$', views.month_update, name='month_update'),

]
