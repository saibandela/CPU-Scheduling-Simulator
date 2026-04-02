"""
FCFS (First Come First Serve) Scheduling Algorithm
Non-preemptive scheduling where processes are executed in the order they arrive.
"""

def calculate_fcfs(processes):
    """
    Calculate waiting time and turnaround time for FCFS scheduling.
    
    Args:
        processes: List of dictionaries containing process information
                   Each process should have: 'pid', 'burst_time', 'arrival_time'
    
    Returns:
        List of processes with calculated waiting_time and turnaround_time
    """
    # Sort processes by arrival time (FCFS principle)
    processes.sort(key=lambda x: x['arrival_time'])
    
    n = len(processes)
    current_time = 0
    
    for i in range(n):
        # If CPU is idle, jump to next process arrival
        if current_time < processes[i]['arrival_time']:
            current_time = processes[i]['arrival_time']
        
        # Waiting time = current time - arrival time
        processes[i]['waiting_time'] = current_time - processes[i]['arrival_time']
        
        # Turnaround time = waiting time + burst time
        processes[i]['turnaround_time'] = processes[i]['waiting_time'] + processes[i]['burst_time']
        
        # Update current time (CPU finishes this process)
        current_time += processes[i]['burst_time']
    
    return processes


def display_gantt_chart(processes):
    """
    Display a visual Gantt chart showing process execution timeline.
    
    Args:
        processes: List of processes sorted by execution order
    """
    print("\n" + "="*80)
    print("Gantt Chart")
    print("="*80 + "\n")
    
    # Calculate execution timeline
    timeline = []
    current_time = 0
    
    for process in processes:
        # Handle idle time if CPU was waiting
        if current_time < process['arrival_time']:
            timeline.append({
                'label': 'IDLE',
                'start': current_time,
                'end': process['arrival_time'],
                'duration': process['arrival_time'] - current_time
            })
            current_time = process['arrival_time']
        
        # Add process execution
        timeline.append({
            'label': f"P{process['pid']}",
            'start': current_time,
            'end': current_time + process['burst_time'],
            'duration': process['burst_time']
        })
        current_time += process['burst_time']
    
    # Draw the chart
    # Top border
    print("┌", end="")
    for segment in timeline:
        width = min(segment['duration'] * 2, 20)  # Limit max width for readability
        if width < 2:
            width = 2
        print("─" * width + "┬", end="")
    print("┐")
    
    # Process labels
    print("│", end="")
    for segment in timeline:
        label = segment['label']
        width = min(segment['duration'] * 2, 20)
        if width < 2:
            width = 2
        padding = (width - len(label)) // 2
        print(" " * padding + label + " " * (width - padding - len(label)) + "│", end="")
    print()
    
    # Bottom border
    print("└", end="")
    for segment in timeline:
        width = min(segment['duration'] * 2, 20)
        if width < 2:
            width = 2
        print("─" * width + "┴", end="")
    print("┘")
    
    # Time markers
    print("0", end="")
    for segment in timeline:
        width = min(segment['duration'] * 2, 20)
        if width < 2:
            width = 2
        time_str = str(segment['end'])
        # Adjust spacing based on width
        spaces = width - len(time_str) + 1
        print(" " * spaces + time_str, end="")
    print("\n")
    
    # Execution sequence
    execution_order = " → ".join([seg['label'] for seg in timeline])
    print(f"Execution Sequence: {execution_order}\n")


def display_fcfs_results(processes):
    """
    Display FCFS scheduling results in a formatted table.
    
    Args:
        processes: List of processes with calculated metrics
    """
    print("\n" + "="*80)
    print("FCFS (First Come First Serve) Scheduling Results")
    print("="*80)
    
    # Display Gantt Chart first
    display_gantt_chart(processes)
    
    # Table header
    print("="*80)
    print("Process Details")
    print("="*80)
    print(f"{'Process':<10} {'Arrival':<12} {'Burst':<12} {'Waiting':<12} {'Turnaround':<12}")
    print(f"{'ID':<10} {'Time':<12} {'Time':<12} {'Time':<12} {'Time':<12}")
    print("-"*80)
    
    # Process details
    total_waiting = 0
    total_turnaround = 0
    
    for process in processes:
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


def get_fcfs_input():
    """
    Get user input for FCFS scheduling.
    
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


def run_fcfs():
    """
    Main function to run FCFS scheduling algorithm.
    """
    print("\n" + "="*80)
    print("FCFS (First Come First Serve) Scheduling")
    print("="*80 + "\n")
    
    processes = get_fcfs_input()
    
    if processes is None:
        print("FCFS scheduling aborted due to invalid input.\n")
        return
    
    # Calculate scheduling metrics
    processes = calculate_fcfs(processes)
    
    # Display results
    display_fcfs_results(processes)


# For testing this module independently
if __name__ == "__main__":
    run_fcfs()
