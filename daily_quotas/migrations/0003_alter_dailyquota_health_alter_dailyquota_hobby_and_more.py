# Generated by Django 4.1.5 on 2023-01-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daily_quotas", "0002_alter_dailyquota_sleep"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyquota",
            name="health",
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name="dailyquota",
            name="hobby",
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name="dailyquota",
            name="study",
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name="dailyquota",
            name="work",
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]