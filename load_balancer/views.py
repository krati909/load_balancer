# load_balancer_app/views.py
import threading
from random import randint

from django.http import JsonResponse
from .models import Worker, RequestStatistics
# List to store worker names for round-robin load balancing
worker_names = []
# Current worker index for round-robin distribution
current_worker_index = 0
# Lock for accessing the worker_names list and current_worker_index
worker_lock = threading.Lock()


def round_robin_load_balancer(failure_percentage):
    # Get the worker to which the request should be assigned
    worker = get_next_worker()
    # Update request statistics for the assigned worker
    status=update_request_statistics(worker,failure_percentage)

    # Execute the request on the assigned worker (Replace this with actual logic to execute the request)
    if status==True:
        return (
             'Request executed on worker: {}'.format(worker.name)
        )
    else:
        return ('Request failed')



def get_next_worker():
    global current_worker_index
    workers=Worker.objects.all()
    if not workers:  # if no worker  available in database raising exception.
        raise Exception("No workers available.")

    worker = workers[current_worker_index]
    current_worker_index = (current_worker_index + 1) % len(workers)
    return worker

def update_request_statistics(worker,failure_percentage):
    # Fetch the request statistics for the given worker
    try:
        request_stats = RequestStatistics.objects.get(worker=worker)
    except RequestStatistics.DoesNotExist:
        # If the worker's statistics do not exist, create a new entry
        request_stats = RequestStatistics(worker=worker)

    # Update the statistics
    request_stats.total_requests += 1
    # Calculate the average request time (replace this with actual request time calculation)
    avg_request_time = calculate_avg_request_time(request_stats.total_requests, request_stats.avg_request_time)
    request_stats.avg_request_time = avg_request_time


    # Replace the following logic with actual success/failure response handling
    if randint(1,100) < failure_percentage:
        request_stats.failure_count += 1
        # Save the updated statistics
        request_stats.save()
        return False
    else:
        request_stats.success_count += 1
        # Save the updated statistics
        request_stats.save()
        return True


def calculate_avg_request_time(total_requests, current_avg_time):

    request_time = 0.5  # Use the actual request time
    new_avg_time = (current_avg_time * (total_requests - 1) + request_time) / total_requests
    return new_avg_time

