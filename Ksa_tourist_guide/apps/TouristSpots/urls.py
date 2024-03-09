from django.urls import path
from apps.TouristSpots import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('spots', views.spots),
    path('spot/<int:sId>', views.spot)
]