from datetime import date as date_type, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Car, Contact, Order


BRAND_NAME = "DriveNest"


def index(request):
    featured_cars = Car.objects.filter(is_available=True)[:6]
    stats = {
        "fleet_count": Car.objects.filter(is_available=True).count(),
        "booking_count": Order.objects.filter(status__in=["Confirmed", "Completed"]).count(),
    }
    return render(request, "index.html", {"featured_cars": featured_cars, "stats": stats})


def about(request):
    return render(request, "about.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if not all([name, username, email, password, password2]):
            messages.error(request, "Please fill in all required fields.")
            return redirect("register")
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "That username is already taken.")
            return redirect("register")
        if User.objects.filter(email__iexact=email).exists():
            messages.error(request, "An account with that email already exists.")
            return redirect("register")
        if len(password) < 8:
            messages.error(request, "Password must contain at least 8 characters.")
            return redirect("register")
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
        messages.success(request, "Account created successfully. You can now sign in.")
        return redirect("signin")

    return render(request, "register.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get("loginusername", "").strip()
        password = request.POST.get("loginpassword", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name or user.username}.")
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
        return redirect("signin")
    return render(request, "login.html")


def signout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("home")


@login_required
def dashboard(request):
    bookings = Order.objects.filter(user=request.user)
    active = bookings.filter(status="Confirmed")
    return render(request, "dashboard.html", {
        "bookings": bookings[:3],
        "active_count": active.count(),
        "completed_count": bookings.filter(status="Completed").count(),
        "cancelled_count": bookings.filter(status="Cancelled").count(),
        "spent": sum(item.total_rent for item in bookings.exclude(status="Cancelled")),
    })


@login_required
def vehicles(request):
    cars = Car.objects.filter(is_available=True)
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    transmission = request.GET.get("transmission", "")
    fuel = request.GET.get("fuel", "")
    sort = request.GET.get("sort", "")

    if query:
        cars = cars.filter(Q(car_name__icontains=query) | Q(car_desc__icontains=query))
    if category:
        cars = cars.filter(category=category)
    if transmission:
        cars = cars.filter(transmission=transmission)
    if fuel:
        cars = cars.filter(fuel_type=fuel)
    if sort == "price_low":
        cars = cars.order_by("price")
    elif sort == "price_high":
        cars = cars.order_by("-price")
    elif sort == "name":
        cars = cars.order_by("car_name")

    return render(request, "vehicles.html", {
        "car": cars,
        "query": query,
        "selected_category": category,
        "selected_transmission": transmission,
        "selected_fuel": fuel,
        "selected_sort": sort,
        "categories": [item[0] for item in Car.CATEGORY_CHOICES],
        "transmissions": [item[0] for item in Car.TRANSMISSION_CHOICES],
        "fuels": [item[0] for item in Car.FUEL_CHOICES],
    })


@login_required
def bill(request):
    cars = Car.objects.filter(is_available=True)
    selected_car = request.GET.get("car", "")
    return render(request, "bill.html", {"cars": cars, "selected_car": selected_car})


@login_required
def order(request):
    if request.method != "POST":
        return redirect("bill")

    data = {
        "name": request.POST.get("billname", "").strip(),
        "email": request.POST.get("billemail", "").strip().lower(),
        "phone": request.POST.get("billphone", "").strip(),
        "address": request.POST.get("billaddress", "").strip(),
        "city": request.POST.get("billcity", "").strip(),
        "state": request.POST.get("state", "").strip(),
        "pincode": request.POST.get("pincode", "").strip(),
        "cars": request.POST.get("cars11", "").strip(),
        "car_color": request.POST.get("color1", "").strip(),
        "days": request.POST.get("dayss", "").strip(),
        "date": request.POST.get("date", "").strip(),
        "loc_from": request.POST.get("fl", "").strip(),
        "loc_to": request.POST.get("tl", "").strip(),
    }

    required = [data[key] for key in ("name", "email", "phone", "address", "city", "cars", "days", "date", "loc_from", "loc_to")]
    if not all(required):
        messages.error(request, "Please complete all required booking fields.")
        return redirect("bill")

    try:
        days = int(data["days"])
        pickup_date = date_type.fromisoformat(data["date"])
    except (ValueError, TypeError):
        messages.error(request, "Please enter a valid rental duration and pickup date.")
        return redirect("bill")

    if days < 1 or days > 30:
        messages.error(request, "Rental duration must be between 1 and 30 days.")
        return redirect("bill")
    if pickup_date < date_type.today():
        messages.error(request, "Pickup date cannot be in the past.")
        return redirect("bill")

    return_date = pickup_date + timedelta(days=days)
    car = get_object_or_404(Car, car_name=data["cars"], is_available=True)

    # Prevent overlapping active reservations for the same vehicle.
    conflicting = Order.objects.filter(
        cars=car.car_name,
        status="Confirmed",
        pickup_date__lt=return_date,
        return_date__gt=pickup_date,
    ).exists()
    if conflicting:
        messages.error(request, "That vehicle is already reserved for part of those dates. Please choose another date or vehicle.")
        return redirect("bill")

    total_rent = car.price * days
    booking = Order.objects.create(
        user=request.user,
        name=data["name"], email=data["email"], phone=data["phone"], address=data["address"],
        city=data["city"], state=data["state"], pincode=data["pincode"], cars=car.car_name,
        car_color=data["car_color"], days_for_rent=days, date=data["date"], pickup_date=pickup_date,
        return_date=return_date, loc_from=data["loc_from"], loc_to=data["loc_to"], total_rent=total_rent,
    )
    messages.success(request, f"Booking {booking.reference} confirmed. Total: ₹{total_rent:,}.")
    return redirect("my_bookings")


@login_required
def my_bookings(request):
    bookings = Order.objects.filter(user=request.user)
    return render(request, "my_bookings.html", {"bookings": bookings})


@login_required
def cancel_booking(request, order_id):
    if request.method != "POST":
        return redirect("my_bookings")
    booking = get_object_or_404(Order, order_id=order_id, user=request.user)
    if booking.status != "Confirmed":
        messages.error(request, "Only confirmed bookings can be cancelled.")
        return redirect("my_bookings")
    booking.status = "Cancelled"
    booking.save(update_fields=["status"])
    messages.success(request, f"Booking {booking.reference} has been cancelled.")
    return redirect("my_bookings")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("contactname", "").strip()
        email = request.POST.get("contactemail", "").strip().lower()
        phone = request.POST.get("contactnumber", "").strip()
        message_text = request.POST.get("contactmsg", "").strip()
        if not all([name, email, phone, message_text]):
            messages.error(request, "Please complete every contact field.")
            return redirect("contact")
        Contact.objects.create(name=name, email=email, phone_number=phone, message_text=message_text)
        messages.success(request, "Thanks. Your message has been received.")
        return redirect("contact")
    return render(request, "contact.html")
