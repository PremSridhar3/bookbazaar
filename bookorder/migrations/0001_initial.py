# Generated by Django 4.2.16 on 2024-11-18 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0005_remove_book_prices"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BookOrder",
            fields=[
                ("cart_id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.PositiveIntegerField(default=0)),
                ("is_ordered", models.BooleanField(default=False)),
                ("ordered_date", models.DateTimeField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="inventory.book",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
