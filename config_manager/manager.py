import threading

from load_balancer.models import Worker

# ...
from load_balancer.views import worker_names


def spawn_workers(num_workers, request_pool_size, stats_directory, avg_delay, failure_percentage):
    # for i in range(num_workers):
    #     worker_name = f"Worker_{i}"
    #     worker = Worker.objects.create(name=worker_name)
    #     worker_names.append(worker_name)
    pass
    # # Run the Load Balancer
    # lb_thread = threading.Thread(target=round_robin_load_balancer, args=(failure_percentage,))
    # lb_thread.start()
    #
    # # Run the WebApp
    # webapp_thread = threading.Thread(target=hello_view, args=(avg_delay))
    # webapp_thread.start()
def read_config_file(config_file_path):
    config_params = {}

    with open(config_file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                param, value = line.split('=')
                config_params[param.strip()] = value.strip()

    return config_params
