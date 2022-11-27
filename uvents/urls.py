from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fans/', views.get_fans, name='get_fans'),

]