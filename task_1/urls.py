from django.contrib import admin
from django.urls import path
from flights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', views.FlightsList.as_view(), name="flights-list"),
    path('bookings/', views.BookingsList.as_view(), name="bookings-list"),
    path('bookings/<int:booking_id>', views.BookingsDetail.as_view(), name="booking-details"),
    path('bookings/<int:booking_id>/update', views.BookingsUpdate.as_view(), name="update-booking"),
    path('bookings/<int:booking_id>/cancel', views.BookingsDelete.as_view(), name="cancel-booking"),
]
