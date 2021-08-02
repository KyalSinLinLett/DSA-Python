# Design a food ordering system where your python program will run two threads,

#     Place Order: This thread will be placing an order and inserting that into a queue. 
#     This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)

#     Serve Order: This thread will server the order. 
#     All you need to do is pop the order out of the queue and print it. 
#     This thread serves an order every 2 seconds. 
#     Also start this thread 1 second after place order thread is started.

from queue import Queue
import time
import threading

order_queue = Queue()
orders = ['pizza','samosa','pasta','biryani','burger']

# place order function
def place_order(orders_arr):
    for order in orders_arr:
        time.sleep(0.5)
        order_queue.enqueue(order)
        print(f'{order} is added to the order queue...')
        
# serve order
def serve_order():
    while not order_queue.isEmpty():
        time.sleep(2)
        served_order = order_queue.dequeue()
        print(f'{served_order} is served...')
    
th1 = threading.Thread(target=place_order, name="Thread that places order", args=(orders,))
th2 = threading.Thread(target=serve_order, name="Thread that serves order")

ts = time.time()

th1.start()
time.sleep(1)
th2.start()

th1.join()
th2.join()

print('Time taken:', round(time.time() - ts, 5))
print("Order processing is complete...")