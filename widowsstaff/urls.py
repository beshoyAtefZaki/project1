from django.conf.urls import url , include
from . views import home ,show_processes

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^show/$', show_processes, name='show_processe'),


    ]