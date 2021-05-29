from threading import Thread
import os
import time

# Define dummy functions to perform task
def square_numbers(tno):
    print(tno)
    for i in range(10):
        i * i
        time.sleep(1)


threads = []
num_processors = os.cpu_count()
print(num_processors)

# Create processes now from only one main process
for i in range(num_processors):
    p = Thread(target=square_numbers, args=[i])
    threads.append(p)

# Start execution
for p in threads:
    p.start()

# Wait ofr processes to finish and block main thead untill all processes are finished
for p in threads:
    p.join()

print("End Main")
