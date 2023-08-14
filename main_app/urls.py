
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('homes/', views.homes_index, name='index'),
    path('homes/<int:home_id>/', views.homes_detail, name='detail'),
    path('homes/create/', views.HomeCreate.as_view(), name='homes_create'),
    path('homes/<int:pk>/update/', views.HomeUpdate.as_view(), name='homes_update'),
    path('homes/<int:pk>/delete/', views.HomeDelete.as_view(), name='homes_delete'),
    path('rents/', views.rents_index, name='rent_index'),
    path('rents/<int:rent_id>/', views.rents_detail, name='rent_detail'),
    path('rents/create/', views.RentCreate.as_view(), name='rents_create'),
    path('rents/<int:pk>/update/', views.RentUpdate.as_view(), name='rents_update'),
    path('rents/<int:pk>/delete/', views.RentDelete.as_view(), name='rents_delete'),
    path('furnitures/', views.furnitures_index, name='furniture_index'),
    path('furnitures/<int:furniture_id>/', views.furnitures_detail, name='furniture_detail'),
    path('furnitures/create/', views.FurnitureCreate.as_view(), name='furnitures_create'),
    path('furnitures/<int:pk>/update/', views.FurnitureUpdate.as_view(), name='furnitures_update'),
    path('furnitures/<int:pk>/delete/', views.FurnitureDelete.as_view(), name='furnitures_delete'),
    path('furnitures/<int:home_id>/assoc_furniture/<int:furniture_id>/', views.assoc_furniture, name='assoc_furniture'),
    path('furnitures/<int:home_id>/unassoc_furniture/<int:furniture_id>/', views.unassoc_furniture, name='unassoc_furniture'),
    path('homes/<int:home_id>/add_review/', views.add_review, name='add_review'),
]