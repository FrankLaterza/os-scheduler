import sys

class Process:
    def __init__(self, name, arrival, burst):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.remaining_time = burst
        self.start_time = None
        self.completion_time = None
        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = None

def parse_input_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(1)

    processes = []
    algorithm = None
    quantum = None
    total_time = None

    for line in lines:
        parts = line.strip().split()
        if parts[0] == 'processcount':
            process_count = int(parts[1])
        elif parts[0] == 'runfor':
            total_time = int(parts[1])
        elif parts[0] == 'use':
            algorithm = parts[1]
        elif parts[0] == 'quantum':
            quantum = int(parts[1])
        elif parts[0] == 'process':
            name = parts[2]
            arrival = int(parts[4])
            burst = int(parts[6])
            processes.append(Process(name, arrival, burst))

    if algorithm == 'rr' and quantum is None:
        print("Error: Missing quantum parameter when use is 'rr'")
        sys.exit(1)

    return processes, algorithm, quantum, total_time

def fifo_scheduler(processes, total_time):
    processes.sort(key=lambda p: p.arrival)
    time = 0
    log = []
    for process in processes:
        if time < process.arrival:
            while time < process.arrival:
                log.append(f"Time {time:>3} : Idle")
                time += 1
        log.append(f"Time {process.arrival:>3} : {process.name} arrived")
        process.start_time = time
        process.wait_time = time - process.arrival
        time += process.burst
        process.completion_time = time
        process.turnaround_time = process.completion_time - process.arrival
        process.response_time = process.wait_time
        log.append(f"Time {process.start_time:>3} : {process.name} selected (burst {process.burst:>3})")
        log.append(f"Time {process.completion_time:>3} : {process.name} finished")
    while time < total_time:
        log.append(f"Time {time:>3} : Idle")
        time += 1
    return log

def sjf_scheduler(processes, total_time):
    time = 0
    log = []
    ready_queue = []
    while time < total_time:
        for process in processes:
            if process.arrival == time:
                ready_queue.append(process)
                log.append(f"Time {time:>3} : {process.name} arrived")
        if ready_queue:
            ready_queue.sort(key=lambda p: p.remaining_time)
            current_process = ready_queue.pop(0)
            if current_process.start_time is None:
                current_process.start_time = time
                current_process.response_time = time - current_process.arrival
            current_process.remaining_time -= 1
            if current_process.remaining_time == 0:
                current_process.completion_time = time + 1
                current_process.turnaround_time = current_process.completion_time - current_process.arrival
                current_process.wait_time = current_process.turnaround_time - current_process.burst
                log.append(f"Time {time + 1:>3} : {current_process.name} finished")
            else:
                ready_queue.append(current_process)
            log.append(f"Time {time:>3} : {current_process.name} selected (burst {current_process.remaining_time:>3})")
        else:
            log.append(f"Time {time:>3} : Idle")
        time += 1
    return log

def round_robin_scheduler(processes, total_time, quantum):
    time = 0
    log = []
    ready_queue = []

    while time < total_time:
        for process in processes:
            if process.arrival == time:
                ready_queue.append(process)
                log.append(f"Time {time:>3} : {process.name} arrived")

        if ready_queue:
            current_process = ready_queue.pop(0)
            if current_process.start_time is None:
                current_process.start_time = time
                current_process.response_time = time - current_process.arrival

            execution_time = min(quantum, current_process.remaining_time)
            current_process.remaining_time -= execution_time
            time += execution_time

            log.append(f"Time {time - execution_time:>3} : {current_process.name} selected (burst {execution_time:>3})")

            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival
                current_process.wait_time = current_process.turnaround_time - current_process.burst
                log.append(f"Time {time:>3} : {current_process.name} finished")
            else:
                ready_queue.append(current_process)
        else:
            log.append(f"Time {time:>3} : Idle")
            time += 1
    return log

def calculate_metrics(processes):
    metrics = []
    for process in processes:
        response_time = process.response_time if process.response_time is not None else 0
        metrics.append(f"{process.name} wait {process.wait_time:>3} turnaround {process.turnaround_time:>3} response {response_time:>3}")
    return metrics

def write_output_file(filename, log, metrics, algorithm, quantum=None):
    with open(filename, 'w') as file:
        file.write(f"{len(metrics)} processes\n")
        if algorithm == 'fcfs':
            file.write("Using First-Come First-Served\n")
        elif algorithm == 'sjf':
            file.write("Using preemptive Shortest Job First\n")
        elif algorithm == 'rr':
            file.write("Using Round-Robin\n")
            file.write(f"Quantum {quantum:>3}\n")
        for entry in log:
            file.write(entry + "\n")
        last_time = int(log[-1].split()[1])
        file.write(f"Finished at time {last_time:>3}\n\n")
        for metric in metrics:
            file.write(metric + "\n")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not input_file.endswith('.in'):
        print(f"Usage: {sys.argv[0]} <input file>")
        sys.exit(1)

    processes, algorithm, quantum, total_time = parse_input_file(input_file)

    if algorithm == 'fcfs':
        log = fifo_scheduler(processes, total_time)
    elif algorithm == 'sjf':
        log = sjf_scheduler(processes, total_time)
    elif algorithm == 'rr':
        log = round_robin_scheduler(processes, total_time, quantum)
    else:
        print(f"Error: Unknown algorithm {algorithm}")
        sys.exit(1)

    metrics = calculate_metrics(processes)
    output_file = input_file.replace('.in', '.out')
    write_output_file(output_file, log, metrics, algorithm, quantum if algorithm == 'rr' else None)

if __name__ == "__main__":
    main()