from django.db import migrations, models
from django.utils import timezone
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("MyApp", "0006_contact"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(default="", upload_to="uploads/cars"),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.RenameField(
            model_name="contact",
            old_name="message",
            new_name="message_text",
        ),
        migrations.AddField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(default="", max_length=150),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="bookings", to="auth.user"),
        ),
        migrations.AddField(
            model_name="order",
            name="state",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AddField(
            model_name="order",
            name="pincode",
            field=models.CharField(blank=True, default="", max_length=10),
        ),
        migrations.AddField(
            model_name="order",
            name="car_color",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
        migrations.AddField(
            model_name="order",
            name="total_rent",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(default="Confirmed", max_length=20),
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.EmailField(default="", max_length=150),
        ),
        migrations.AlterField(
            model_name="order",
            name="days_for_rent",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
