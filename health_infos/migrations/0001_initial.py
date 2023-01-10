# Generated by Django 4.1.5 on 2023-01-10 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Heath_Info",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("height", models.DecimalField(decimal_places=2, max_digits=3)),
                ("weight", models.DecimalField(decimal_places=2, max_digits=8)),
                ("bmi", models.DecimalField(decimal_places=2, max_digits=4)),
                ("ideal_weight", models.IntegerField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="health_infos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
