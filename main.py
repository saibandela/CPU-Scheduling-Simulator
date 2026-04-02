"""
CPU Scheduling Simulator
Main program with menu interface to select scheduling algorithms.

Supported Algorithms:
- FCFS (First Come First Serve)
- SJF (Shortest Job First - Non-preemptive)
"""

import fcfs
import sjf
import copy


def display_menu():
    """
    Display the main menu for algorithm selection.
    """
    print("\n" + "="*80)
    print(" "*25 + "CPU SCHEDULING SIMULATOR")
    print("="*80)
    print("\nSelect a Scheduling Algorithm:")
    print("  1. FCFS (First Come First Serve)")
    print("  2. SJF (Shortest Job First - Non-preemptive)")
    print("  3. Compare Both Algorithms")
    print("  4. Exit")
    print("-"*80)


def get_process_input():
    """
    Get user input for processes (used in comparison mode).
    
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


def compare_algorithms():
    """
    Compare FCFS and SJF algorithms side by side.
    """
    print("\n" + "="*80)
    print("ALGORITHM COMPARISON MODE")
    print("="*80 + "\n")
    
    # Get input once
    processes = get_process_input()
    
    if processes is None:
        print("Comparison aborted due to invalid input.\n")
        return
    
    # Make deep copies for each algorithm
    fcfs_processes = copy.deepcopy(processes)
    sjf_processes = copy.deepcopy(processes)
    
    # Calculate FCFS
    fcfs_result = fcfs.calculate_fcfs(fcfs_processes)
    
    # Calculate SJF
    sjf_result, sjf_timeline = sjf.calculate_sjf(sjf_processes)
    
    # Display FCFS results
    fcfs.display_fcfs_results(fcfs_result)
    
    # Display SJF results
    sjf.display_sjf_results(sjf_result, sjf_timeline)
    
    # Calculate and display comparison summary
    fcfs_avg_wt = sum(p['waiting_time'] for p in fcfs_result) / len(fcfs_result)
    fcfs_avg_tat = sum(p['turnaround_time'] for p in fcfs_result) / len(fcfs_result)
    
    sjf_avg_wt = sum(p['waiting_time'] for p in sjf_result) / len(sjf_result)
    sjf_avg_tat = sum(p['turnaround_time'] for p in sjf_result) / len(sjf_result)
    
    print("="*80)
    print("COMPARISON SUMMARY")
    print("="*80)
    print(f"{'Metric':<30} {'FCFS':<20} {'SJF':<20} {'Winner':<10}")
    print("-"*80)
    
    wt_winner = "SJF" if sjf_avg_wt < fcfs_avg_wt else "FCFS" if fcfs_avg_wt < sjf_avg_wt else "TIE"
    tat_winner = "SJF" if sjf_avg_tat < fcfs_avg_tat else "FCFS" if fcfs_avg_tat < sjf_avg_tat else "TIE"
    
    print(f"{'Average Waiting Time':<30} {fcfs_avg_wt:<20.2f} {sjf_avg_wt:<20.2f} {wt_winner:<10}")
    print(f"{'Average Turnaround Time':<30} {fcfs_avg_tat:<20.2f} {sjf_avg_tat:<20.2f} {tat_winner:<10}")
    print("="*80)
    
    # Performance improvement
    if sjf_avg_wt < fcfs_avg_wt:
        improvement = ((fcfs_avg_wt - sjf_avg_wt) / fcfs_avg_wt) * 100
        print(f"\n✅ SJF reduces average waiting time by {improvement:.2f}%")
    elif fcfs_avg_wt < sjf_avg_wt:
        improvement = ((sjf_avg_wt - fcfs_avg_wt) / sjf_avg_wt) * 100
        print(f"\n✅ FCFS reduces average waiting time by {improvement:.2f}%")
    else:
        print("\n⚖️  Both algorithms perform equally for this process set")
    
    print("="*80 + "\n")


def main():
    """
    Main function to run the CPU scheduling simulator.
    """
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                # Run FCFS algorithm
                fcfs.run_fcfs()
                input("\nPress Enter to continue...")
                
            elif choice == '2':
                # Run SJF algorithm
                sjf.run_sjf()
                input("\nPress Enter to continue...")
                
            elif choice == '3':
                # Compare both algorithms
                compare_algorithms()
                input("\nPress Enter to continue...")
                
            elif choice == '4':
                # Exit program
                print("\n" + "="*80)
                print("Thank you for using CPU Scheduling Simulator!")
                print("="*80 + "\n")
                break
                
            else:
                print("\n❌ Invalid choice! Please select 1, 2, 3, or 4.")
                input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
