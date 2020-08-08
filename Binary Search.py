# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:54:24 2020

Description: Binary Search. 
"""

'''
Binary search algorithm to find v in a seq
1) Compare v with midpoint of seq.
2) if midpoint is v, the value is found.
3) if v < midpoint, search left half of seq. 
4) if v > midpoint, search right half of seq.
'''

def bsearch(seq,v,l,r):
    # Search for v in seq[l:r], seq is sorted
    if (r-l == 0): # Empty Slice case
        return False
    mid = (l-r)//2  # Floor division or Integer division
    if (v == seq[mid]):
        return True
    if (v < seq[mid]):
        return (bsearch(seq,v,l,mid))
    else:
        return (bsearch(seq,v,mid+1,r))

'''
Taking in consideration time complexity of Binary Search in terms of Big O

T(n) = O(logn)

where n is the number of elements on which search is executed.

Unsorted array - Linear Scan, O(n)
Sorted array - Binary Scan, O(logn)
'''
    