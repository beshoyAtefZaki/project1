from django.conf.urls import url , include

from .views import BlogPost
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPost.as_view(), name='api_view')
  
]