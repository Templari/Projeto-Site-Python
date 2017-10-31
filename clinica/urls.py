from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^generic$',views.generic),
    url(r'^index$',views.index),
    url(r'^elements$',views.elements),
    url(r'^about$',views.about)
]