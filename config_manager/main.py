# main.py
# ...


# ...
from config_manager.manager import read_config_file, spawn_workers

global avg_delay, failure_percentage
def config_manage():
    # Read the configuration file and extract parameters
    config_file_path ="configuration"
    config_params = read_config_file(config_file_path)

    # Convert some parameters to appropriate data types (e.g., int, float)
    num_workers = int(config_params.get('Number of workers', 3))
    request_pool_size = int(config_params.get('Request pool size', 10))
    stats_directory = config_params.get('Stats directory', '/path/to/stats/directory')
    avg_delay = float(config_params.get('Average Delay in sec', 0.5))
    failure_percentage = float(config_params.get('Failure percentage', 10))

    # Spawn workers based on the configuration parameters
    spawn_workers(
        num_workers=num_workers,
        request_pool_size=request_pool_size,
        stats_directory=stats_directory,
        avg_delay=avg_delay,
        failure_percentage=failure_percentage
    )
    return avg_delay,failure_percentage

# ...
