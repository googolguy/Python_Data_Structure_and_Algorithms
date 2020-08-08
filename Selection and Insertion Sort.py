# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:13:02 2020

Description: Selection and Insertion Sort Techniques.
"""

#Note: Python computes 10^7 steps in a second on an average

####################### Selection Sort ######################################
'''
TECHNIQUE:
    1) Select the next element in sorted order.
    2) Move it into its correct place in the final sorted list.

Note: In order to avoid using a second list.
    1) Swap minimum element with value in first position.
    2) Swap second minimum element to second position.
'''

def SelectionSort(l):
    # Scan slices l[0:len(l)], l[1,len(l)],....
    for start in range(len(l)):
        # Find minimum value in the slice.
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                minpos = i
        # Switching the values i.e. making minimum value to move to start of slice
        l[start], l[minpos] = l[minpos], l[start]
    return l

listinput = list(range(1000, 0,-1))
print("Selection Sort Input:",listinput)
print("Selection Sort Output:",SelectionSort(listinput))

'''
ANALYSIS:
    1) Finding minimum in unsorted sequence of length k requires one scan, k steps.
    2) In each iteration, sequence to be scanned reduce by 1.
    
    T(n) = n + (n-1) + (n-2) + ...... 1
         = n(n+1)/2
         = n^2/2 + n/2
Since Big O takes the highest term in expression.

    T(n) = O(n^2)
'''



####################### Insertion Sort ######################################
'''
TECHNIQUE:
    1) Move first element to new stack
    2) Move second element below first if it is less than first, or move it 
       above first element if it is greater than first.
    3) Insert third element into the correct position with respect to first
       two elements.
Note: Do this for each subsequent element, Insert into correct position in 
      new sorted stack.
'''

def InserionSort(seq):
    for sliceEnd in range(len(seq)):
        # Build longer and longer sorted slices.
        # In each iteration seq[0:sliceEnd] is already sorted.
        # Move first element after sorted slice left till it is in correct place.
        
        pos = sliceEnd
        while pos>0 and seq[pos] < seq[pos-1]:
            seq[pos], seq[pos-1] = seq[pos-1], seq[pos]
    return seq

listinput = list(range(1000, 0,-2))
print("Insertion Sort Input:",listinput)
print("Insertion Sort Output:",SelectionSort(listinput))

'''
ANALYSIS:
    1) Inserting a new value in sorted sequence of length k require upto k steps in worst case.
    2) In each iteration, sorted sequence in which we have to insert is increased by 1.
    
    T(n) = 1+2+3+---------(n-1)
         = n(n-1)/2
         = n^2/2 -n/2
         
    T(n) = O(n)
'''

'''
Recursive Insertion Sort:
    Base Case:- if length of list is 1 or 0, return the list
    Insuctive Case:- Inductively sort slice l[0:len(l)-1]
                     Insert l[len(l)-1] into this sorted slice.

Note: for longer range recursion will fail with reason- Maximum recursion depth
      exceeded in comparison.

Python has 998 recursion limit by default, although we can set the recursion 
limit in python as per our requirement.

import sys
sys.setrecursionlimit(10000)

Above code will set resursion limit to 10000 but python always needs the upper
limit called recursion limit, which is 10000 in this case. As it wants to make
sure that loop is terminated if in case user has done any mistake. like infinite
running while loop.
    
'''

'''
SUMMARY:
    1) Selection sort and Insertion sort are both O(n^2)
    2) O(n^2) sorting is infeasable for n over 5000
    3) Among O(n^2) sorts, Insertion sort is usually better than selection
       sort as if list is slightly sorted then less number of steps are executed
       in insertion sort.
'''