from collections import deque

time_count = 0
ready_queue = deque()
IO_queue = deque()
count = 0
Gantt_chart = []
Arrival_IO = []
Time_sequence = []

def IO_enqueue(process_number, time_initial):
    if time_initial == time_count - 4:
        ready_queue.append(process_number)
    else:
        IO_queue.append(process_number)
    return process_number

def time_step(process_number, burst, IO, IO_burst, count, n):
    global time_count
    global ready_queue
    global Gantt_chart
    global Time_sequence

    if IO[process_number] == 1 and IO_burst[process_number] == 0:
        IO[process_number] = 0
        Arrival_IO[process_number] = time_count
        IO_queue.append(process_number)
        Gantt_chart.append(process_number)
        Time_sequence.append(time_count)
        ready_queue.popleft()
        if len(ready_queue) > 0:
            process_number = ready_queue[0]

    elif (burst[process_number] == 0) and len(ready_queue) != 0:
        Gantt_chart.append(process_number)
        Time_sequence.append(time_count)
        ready_queue.popleft()
        if burst[process_number] == 0:
            count += 1
            if len(ready_queue) != 0:
                process_number = ready_queue[0]
        else:
            ready_queue.append(process_number)
            process_number = ready_queue[0]

    elif burst[process_number] > 0:
        burst[process_number] -= 1
        IO_burst[process_number] -= 1
        time_count += 1
        print(f"Timer is (Update):{time_count}\n")
        print(ready_queue)
        print(IO_queue)

    return process_number, burst, IO_burst, count

if __name__ == "__main__":
    n = int(input("Enter the number of processes"))
    print(f"The number of processes to be simulated are :{n}\n ")
    burst = []
    IO = []
    IO_burst = []

    for i in range(n):
        burst.append(int(input(f"Enter the burst for {i}th process")))
        answer = input("Does this process have IO request? (Y/N)\n")

        if answer == "Y":
            IO_percent_after = int(input("Enter the %time after which IO would be required\n"))
            time_instance = int((IO_percent_after / 100) * burst[i])

            if time_instance > 0:
                IO.append(1)
                IO_burst.append(time_instance)
            else:
                IO.append(0)
                IO_burst.append(0)
        else:
            IO.append(0)
            IO_burst.append(0)

        ready_queue.append(i)
        Arrival_IO.append(0)

    process_n = 0

    while count != n or len(IO_queue) > 0 or len(ready_queue) > 0:
        process_n, burst, IO_burst, count = time_step(process_n, burst, IO, IO_burst, count, n)

        if len(IO_queue) > 0:
            local_process_no = IO_queue.popleft()
            local_process_no = IO_enqueue(local_process_no, Arrival_IO[local_process_no])
        elif len(ready_queue) > 0:
            process_n = ready_queue[0]

    Gantt_chart_overall = []

    for i in range(len(Gantt_chart)):
        element = []
        if i == 0:
            element.append(0)
            element.append(Time_sequence[i])
            element.append(Gantt_chart[i])
        else:
            element.append(Time_sequence[i-1])
            element.append(Time_sequence[i])
            element.append(Gantt_chart[i])
        Gantt_chart_overall.append(element)

    print(Gantt_chart_overall)

