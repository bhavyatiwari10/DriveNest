from django.urls import path
from MyApp import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.index, name="home_alias"),
    path("about/", views.about, name="about"),
    path("vehicles/", views.vehicles, name="vehicles"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("book/", views.bill, name="bill"),
    path("book/confirm/", views.order, name="order"),
    path("bookings/", views.my_bookings, name="my_bookings"),
    path("bookings/<int:order_id>/cancel/", views.cancel_booking, name="cancel_booking"),
    path("contact/", views.contact, name="contact"),
]
