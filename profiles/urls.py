from django.conf.urls import url
from .views import(
				 post_edit,
				 PostEdit ,
				 post_delete ,
				 add_post )
urlpatterns = [
    url(r'^edit/$', post_edit, name='edit1'),
    url(r'^add/$', add_post, name='add'),
    url(r'^delete/$', post_delete, name='delete'),
    url(r'(?P<slug>[\w-]+)/$', PostEdit.as_view() , name='edit')
    ]