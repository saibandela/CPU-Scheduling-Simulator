# CPU Scheduling Simulator

A Python-based CPU scheduling simulator that implements fundamental operating system scheduling algorithms. This educational tool helps visualize and understand how different scheduling algorithms work.

## 📋 Features

- **FCFS (First Come First Serve)**: Processes execute in arrival order
- **SJF (Shortest Job First)**: Processes with shortest burst time execute first
- **Visual Gantt Charts**: See process execution timeline graphically
- **Algorithm Comparison**: Run both algorithms on the same input and compare results
- **Arrival Time Support**: Simulate realistic scenarios with different arrival times
- Clean, modular code structure
- Interactive menu-driven interface
- Detailed performance metrics (Waiting Time, Turnaround Time)
- Input validation and error handling
- Shows idle CPU time in Gantt charts

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/cpu-scheduling-simulator.git
cd cpu-scheduling-simulator
```

2. Run the program:
```bash
python main.py
```

## 📖 Usage

### Running the Simulator

```bash
python main.py
```

The program will display a menu where you can select the scheduling algorithm:

```
================================================================================
                         CPU SCHEDULING SIMULATOR
================================================================================

Select a Scheduling Algorithm:
  1. FCFS (First Come First Serve)
  2. SJF (Shortest Job First - Non-preemptive)
  3. Compare Both Algorithms
  4. Exit
--------------------------------------------------------------------------------
```

### Input Format

For each process, you'll need to provide:
- **Burst Time**: Time required by the process to complete execution
- **Arrival Time** (optional): When the process arrives in the ready queue (default: 0)

### Example Usage

#### Example 1: FCFS with Same Arrival Time

**Input:**
```
Number of processes: 3
Process 1:
  Burst Time: 24
  Arrival Time: 0
Process 2:
  Burst Time: 3
  Arrival Time: 0
Process 3:
  Burst Time: 3
  Arrival Time: 0
```

**Output:**
```
================================================================================
FCFS (First Come First Serve) Scheduling Results
================================================================================
Process    Arrival      Burst        Waiting      Turnaround  
ID         Time         Time         Time         Time        
--------------------------------------------------------------------------------
P1         0            24           0            24          
P2         0            3            24           27          
P3         0            3            27           30          
--------------------------------------------------------------------------------

Average Waiting Time: 17.00
Average Turnaround Time: 27.00
================================================================================
```

#### Example 2: SJF with Different Arrival Times

**Input:**
```
Number of processes: 4
Process 1:
  Burst Time: 6
  Arrival Time: 0
Process 2:
  Burst Time: 8
  Arrival Time: 1
Process 3:
  Burst Time: 7
  Arrival Time: 2
Process 4:
  Burst Time: 3
  Arrival Time: 3
```

**Output:**
```
================================================================================
SJF (Shortest Job First) Scheduling Results
================================================================================

Gantt Chart
================================================================================

┌────────┬──────┬──────────┬────────────┐
│   P1   │  P4  │    P3    │     P2     │
└────────┴──────┴──────────┴────────────┘
0        6      9          16           24

Execution Sequence: P1 → P4 → P3 → P2

================================================================================
Process Details
================================================================================
Process    Arrival      Burst        Waiting      Turnaround  
ID         Time         Time         Time         Time        
--------------------------------------------------------------------------------
P1         0            6            0            6           
P2         1            8            15           23          
P3         2            7            7            14          
P4         3            3            3            6           
--------------------------------------------------------------------------------

Average Waiting Time: 6.25
Average Turnaround Time: 12.25
================================================================================
```

#### Example 3: Algorithm Comparison

**Input:**
```
Number of processes: 4
Process 1:
  Burst Time: 6
  Arrival Time: 0
Process 2:
  Burst Time: 8
  Arrival Time: 1
Process 3:
  Burst Time: 7
  Arrival Time: 2
Process 4:
  Burst Time: 3
  Arrival Time: 3
```

**Output:**
```
[Shows both FCFS and SJF results with Gantt charts]

================================================================================
COMPARISON SUMMARY
================================================================================
Metric                         FCFS                 SJF                  Winner    
--------------------------------------------------------------------------------
Average Waiting Time           7.50                 6.25                 SJF       
Average Turnaround Time        13.50                12.25                SJF       
================================================================================

✅ SJF reduces average waiting time by 16.67%
================================================================================
```

## 📊 Understanding the Metrics

- **Burst Time**: CPU time required by a process
- **Arrival Time**: Time when process enters the ready queue
- **Waiting Time**: Time spent waiting in the ready queue
  - Formula: `Waiting Time = Start Time - Arrival Time`
- **Turnaround Time**: Total time from arrival to completion
  - Formula: `Turnaround Time = Waiting Time + Burst Time`
  - Or: `Turnaround Time = Completion Time - Arrival Time`

## 🗂️ Project Structure

```
cpu-scheduling-simulator/
│
├── main.py          # Main program with menu interface
├── fcfs.py          # FCFS scheduling algorithm
├── sjf.py           # SJF scheduling algorithm
└── README.md        # Project documentation
```

## 🔍 Algorithm Details

### FCFS (First Come First Serve)

**Characteristics:**
- Non-preemptive
- Simplest scheduling algorithm
- Processes execute in arrival order
- Can suffer from "Convoy Effect"

**Advantages:**
- Simple to implement
- Fair (no starvation)

**Disadvantages:**
- Poor average waiting time
- Not optimal for interactive systems

### SJF (Shortest Job First)

**Characteristics:**
- Non-preemptive (in this implementation)
- Selects process with shortest burst time
- Optimal for minimizing average waiting time

**Advantages:**
- Minimum average waiting time
- Efficient for batch systems

**Disadvantages:**
- Can cause starvation for long processes
- Requires knowledge of burst time (difficult to predict)

## 🛠️ Running Individual Modules

You can test each algorithm independently:

```bash
# Test FCFS only
python fcfs.py

# Test SJF only
python sjf.py
```

## 🔧 Future Enhancements

Potential improvements for this project:

1. **Additional Algorithms:**
   - Priority Scheduling (preemptive and non-preemptive)
   - Round Robin (RR)
   - Shortest Remaining Time First (SRTF)
   - Multilevel Queue Scheduling

2. **Visualization:**
   - Gantt Chart generation
   - Timeline visualization
   - Graphical comparison of algorithms

3. **Advanced Features:**
   - File input support (CSV/JSON)
   - Export results to file
   - Batch mode for testing multiple scenarios
   - Performance comparison across algorithms

4. **User Interface:**
   - GUI using Tkinter or PyQt
   - Web interface using Flask/Django
   - Command-line arguments support

5. **Statistics:**
   - CPU utilization calculation
   - Throughput metrics
   - Response time tracking

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Your Name - [GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- Operating System concepts by Abraham Silberschatz
- Educational resource for understanding CPU scheduling algorithms
