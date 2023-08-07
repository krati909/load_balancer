# load_balancer_app/views.py
import random
import time

from django.db.models import Sum
from django.http import JsonResponse

from config_manager.main import config_manage
from load_balancer.models import Worker, RequestStatistics
from load_balancer.views import round_robin_load_balancer


def hello_view(request):
    avg_delay,failure_percentage=config_manage()
    msg=round_robin_load_balancer(failure_percentage)
    # Introduce random sleep time to simulate the average delay in the configuration
    sleep_time = avg_delay
    time.sleep(sleep_time)

    response_data = {
        'message': 'Hello from WebApp!',
        'status':msg,
        'average_delay': sleep_time
    }

    return JsonResponse(response_data)

def stats_view(request):
    # Fetch statistics from the RequestStatistics model and return them as JSON response
    workers = Worker.objects.all()
    stats = {
            'success_count': {'Total':RequestStatistics.objects.aggregate(Sum('success_count'))['success_count__sum']},
           'failure_count':{'Total': RequestStatistics.objects.aggregate(Sum('failure_count'))['failure_count__sum']},
            'total_requests':{'Total': RequestStatistics.objects.aggregate(Sum('total_requests'))['total_requests__sum']},
            'avg_request_time':{'Total': RequestStatistics.objects.aggregate(Sum('avg_request_time'))['avg_request_time__sum']/len(workers)}
        }
    for worker in workers:
        w=RequestStatistics.objects.get(worker=worker)
        stats['success_count'][worker.name]=w.success_count
        stats['failure_count'][worker.name] = w.failure_count
        stats['total_requests'][worker.name] = w.total_requests
        stats['avg_request_time'][worker.name] = w.avg_request_time

    return JsonResponse(stats)

