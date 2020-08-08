# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 09:40:16 2020

Description: Merge Sort
"""

'''
TECHNIQUE:
    1) Divide array in two equal parts.
    2) Seperately sort left and right half.
    3) Combine the two sorted halves to get the full array sorted.
'''

'''
COMBINING SORTED LIST: Given two sorted lists A and B, combine them into a 
sorted list C
    1) Compare first element of A and B.
    2) Move it into C
    3) Repeat until all elements in A and B are over.
'''

'''
SORTING STEPS:
    1) Sort A[0:n//2] - Left
    2) Sort A[n//2:n] - Right
    3) Merge sorted halces into B[0:n]

Now question arises, how do we sort the halves?
we do it by recursively using ths same strategy of dividing the array until we
are left with only one element in the array.
'''

'''
MERGING SORTED LISTS: Combine two sorted lists A and B into C.
    1) If A is empty, Copy B into C
    2) If B is empty, Copy A into C
    3) Otherwise, compare first element of A and B and move smaller into C
    4) Repeat until all elements in A and B has been moved.
'''
def merge(A,B): # Merge A[0:m], B[0:n]
    C,m,n = [],len(A),len(B)
    i,j = 0,0 # Current Position in A and B
    while i+j < m+n: # i+j is the number of elements merged so far
        if i == m: # Case-1: A is empty
            C.append(B[j])
            j+=1
        elif j == n: # Case-2: B is empty
            C.append(A[i])
            i+=1
        elif A[i] <= B[j]: # Case-3: Head of A is smaller
            C.append(A[i])
            i+=1
        elif A[i] > B[j]: # Case-4: Head of B is samller
            C.append(B[j])
            j+=1
    return C

l1 = list(range(10))
l2 = list(range(10,21))

print("Merged list:",merge(l1,l2))

'''
MERGE SORT: To sort A[0:n] into B[0:n]
    1) If n is 1, nothing to be done.
    2) Otherwise
        a) Sort A[o:n//2] into L (left)
        b) Sort A[n//2:n] into R (right)
        c) Merge L and R into B
'''
def mergesort(A,left,right):
    # Sort the slice A[left:right]
    if right-left <= 1: # Base case
        return A[left:right]
    if right-left > 1: # Recursive Call
        mid = (left+right)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        
        return(merge(L,R))

lin = list(range(100,0,-1))
print("Merge Sort Output:",mergesort(lin,0,len(lin)))
    
'''
ANALYSIS OF MERGE:
    Time taken to merge A of size m and B of size n into C
    In each iteration, we add one element to C
        size of C is m+n
        m+n <= 2*max(m,n)
    Hence O(max(m,n)) = O(n), if m~n
'''

'''
VARIATION OF MERGE:
    1) Union of two sorted lists (discard duplicates)
        while A[i] == B[j], increment j
        Append A[i] to C and increment i
        
    2) Intersection of two sorted lists
        if A[i] < B[i], increment i
        if B[i] < A[i], increment j
        if A[i] == B[j]
            while A[i] == B[j], increment j
            Append A[i] to C and increment i
'''

'''
SHORTCOMINGS:
    1) Merging A and B creates a new array and there is no obvious way to efficiently
       merge in place.
    2) Extra storage can be costly.
    3) Inherently recurssive: Recursive call and return are expensive.
'''