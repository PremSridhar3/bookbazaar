# Generated by Django 4.2.16 on 2024-11-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_alter_book_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="prices",
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
    ]
