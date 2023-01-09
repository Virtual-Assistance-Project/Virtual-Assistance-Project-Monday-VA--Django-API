# Generated by Django 4.1.5 on 2023-01-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academics", "0009_alter_academic_educational_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academic",
            name="educational_level",
            field=models.CharField(
                choices=[
                    ("Early childhood education", "Isced0"),
                    ("Primary Education", "Isced1"),
                    ("Lower Secondary Education", "Isced2"),
                    ("Upper Secondary Education", "Isced3"),
                    ("Post-Secondary non-Tertiary Education", "Isced4"),
                    ("Short-cycle tertiary education", "Isced5"),
                    ("Bachelors degree or equivalent education level", "Isced6"),
                    ("Masters degree or equivalent education level", "Isced7"),
                    ("Doctoral degree or equivalent education level", "Isced8"),
                    ("Not Informed", "Default"),
                ],
                default="Not Informed",
                max_length=255,
            ),
        ),
    ]
