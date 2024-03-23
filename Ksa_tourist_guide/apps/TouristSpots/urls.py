from django.urls import path
from apps.TouristSpots import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('spots', views.spots),
    path('register', views.register),
    path('spot/<int:sId>', views.spot),
    path('filterSpots', views.filterSpots, name="filterSpots")

]
