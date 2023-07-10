# Generated by Django 4.2.2 on 2023-07-09 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="type",
            field=models.CharField(
                choices=[("CAT", "Cat"), ("DOG", "Dog"), ("CAPYBARA", "Capybara")],
                default=None,
            ),
        ),
    ]
