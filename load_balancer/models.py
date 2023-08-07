# load_balancer_app/models.py
from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=50)

class RequestStatistics(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    success_count = models.IntegerField(default=0)
    failure_count = models.IntegerField(default=0)
    total_requests = models.IntegerField(default=0)
    avg_request_time = models.FloatField(default=0.0)
