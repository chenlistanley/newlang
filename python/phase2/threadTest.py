import _thread
import time

def print_time(threadname, counter):
    while counter:
        time.sleep(3)
        counter-=1
        print("%s: %s: %s" %(threadname, time.ctime(), counter))

try:
    _thread.start_new_thread(print_time,("thread_1", 4))
    _thread.start_new_thread(print_time,("thread_2", 6))
except:
    print("error: thread start failed")

input()
