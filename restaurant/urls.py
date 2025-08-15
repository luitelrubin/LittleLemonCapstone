from django.urls import path, include

from . import views

app_name = "restaurant"


urlpatterns = [
    # API endpoints: Menu
    path("menu", views.MenuItemView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    # API endpoints: Booking
    # path("booking", views.BookingView.as_view()),
    # path("booking/<int:pk>", views.BookingView.as_view()),
]
