"""
Demo script to showcase the CPU Scheduling Simulator features
This script demonstrates all the functionality programmatically
"""

import fcfs
import sjf
import copy


def demo_fcfs():
    """
    Demonstrate FCFS scheduling with sample data.
    """
    print("\n" + "="*80)
    print("DEMO 1: FCFS with Different Arrival Times")
    print("="*80)
    
    # Sample processes
    processes = [
        {'pid': 1, 'burst_time': 5, 'arrival_time': 0, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 2, 'burst_time': 3, 'arrival_time': 1, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 3, 'burst_time': 8, 'arrival_time': 2, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 4, 'burst_time': 6, 'arrival_time': 3, 'waiting_time': 0, 'turnaround_time': 0},
    ]
    
    print("\nInput Processes:")
    for p in processes:
        print(f"  P{p['pid']}: Burst Time = {p['burst_time']}, Arrival Time = {p['arrival_time']}")
    
    # Calculate FCFS
    result = fcfs.calculate_fcfs(processes)
    
    # Display results
    fcfs.display_fcfs_results(result)


def demo_sjf():
    """
    Demonstrate SJF scheduling with sample data.
    """
    print("\n" + "="*80)
    print("DEMO 2: SJF with Different Arrival Times")
    print("="*80)
    
    # Sample processes
    processes = [
        {'pid': 1, 'burst_time': 6, 'arrival_time': 0, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 2, 'burst_time': 8, 'arrival_time': 1, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 3, 'burst_time': 7, 'arrival_time': 2, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 4, 'burst_time': 3, 'arrival_time': 3, 'waiting_time': 0, 'turnaround_time': 0},
    ]
    
    print("\nInput Processes:")
    for p in processes:
        print(f"  P{p['pid']}: Burst Time = {p['burst_time']}, Arrival Time = {p['arrival_time']}")
    
    # Calculate SJF
    result, timeline = sjf.calculate_sjf(processes)
    
    # Display results
    sjf.display_sjf_results(result, timeline)


def demo_comparison():
    """
    Demonstrate algorithm comparison.
    """
    print("\n" + "="*80)
    print("DEMO 3: Comparing FCFS vs SJF")
    print("="*80)
    
    # Sample processes
    processes = [
        {'pid': 1, 'burst_time': 24, 'arrival_time': 0, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 2, 'burst_time': 3, 'arrival_time': 0, 'waiting_time': 0, 'turnaround_time': 0},
        {'pid': 3, 'burst_time': 3, 'arrival_time': 0, 'waiting_time': 0, 'turnaround_time': 0},
    ]
    
    print("\nInput Processes (Classic Convoy Effect Example):")
    for p in processes:
        print(f"  P{p['pid']}: Burst Time = {p['burst_time']}, Arrival Time = {p['arrival_time']}")
    
    # Make copies
    fcfs_processes = copy.deepcopy(processes)
    sjf_processes = copy.deepcopy(processes)
    
    # Calculate both
    fcfs_result = fcfs.calculate_fcfs(fcfs_processes)
    sjf_result, sjf_timeline = sjf.calculate_sjf(sjf_processes)
    
    # Display results
    fcfs.display_fcfs_results(fcfs_result)
    sjf.display_sjf_results(sjf_result, sjf_timeline)
    
    # Comparison
    fcfs_avg_wt = sum(p['waiting_time'] for p in fcfs_result) / len(fcfs_result)
    sjf_avg_wt = sum(p['waiting_time'] for p in sjf_result) / len(sjf_result)
    
    print("="*80)
    print("COMPARISON SUMMARY")
    print("="*80)
    print(f"FCFS Average Waiting Time: {fcfs_avg_wt:.2f}")
    print(f"SJF Average Waiting Time:  {sjf_avg_wt:.2f}")
    
    if sjf_avg_wt < fcfs_avg_wt:
        improvement = ((fcfs_avg_wt - sjf_avg_wt) / fcfs_avg_wt) * 100
        print(f"\n✅ SJF improves performance by {improvement:.2f}%")
    
    print("="*80 + "\n")


def main():
    """
    Run all demos.
    """
    print("\n" + "="*80)
    print(" "*20 + "CPU SCHEDULING SIMULATOR DEMO")
    print(" "*15 + "Showcasing Gantt Charts & Comparisons")
    print("="*80)
    
    input("\nPress Enter to see FCFS Demo...")
    demo_fcfs()
    
    input("\nPress Enter to see SJF Demo...")
    demo_sjf()
    
    input("\nPress Enter to see Algorithm Comparison...")
    demo_comparison()
    
    print("\n" + "="*80)
    print("✅ Demo Complete! Run 'python main.py' for interactive mode.")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
