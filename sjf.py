"""
SJF (Shortest Job First) Scheduling Algorithm
Non-preemptive scheduling where the process with shortest burst time executes first.
"""

def calculate_sjf(processes):
    """
    Calculate waiting time and turnaround time for SJF scheduling.
    
    Args:
        processes: List of dictionaries containing process information
                   Each process should have: 'pid', 'burst_time', 'arrival_time'
    
    Returns:
        List of processes with calculated waiting_time and turnaround_time
    """
    n = len(processes)
    current_time = 0
    completed = 0
    is_completed = [False] * n
    
    # Store results in order of completion
    result = []
    
    while completed < n:
        # Find process with shortest burst time among arrived processes
        shortest_idx = -1
        shortest_burst = float('inf')
        
        for i in range(n):
            # Check if process has arrived and not completed
            if (not is_completed[i] and 
                processes[i]['arrival_time'] <= current_time and
                processes[i]['burst_time'] < shortest_burst):
                shortest_burst = processes[i]['burst_time']
                shortest_idx = i
        
        # If no process has arrived yet, jump to next arrival
        if shortest_idx == -1:
            # Find the next process to arrive
            next_arrival = float('inf')
            for i in range(n):
                if not is_completed[i] and processes[i]['arrival_time'] < next_arrival:
                    next_arrival = processes[i]['arrival_time']
            current_time = next_arrival
            continue
        
        # Execute the shortest process
        process = processes[shortest_idx]
        
        # Waiting time = current time - arrival time
        process['waiting_time'] = current_time - process['arrival_time']
        
        # Turnaround time = waiting time + burst time
        process['turnaround_time'] = process['waiting_time'] + process['burst_time']
        
        # Update current time
        current_time += process['burst_time']
        
        # Mark as completed
        is_completed[shortest_idx] = True
        completed += 1
        
        # Add to result (for display in execution order)
        result.append(process.copy())
    
    return result


def display_gantt_chart(execution_timeline):
    """
    Display a visual Gantt chart showing process execution timeline.
    
    Args:
        execution_timeline: List of execution segments with process info
    """
    print("\n" + "="*80)
    print("Gantt Chart")
    print("="*80 + "\n")
    
    if not execution_timeline:
        print("No processes to display.\n")
        return
    
    # Draw the chart
    # Top border
    print("┌", end="")
    for segment in execution_timeline:
        width = min(segment['duration'] * 2, 20)  # Limit max width for readability
        if width < 2:
            width = 2
        print("─" * width + "┬", end="")
    print("┐")
    
    # Process labels
    print("│", end="")
    for segment in execution_timeline:
        label = segment['label']
        width = min(segment['duration'] * 2, 20)
        if width < 2:
            width = 2
        padding = (width - len(label)) // 2
        print(" " * padding + label + " " * (width - padding - len(label)) + "│", end="")
    print()
    
    # Bottom border
    print("└", end="")
    for segment in execution_timeline:
        width = min(segment['duration'] * 2, 20)
        if width < 2:
            width = 2
        print("─" * width + "┴", end="")
    print("┘")
    
    # Time markers
    print("0", end="")
    for segment in execution_timeline:
        width = min(segment['duration'] * 2, 20)
        if width < 2:
            width = 2
        time_str = str(segment['end'])
        # Adjust spacing based on width
        spaces = width - len(time_str) + 1
        print(" " * spaces + time_str, end="")
    print("\n")
    
    # Execution sequence
    execution_order = " → ".join([seg['label'] for seg in execution_timeline])
    print(f"Execution Sequence: {execution_order}\n")


def calculate_sjf(processes):
    """
    Calculate waiting time and turnaround time for SJF scheduling.
    
    Args:
        processes: List of dictionaries containing process information
                   Each process should have: 'pid', 'burst_time', 'arrival_time'
    
    Returns:
        Tuple of (processes_list, execution_timeline)
    """
    n = len(processes)
    current_time = 0
    completed = 0
    is_completed = [False] * n
    
    # Store results in order of completion
    result = []
    execution_timeline = []
    
    while completed < n:
        # Find process with shortest burst time among arrived processes
        shortest_idx = -1
        shortest_burst = float('inf')
        
        for i in range(n):
            # Check if process has arrived and not completed
            if (not is_completed[i] and 
                processes[i]['arrival_time'] <= current_time and
                processes[i]['burst_time'] < shortest_burst):
                shortest_burst = processes[i]['burst_time']
                shortest_idx = i
        
        # If no process has arrived yet, jump to next arrival
        if shortest_idx == -1:
            # Find the next process to arrive
            next_arrival = float('inf')
            for i in range(n):
                if not is_completed[i] and processes[i]['arrival_time'] < next_arrival:
                    next_arrival = processes[i]['arrival_time']
            
            # Add idle time to timeline
            if next_arrival > current_time:
                execution_timeline.append({
                    'label': 'IDLE',
                    'start': current_time,
                    'end': next_arrival,
                    'duration': next_arrival - current_time
                })
            
            current_time = next_arrival
            continue
        
        # Execute the shortest process
        process = processes[shortest_idx]
        
        # Waiting time = current time - arrival time
        process['waiting_time'] = current_time - process['arrival_time']
        
        # Turnaround time = waiting time + burst time
        process['turnaround_time'] = process['waiting_time'] + process['burst_time']
        
        # Add to execution timeline
        execution_timeline.append({
            'label': f"P{process['pid']}",
            'start': current_time,
            'end': current_time + process['burst_time'],
            'duration': process['burst_time']
        })
        
        # Update current time
        current_time += process['burst_time']
        
        # Mark as completed
        is_completed[shortest_idx] = True
        completed += 1
        
        # Add to result (for display in execution order)
        result.append(process.copy())
    
    return result, execution_timeline


def display_sjf_results(processes, execution_timeline):
    """
    Display SJF scheduling results in a formatted table.
    
    Args:
        processes: List of processes with calculated metrics
        execution_timeline: Timeline of process execution for Gantt chart
    """
    print("\n" + "="*80)
    print("SJF (Shortest Job First) Scheduling Results")
    print("="*80)
    
    # Display Gantt Chart first
    display_gantt_chart(execution_timeline)
    
    # Table header
    print("="*80)
    print("Process Details")
    print("="*80)
    print(f"{'Process':<10} {'Arrival':<12} {'Burst':<12} {'Waiting':<12} {'Turnaround':<12}")
    print(f"{'ID':<10} {'Time':<12} {'Time':<12} {'Time':<12} {'Time':<12}")
    print("-"*80)
    
    # Sort by PID for display
    processes_sorted = sorted(processes, key=lambda x: x['pid'])
    
    # Process details
    total_waiting = 0
    total_turnaround = 0
    
    for process in processes_sorted:
        print(f"P{process['pid']:<9} {process['arrival_time']:<12} "
              f"{process['burst_time']:<12} {process['waiting_time']:<12} "
              f"{process['turnaround_time']:<12}")
        
        total_waiting += process['waiting_time']
        total_turnaround += process['turnaround_time']
    
    # Calculate averages
    n = len(processes)
    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n
    
    print("-"*80)
    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")
    print("="*80 + "\n")


def get_sjf_input():
    """
    Get user input for SJF scheduling.
    
    Returns:
        List of process dictionaries
    """
    processes = []
    
    try:
        n = int(input("Enter number of processes: "))
        
        if n <= 0:
            print("Error: Number of processes must be positive!")
            return None
        
        print("\n" + "-"*60)
        print("Enter process details:")
        print("• Burst Time: Time required for process execution")
        print("• Arrival Time: When process enters ready queue")
        print("  (Press Enter to use default value 0)")
        print("-"*60)
        
        for i in range(n):
            print(f"\n📌 Process {i+1}:")
            
            # Get burst time
            burst_time = int(input(f"  Burst Time: "))
            if burst_time <= 0:
                print("❌ Error: Burst time must be positive!")
                return None
            
            # Get arrival time (optional)
            arrival_input = input(f"  Arrival Time [default: 0]: ").strip()
            arrival_time = int(arrival_input) if arrival_input else 0
            
            if arrival_time < 0:
                print("❌ Error: Arrival time cannot be negative!")
                return None
            
            processes.append({
                'pid': i + 1,
                'burst_time': burst_time,
                'arrival_time': arrival_time,
                'waiting_time': 0,
                'turnaround_time': 0
            })
        
        return processes
    
    except ValueError:
        print("❌ Error: Please enter valid integer values!")
        return None


def run_sjf():
    """
    Main function to run SJF scheduling algorithm.
    """
    print("\n" + "="*80)
    print("SJF (Shortest Job First) Scheduling")
    print("="*80 + "\n")
    
    processes = get_sjf_input()
    
    if processes is None:
        print("SJF scheduling aborted due to invalid input.\n")
        return
    
    # Calculate scheduling metrics
    processes, execution_timeline = calculate_sjf(processes)
    
    # Display results
    display_sjf_results(processes, execution_timeline)


# For testing this module independently
if __name__ == "__main__":
    run_sjf()
