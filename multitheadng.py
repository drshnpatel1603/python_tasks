from threading import Thread
import concurrent.futures
import time
import multiprocessing
import os

def func1(l):
    # pid = os.getpid()
    for i in range(l):
        print(f"func1 {i}")
        # print("pid :",pid)

def func2(l):
    # pid = os.getpid()
    for i in range(l):
        print(f"func2 {i}")
        # print("pid :",pid)

""" Using Theading """
# time1 = time.perf_counter()
# t1 = Thread(target=func1,args=(5000000,))
# t2 = Thread(target=func2,args=(5000000,))
# t1.start()
# t2.start()
# t2.join()
# func1()
# func2()
# print(f"Time is {time.perf_counter() - time1}")


""" Using concurrent future """
# pool = concurrent.futures.ThreadPoolExecutor()
# time1 = time.perf_counter()
# pool.submit(func1)
# pool.submit(func2)
# pool.shutdown(wait=True)
# print(f"Time is {time.perf_counter() - time1}")


""" using multiprocessing """
# p1 = multiprocessing.Process(target=func1)
# p2 = multiprocessing.Process(target=func2)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()

""" using multiproceesing pool """
# l = (5000000,)
# p = multiprocessing.Pool(6)
# p.map(func1,l)
# p.map(func2,l)
# print(f"Time is {time.perf_counter() - time1}")

dict = {"drshn" : [{"python" : (10,20)}]}
dict["drshn"].append({"java" : (20,25)})

value = dict.get("drshn")

print(value)


print(dict)

