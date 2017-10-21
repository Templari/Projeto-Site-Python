from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^generic/',views.generic, name='generic'),
]