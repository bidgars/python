from multiprocessing import process
from multiprocessing.context import Process
import os
import time

# import parallelTestModule

# if __name__ == '__main__':
#     extractor = parallelTestModule.ParallelExtractor()
#     extractor.runInParallel(numProcesses=2, numThreads=4)

# Define dummy functions to perform task
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


processes = []
num_processors = os.cpu_count()
if __name__ == "__main__":
    print(num_processors)

# Create processes now from only one main process
for i in range(num_processors):
    if __name__ == "__main__":
        p = Process(target=square_numbers)
        processes.append(p)

# Start execution
for p in processes:
    p.start()

# Wait ofr processes to finish and block main thead untill all processes are finished
for p in processes:
    p.join()

print("End Main")
