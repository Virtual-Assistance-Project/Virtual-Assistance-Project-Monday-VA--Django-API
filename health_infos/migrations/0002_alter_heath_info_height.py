# Generated by Django 4.1.5 on 2023-01-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("health_infos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="heath_info",
            name="height",
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
