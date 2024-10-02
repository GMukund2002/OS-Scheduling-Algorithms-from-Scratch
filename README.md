# Operating System Project
This repository contains code for the project done for implementing OS scheduling algorithms from scratch, particularly: First Come First Serve (FCFS) and Round Robin (RR).

## First Come First Serve (FCFS) Algorithm
The FCFS algorithm is implemented in the fcfs_with_io.py file. It simulates the scheduling of processes using the FCFS scheduling policy. It takes into consideration the arrival time, burst time, I/O requests, and I/O durations to calculate various metrics. The output includes a __Gantt chart__ and the following metrics for each process:

- Arrival Time
- Burst Time
- Exit Time (Completion Time)
- Turnaround Time
- Waiting Time
- Average Waiting Time

## Round Robin Algorithm
The Round Robin algorithm is implemented in the backend.py file. It simulates the scheduling of processes using the Round Robin scheduling policy. It uses a time quantum to switch between processes and handles I/O requests efficiently. The output includes a __Gantt chart__.
