from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
]
