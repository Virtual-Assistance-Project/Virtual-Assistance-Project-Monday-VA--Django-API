# Generated by Django 4.1.5 on 2023-01-08 03:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
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
                ("title", models.CharField(max_length=128)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Trabalho", "Work"),
                            ("Dormindo", "Sleep"),
                            ("Estudo", "Study"),
                            ("Hobby", "Hobby"),
                            ("Saúde", "Health"),
                            ("Compromisso", "Commitment"),
                        ],
                        default="Compromisso",
                        max_length=16,
                    ),
                ),
                ("begans_at", models.DateTimeField(auto_now_add=True)),
                ("ends_at", models.DateTimeField(auto_now_add=True)),
                ("routine_weekdays", models.CharField(max_length=23)),
                ("description", models.TextField(max_length=500)),
            ],
        ),
    ]
