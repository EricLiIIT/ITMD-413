'''
Name: Eric Li
ID: A20419312
Homework 6 - Sorting and Searching

Question 2 - There are various sorting algorithms available to sort data of 
different sizes. Three of these algorithms are Bubble sort, Shell sort, and 
Quicksort. Write a program to generate random integer numbers of multiple 
sizes; 10000, 30000, 50000, 70000, and 90000, and find out which of these 
sorting algorithms perform the fastest sorting technique. You can write the 
sorting program yourself or use an existing sorting programs that you can find 
on the cloud and modify them to fit your need. Provide data to proof and 
support your findings by plotting a graph showing the time each takes to sort 
data of various sizes. What can you conclude from your data visualization 
chart? 


This program tests the sorting efficacy of different sorting methods (Bubble,
Shell, and Quicksort) and illustratively represents the results.
'''
import time
import random
#import numpy as np
import matplotlib.pyplot as plt

# print(test_list) is intentionally commented out -- for debugging purposes

# =============== Bubble Sort Algorithm =============== # 
# From: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(test_list): # Bubble Sort Algorithm
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
    
# =============== Shell Sort Algorithm =============== # 
# By Mohit Kumra
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot. 

# From https://www.geeksforgeeks.org/python-program-for-shellsort/
def shell_sort(test_list): # Shell Sort Algorithm
    # Start with a big gap, then reduce the gap 
    n = len(test_list) 
    gap = n//2
   
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 

    while gap > 0: 
        gap = int(gap)
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = test_list[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while j >= gap and test_list[j-gap] >temp: 
                test_list[j] = test_list[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            test_list[j] = temp 
        gap /= 2


# =============== Quick Sort Algorithm =============== # 
# By Mohit Kumra
def partition(test_list, low, high): 
    i = (low-1)         # index of smaller element 
    pivot = test_list[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if test_list[j] <= pivot: 
  
            # increment index of smaller element 
            i = i+1
            test_list[i], test_list[j] = test_list[j], test_list[i] 
  
    test_list[i+1], test_list[high] = test_list[high], test_list[i+1] 
    return (i+1) 
  
# The main function that implements QuickSort 
# test_list[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
def quick_sort(test_list, low, high): 
    if len(test_list) == 1: 
        return test_list 
    if low < high: 
  
        # pi is partitioning index, test_list[p] is now 
        # at right place 
        pi = partition(test_list, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(test_list, low, pi-1) 
        quick_sort(test_list, pi+1, high) 
  
# =============================================================================
# # Driver code to test above 
# test_list = [10, 7, 8, 9, 1, 5] 
# n = len(test_list) 
# quickSort(test_list, 0, n-1) 
# print("Sorted array is:") 
# for i in range(n): 
#     print("%d" % test_list[i])
# =============================================================================
    
# =============== List Creation =============== # 
def tenK():
    test_list = []
    for i in range(0, 10001): # Loop to create list of 10,000 values 
        a = random.randint(1,10000) # 1 and 10k are included
        test_list.append(a)
    #print(test_list)
    return test_list

def thirtyK():
    test_list = []
    for i in range(0, 30001): # Loop to create list of 30,000 values
        a = random.randint(1,30000) 
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

# =============== Bubble Sort Run =============== # 
def bubble_sort_exe():
    print("Sort with Bubble Sort Algorithm ->")
    print("Sorting 10k elements...")
    st1 = time.time() # Starts timer
    bubble_sort(tenK())
    BSend1 = format((time.time()-st1), '.2f')
    print("Time to sort 10k elements: ", BSend1, "seconds") # Stops timer
    
    print("Sorting 30k elements...")
    st2 = time.time() 
    bubble_sort(thirtyK())
    BSend2 = format((time.time()-st2), '.2f')
    print("Time to sort for 30k elements: ", BSend2, "seconds")
    
    print("Sorting 50k elements...")
    st3 = time.time() 
    bubble_sort(fiftyK())
    BSend3 = format((time.time()-st3), '.2f')
    print("Time to sort for 50k elements: ", BSend3, "seconds")
    
    print("Sorting 70k elements...")
    st4 = time.time() 
    bubble_sort(seventyK())
    BSend4 = format((time.time()-st4), '.2f')
    print("Time to sort for 70k elements: ", BSend4, "seconds")
    
    print("Sorting 90k elements...")
    st5 = time.time() 
    bubble_sort(ninetyK())
    BSend5 = format((time.time()-st5), '.2f')
    print("Time to sort for 90k elements: ", BSend5, "seconds")
    
    bubble_sort_time = [BSend1, BSend2, BSend3, BSend4, BSend5]
    return bubble_sort_time

# =============== Shell Sort Run =============== # 
def shell_sort_exe():
    print("Sort with Shell Sort Algorithm")
    print("Sorting 10k elements...")
    st1 = time.time() 
    shell_sort(tenK())
    ss_end1 = format((time.time()-st1), '.2f')
    print("Time to sort 10k elements: ", ss_end1, "seconds")

    print("Sorting 30k elements...")
    st2 = time.time() 
    shell_sort(thirtyK())
    ss_end2 = format((time.time()-st2), '.2f')
    print("Time to sort for 30k elements: ", ss_end2, "seconds")
   
    print("Sorting 50k elements...")
    st3 = time.time() 
    shell_sort(fiftyK())
    ss_end3 = format((time.time()-st3), '.2f')
    print("Time to sort for 50k elements: ", ss_end3, "seconds")

    print("Sorting 70k elements...")
    st4 = time.time() 
    shell_sort(seventyK())
    ss_end4 = format((time.time()-st4), '.2f')
    print("Time to sort for 70k elements: ", ss_end4, "seconds")

    print("Sorting 90k elements...")
    st5 = time.time() 
    shell_sort(ninetyK())
    ss_end5 = format((time.time()-st5), '.2f')
    print("Time to sort for 90k elements: ", ss_end5, "seconds")    
    
    shell_sort_time = [ss_end1, ss_end2, ss_end3, ss_end4, ss_end5]
    return shell_sort_time
    
# =============== Quick Sort Run =============== # 
def quick_sort_exe():
    print("Sort with Quick Sort Algorithm")
    print("Sorting 10k elements...")
    st1 = time.time()
    quick_sort(tenK(), 0, len(tenK())-1)
    qs_end1 = format((time.time()-st1), '.2f')
    print("Time to sort 10k elements: ", qs_end1, "seconds")

    print("Sorting 30k elements...")
    st2 = time.time() 
    quick_sort(thirtyK(), 0, len(thirtyK())-1)
    qs_end2 = format((time.time()-st2), '.2f')
    print("Time to sort for 30k elements: ", qs_end2, "seconds")
    
    print("Sorting 50k elements...")
    st3 = time.time() 
    quick_sort(fiftyK(), 0, len(fiftyK())-1)
    qs_end3 = format((time.time()-st3), '.2f')
    print("Time to sort for 50k elements: ", qs_end3, "seconds")

    print("Sorting 70k elements...")
    st4 = time.time() 
    quick_sort(seventyK(), 0, len(seventyK())-1)
    qs_end4 = format((time.time()-st4), '.2f')
    print("Time to sort for 70k elements: ", qs_end4, "seconds")
    
    print("Sorting 90k elements...")
    st5 = time.time() 
    quick_sort(ninetyK(), 0, len(ninetyK())-1)
    qs_end5 = format((time.time()-st5), '.2f')
    print("Time to sort for 90k elements: ", qs_end5, "seconds")
    
    quick_sort_time = [qs_end1, qs_end2, qs_end3, qs_end4, qs_end5]
    return quick_sort_time

# =============== Graphing =============== # 
elem_size = ['10k', '30k', '50k', '70k', '80k']

bs_time = bubble_sort_exe()
bs_bar = plt.bar(elem_size, bs_time)
plt.title("Bubble Sorting Times")
plt.xlabel("List Size")
plt.ylabel("Time in Seconds")
plt.show()

ss_time = shell_sort_exe()
ss_bar = plt.bar(elem_size, ss_time)
plt.title("Shell Sort Times")
plt.xlabel("List Size")
plt.ylabel("Time in Seconds")
plt.show()

qs_time = quick_sort_exe()
qs_bar = plt.bar(elem_size, qs_time)
plt.title("Quick Sort Times")
plt.xlabel("List Size")
plt.ylabel("Time in Seconds")
plt.show()

#---Testing---#
# data = [ss_time,
# ss_time,
# qs_time]
# X = np.arange(10, 100, 20)
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(X - 0, data[0], color = 'b', width = 10, align='center')
# ax.bar(X + 10, data[1], color = 'g', width = 10, align='center')
# ax.bar(X + 20, data[2], color = 'r', width = 10, align='center')
# ax.set_title("Comparative Times for Sorting Algorithms")
# ax.set_xlabel("List Size")

#---For Debugging---#
#bubble_sort_exe()
#shell_sort_exe()
#quick_sort_exe()
  
  
