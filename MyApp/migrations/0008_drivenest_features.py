from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("MyApp", "0007_modernize_models")]

    operations = [
        migrations.AddField(model_name="car", name="category", field=models.CharField(choices=[("Hatchback", "Hatchback"), ("Sedan", "Sedan"), ("SUV", "SUV"), ("Luxury", "Luxury")], default="Sedan", max_length=20)),
        migrations.AddField(model_name="car", name="seats", field=models.PositiveSmallIntegerField(default=5)),
        migrations.AddField(model_name="car", name="transmission", field=models.CharField(choices=[("Manual", "Manual"), ("Automatic", "Automatic")], default="Manual", max_length=15)),
        migrations.AddField(model_name="car", name="fuel_type", field=models.CharField(choices=[("Petrol", "Petrol"), ("Diesel", "Diesel"), ("CNG", "CNG"), ("Electric", "Electric")], default="Petrol", max_length=15)),
        migrations.AddField(model_name="car", name="is_available", field=models.BooleanField(default=True)),
        migrations.AddField(model_name="order", name="pickup_date", field=models.DateField(blank=True, null=True)),
        migrations.AddField(model_name="order", name="return_date", field=models.DateField(blank=True, null=True)),
        migrations.AlterField(model_name="order", name="status", field=models.CharField(choices=[("Confirmed", "Confirmed"), ("Completed", "Completed"), ("Cancelled", "Cancelled")], default="Confirmed", max_length=20)),
        migrations.AlterField(model_name="car", name="car_name", field=models.CharField(default="", max_length=60)),
        migrations.AlterField(model_name="order", name="cars", field=models.CharField(default="", max_length=60)),
    ]
