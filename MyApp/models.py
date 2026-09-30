from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    CATEGORY_CHOICES = [
        ("Hatchback", "Hatchback"),
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("Luxury", "Luxury"),
    ]
    TRANSMISSION_CHOICES = [("Manual", "Manual"), ("Automatic", "Automatic")]
    FUEL_CHOICES = [("Petrol", "Petrol"), ("Diesel", "Diesel"), ("CNG", "CNG"), ("Electric", "Electric")]

    car_id = models.IntegerField(unique=True, default=0)
    car_name = models.CharField(max_length=60, default="")
    car_desc = models.CharField(max_length=300, default="")
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="uploads/cars", default="")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Sedan")
    seats = models.PositiveSmallIntegerField(default=5)
    transmission = models.CharField(max_length=15, choices=TRANSMISSION_CHOICES, default="Manual")
    fuel_type = models.CharField(max_length=15, choices=FUEL_CHOICES, default="Petrol")
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ["car_id"]

    def __str__(self):
        return self.car_name

    @property
    def image_source(self):
        if self.image and self.image.name:
            return self.image.url
        return ""


class Order(models.Model):
    STATUS_CHOICES = [
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings", null=True, blank=True)
    name = models.CharField(max_length=90, default="")
    email = models.EmailField(max_length=150, default="")
    phone = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="", blank=True)
    pincode = models.CharField(max_length=10, default="", blank=True)
    cars = models.CharField(max_length=60, default="")
    car_color = models.CharField(max_length=20, default="", blank=True)
    days_for_rent = models.PositiveIntegerField(default=0)
    date = models.CharField(max_length=50, default="")
    pickup_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    loc_from = models.CharField(max_length=50, default="")
    loc_to = models.CharField(max_length=50, default="")
    total_rent = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Confirmed")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"#{self.order_id} - {self.name} - {self.cars}"

    @property
    def reference(self):
        return f"DN-{self.order_id:05d}"


class Contact(models.Model):
    name = models.CharField(max_length=150, default="")
    email = models.EmailField(max_length=150, default="")
    phone_number = models.CharField(max_length=15, default="")
    message_text = models.TextField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
