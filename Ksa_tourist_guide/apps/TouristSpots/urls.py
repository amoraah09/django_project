from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('spots/', views.spots, name='spots'),
    path('spot/<int:sId>/', views.spot, name='spot'),
    path('filter/', views.filterSpots, name='filter_spots'),
    path('add/', views.add_spot, name='add_spot'),
    path('edit/<int:sId>/', views.edit_spot, name='edit_spot'),
        path('delete/<int:sId>/', views.delete_spot, name='delete_spot'), 

]
