from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    
    url('signup', views.signup, name='signup'),
    url('accounts/signup', views.signup, name='signup'),
    url('profile', views.profile, name='profile'),
    url('accounts/profile', views.profile, name='profile'),
    
    ]