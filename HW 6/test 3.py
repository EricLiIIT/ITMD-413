# Python program to illustrate the concept 
# of threading 
from multiprocessing import Process
import os 
import random
  
def task1():  
    #print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 1: {}".format(os.getpid())) 
    print(1)

def bubbleSort(test_list): 
    n = len(test_list) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if test_list[j] > test_list[j+1] : 
                test_list[j], test_list[j+1] = test_list[j+1], test_list[j] 

def task2(): 
    test_list = []
    for i in range(0, 10001): # Loop to create list of 10,000 values 
        a = random.randint(1,10000) # 1 and 10k are included
        test_list.append(a)
    #print(test_list)
    #print("Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 2: {}".format(os.getpid())) 
    return test_list
    
    


if __name__ == '__main__': 
  
    # print ID of current process 
    #print("ID of process running main program: {}".format(os.getpid())) 
  
    # print name of main thread 
    #print("Main thread name: {}".format(threading.current_thread().name)) 
  
    # creating threads 
    t1 = Process(target=task1) 
    #t2 = multiprocessing.Process(target=bubbleSort)   
  
    # starting threads 
    #t2.start() 
    t1.start() 
  
    # wait until all threads finish 
    
    t1.join() 
    #t2.join() 
    #print(1)
