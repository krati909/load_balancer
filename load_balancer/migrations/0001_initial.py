# Generated by Django 4.1.4 on 2023-08-06 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Worker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="RequestStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("success_count", models.IntegerField(default=0)),
                ("failure_count", models.IntegerField(default=0)),
                ("total_requests", models.IntegerField(default=0)),
                ("avg_request_time", models.FloatField(default=0.0)),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="load_balancer.worker",
                    ),
                ),
            ],
        ),
    ]
