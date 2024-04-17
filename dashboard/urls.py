from django.urls import path
from . import views
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView


app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('category-create', views.create_category, name='create_category'),
    path('category-list', views.list_category, name='list_category'),
    path('category-detail/<int:id>/', views.detail_category, name='detail_category'),
    path('category-update/<int:id>/', views.update_category, name='update_category'),
    path('post-create/', views.create_post, name='create_post'),
    path('regions/', views.regions, name='regions'),
    path('log-in', views.log_in, name='log_in'),
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category_retrieve_update_destroy'),


]