import time 
from sys import getsizeof
import matplotlib.pyplot as plt
sizes = range(10000, 600000, 100000)
l1 = []

for n in sizes:
    data = 'x' * n
    b = data 
    start = time.time()
    max_mem = 0
    min_mem = 0
    while b:
        if n== len(b):
            max_mem = getsizeof(b) - getsizeof('')
        elif len(b) == 1:
            min_mem = getsizeof(b) - getsizeof('')
        b = b[1:]
    stop = time.time()
    print(f'valor {n} {stop - start} - max mem {max_mem/10**3} KB - Min mem {min_mem} B')
    l1.append(stop-start)
l2 = []
for n in sizes:
    data = b'x' * n
    b = memoryview(data)
    start = time.time()
    max_mem = 0
    min_mem = 0
    while b:
        if n == len(b):
            max_mem = getsizeof(b) - getsizeof('')
        elif len(b) == 1:
            min_mem = getsizeof(b) - getsizeof('')
        b = b[1:]
    stop = time.time()
    print(f'valor {n} {stop - start} - max mem {max_mem/10**3} KB - Min mem {min_mem} B')
    l2.append(stop-start)

plt.plot(l1, 'x-', label='whithout Memoryview')    
plt.plot(l2, 'o--', label='whith Memoryview')    
plt.xlabel('Size of Bytearray')
plt.ylabel('Time (s)')
plt.legend()
plt.show()