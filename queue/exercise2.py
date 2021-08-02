# Write a program to print binary numbers from 1 to 10 using Queue.
# Use Queue class implemented in main tutorial. Binary sequence should look like,

from queue import Queue

bin_q = Queue()
MAX = 20
target = 1
counter = 0
while bin_q.size() < MAX:
    # so that it only runs in the beginning
    if bin_q.isEmpty():
        bin_q.enqueue(str(target))
    bin_q.enqueue(str(target) + '0')
    # so that i doesnt enqueue the extra digit
    if bin_q.size() < MAX:
        bin_q.enqueue(str(target) + '1')
    
    counter += 1
    target = bin_q.buffer[counter]
    
# 1 10 11 100 101 110 111 1000 1001 1010

# for _ in range(bin_q.size()):
#     print(bin_q.dequeue())
    
# testing answers
# for b in range(1, MAX+1):
#     print(bin(b))
    
    