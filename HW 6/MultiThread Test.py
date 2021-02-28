import time
import random
import matplotlib.pyplot as plt
import multiprocessing

# Python program for implementation of Bubble Sort
# From: https://www.geeksforgeeks.org/python-program-for-bubble-sort/

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
    #print(test_list)

#test_list = []
# print(test_list) is intentionally commented out -- for debugging purposes

def tenK():
    test_list = []
    for i in range(0, 10001): # Loop to create list of 10,000 values 
        a = random.randint(1,10000) # 1 and 10k are included
        test_list.append(a)
    #print(test_list)
    return test_list

def thirtyK():
    test_list = []
    for i in range(0, 10001): # Loop to create list of 30,000 values
        a = random.randint(1,10000) 
        test_list.append(a)
    #print(test_list)
    return test_list

def fiftyK():
    test_list = []
    for i in range(0, 50001): # Loop to create list of 50,000 values
        a = random.randint(1,50000) 
        test_list.append(a)
    #print(test_list)
    return test_list

def seventyK():
    test_list = []
    for i in range(0, 70001): # Loop to create list of 70,000 values
        a = random.randint(1,70000) 
        test_list.append(a)
    #print(test_list)
    return test_list

def ninetyK():
    test_list = []
    for i in range(0, 90001): # Loop to create list of 90,000 values
        a = random.randint(1,90000) 
        test_list.append(a)
    #print(test_list)
    return test_list

# ===============Bubble Sort=============== # 
def t1():
    print("Sorting 10k elements...")
    st1 = time.time() # Starts timer
    bubbleSort(tenK())
    BSend1 = format((time.time()-st1), '.2f')
    print("Time to sort for 10k elements: ", BSend1, "seconds")
    print(1)
def t2():
    print("Sorting 30k elements...")
    st2 = time.time() 
    bubbleSort(thirtyK())
    BSend2 = format((time.time()-st2), '.2f')
    print("Time to sort for 30k elements: ", BSend2, "seconds")
'''
print("Sorting 50k elements...")
st3 = time.time() 
bubbleSort(fiftyK())
BSend3 = format((time.time()-st3), '.2f')
print("Time to sort for 50k elements: ", BSend3, "seconds")

print("Sorting 70k elements...")
st4 = time.time() 
bubbleSort(seventyK())
BSend4 = format((time.time()-st4), '.2f')
print("Time to sort for 70k elements: ", BSend4, "seconds")

print("Sorting 90k elements...")
st5 = time.time() 
bubbleSort(ninetyK())
BSend5 = format((time.time()-st5), '.2f')
print("Time to sort for 90k elements: ", BSend5, "seconds")
'''
# ===============Multi-Threaded Support=============== #
#if __name__ == "__main__":
p1 = multiprocessing.Process(target=t1)
#p2 = multiprocessing.Process(target=t2)

p1.start()
#p2.start()

p1.join()
#p2.join()

















