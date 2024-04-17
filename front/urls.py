from django.urls import path
from . import views


app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('log-in', views.log_in, name='log_in'),

]