from collections import deque 

time_count =0
ready_queue=deque()
IO_queue=deque()
count=0
Gantt_chart=[]
Arrival_IO=[]
Time_sequence=[]


def IO_enqueue(process_number,time_initial):
    if(time_initial==time_count-4):
        ready_queue.append(process_number)
    else:
       IO_queue.append(process_number)
    return process_number
    

# Allocating the resources present within the system

def time_step(Process_number, time_q, Burst, IO,IO_Burst, count, n):
    global time_count
    global ready_queue
    global Gantt_chart
    global Time_sequence

    if IO[Process_number]== 1 and IO_Burst[Process_number]==0:
        time_q = 2
        IO[Process_number]=0
        Arrival_IO[Process_number]=time_count
        IO_queue.append(Process_number)
      #   print(f"Elements dequeued from the queue for IO:{Process_number}")
        Gantt_chart.append(Process_number) #To store the number of process 
        Time_sequence.append(time_count)  #To store the time at which that particular process leaves.
        ready_queue.popleft()
        Process_number = ready_queue[0]
      #   print(f"Timer is(IO):{time_count}")
        # Assuming negligible time to switch between one process to another for IO.
        
    elif (Burst[Process_number] == 0 or time_q == 0) and len(ready_queue)!=0:
        time_q = 2
      #   print("\nElements dequeued from the queue")
        Gantt_chart.append(Process_number)
        Time_sequence.append(time_count)
        
        ready_queue.popleft()
        if(Burst[Process_number]==0):
           count+=1
           if(len(ready_queue)!=0):
               Process_number=ready_queue[0]
         #   print(f"The new process number is {Process_number}\n")
           
        else:
           ready_queue.append(Process_number)
         #   print(ready_queue)
           Process_number=ready_queue[0]
         #   print(f"The new process number is :{Process_number}\n")

    elif Burst[Process_number] > 0 and time_q > 0:
       
        Burst[Process_number] = Burst[Process_number] - 1
        IO_Burst[Process_number]=IO_Burst[Process_number]-1
        time_q = time_q - 1
        time_count += 1  # Increment time_count
        print(f"Timer is(Update):{time_count}\n ")
        print(ready_queue)
        print(IO_queue)

    return Process_number,Burst, time_q,IO_Burst, count



if __name__ == "__main__":
   # Allocating the resources present within the system
   n=int(input("Enter the number of processes"))
   print(f"The number of processes to be simulated are :{n}\n ")
   Burst=[]
   IO=[]
   IO_Burst=[]
   for i in range(n):
      Burst.append(int(input(f"Enter the burst for {i}th process\n")))
      answer=(input("Does this process have IO request? (Y/N)\n"))
      if(answer=="Y"):
         IO_percent_after=int(input("Enter the %time after which IO would be required\n"))
         time_instance=int((IO_percent_after/100)*Burst[i])
         if(time_instance>0):
            IO.append(1)
            IO_Burst.append(time_instance)
         else:
            IO.append(0)
            IO_Burst.append(0)
            
      else:
         IO.append(0)
         IO_Burst.append(0)
         
      ready_queue.append(i)
      Arrival_IO.append(0)
   Process_n=0
   Time_q=2
   while(count!=n or len(IO_queue)>0):
      Process_n,Burst,Time_q,IO_Burst,count=time_step(Process_n,Time_q,Burst,IO,IO_Burst,count,n)
      if(len(IO_queue)>0):
         local_process_no=IO_queue.popleft()
         local_process_no=IO_enqueue(local_process_no,Arrival_IO[local_process_no])
         
   # print(Gantt_chart)
   # print(Time_sequence)
   
   Gantt_chart_overall=[]
   for i in range(len(Gantt_chart)):
      element=[]
      if(i==0):
         element.append(0)
         element.append(Time_sequence[i])
         element.append(Gantt_chart[i])
      else:
         element.append(Time_sequence[i-1])
         element.append(Time_sequence[i])
         element.append(Gantt_chart[i])
      Gantt_chart_overall.append(element)
   
   print (Gantt_chart_overall)