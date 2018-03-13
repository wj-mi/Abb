
from django.conf.urls import url
from . import views


app_name = 'myapp'

urlpatterns = [
    url(r'^index/$', views.say_hello, name='index'),
]
