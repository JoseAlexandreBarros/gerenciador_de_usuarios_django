#from atexit import register
from django.urls import path,include, re_path
from . import views


urlpatterns = [
    
    path("oauth/", include("social_django.urls")),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/',views.register,name='register')
]