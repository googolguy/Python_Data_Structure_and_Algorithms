# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:12:19 2020

Description: Quick Sort
"""

'''
Alternative method of using divide and conquer method of merge sort without the
need of merging.

1) Suppose the median value of A is m.
2) Move all the values <= m to left half of A
    a) Right half has values > m.
    b) This shifting can be done in place in time O(n)
3) Recursively sort left and right halves.
4) A is now sorted, no need to merge.

How do we find a median?
So, the approach we follow is, pick up some value in A and use it as a pivot.
we split A as per this pivot.
'''

'''
QUICK SORT:
    1) Choose a pivot element, typically the first value in the array.
    2) Partition A into lower and upper part with respect to pivot.
    3) Move pivot between lower and upper partitions.
    4) Recursively sort the two partitions.
'''
def quicksort(A,l,r): # Sort A[l:r]
    if r-l <= 1: # Base Case
        return
    # Partition w.r.t pivot A[l]
    yellow = l+1
    for green in range(l+1,r):
        if A[green] <= A[l]:
            A[green],A[yellow] = A[yellow],A[green]
            yellow += 1
    # Move pivot into place
    A[l],A[yellow-1] = A[yellow-1],A[l]
    
    quicksort(A, l, yellow-1) # Recursive Calls
    quicksort(A, yellow, r)
    return A

lin = list(range(100,0,-2))
print("Quick Sort Output:",quicksort(lin, 0, len(lin)))

'''
ANALYSIS:
    Worst Case:
        1) Pivot is either max or min.
            a) One partition is empty.
            b) Other has size n-1.
            c) T(n) = O(n^2)
        2) Already sorted array is worst case input.
    
    But...
        3) Average case is O(nlog(n))
        4) Sorting is a rare example where average case can be computed.
'''

'''
Quick Sort is fast in highly randomize list, while it is slow on already 
sorted lists.
'''
