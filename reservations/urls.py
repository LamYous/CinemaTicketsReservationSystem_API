from django.urls import path
from . import views
urlpatterns = [
    path('halls/', views.hall_list, name="hall-list"),
    path('halls/<int:pk>/', views.hall_details, name="hall-details"),

    path('movies/', views.movie_list, name ="movie-list"),
    path('movies/<int:pk>/', views.movie_details, name ="movie-details"),

    path('showtimes/', views.showtim_list, name ="showtime-list"),
    path('showtimes/<int:pk>/', views.showtime_details, name ="showtime-details"),

    path('reservations/', views.reservation_list, name ="reservation-list"),
    path('reservations/<int:pk>/', views.reservation_details, name ="reservations-details"),
]