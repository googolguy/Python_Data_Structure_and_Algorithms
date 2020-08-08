# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:33:23 2020

@author: aditipc

Description: Algorithm for Greatest Common Divisor of 2 Positive Integers.
"""

"""
Points to Remember regarding gcd(m,n):
1. We have to find largest k such that k divides m and k divides n as well.
2. There is always atleast one common divisor for every m and n
"""

# Basic Code

def gcd(m,n):
    cf = []
    mf = []
    nf = []
    
    for i in range(1,m+1):
        if m%i == 0:
            mf.append(i)
    for j in range(1,n+1):
        if n%j == 0:
            nf.append(j)
    for item in mf:
        if item in nf:
            cf.append(item)
    return cf[-1]

m,n = input("Enter the two numbers whose GCD has to be calculated: ").split(" ")
m = int(m)
n = int(n)
print(gcd(m,n))

"""
The above coded basic algorithm can be refined much further.
"""

# Refined Code

def gcd(m,n):
    for i in range(min(m,n), 0, -1):
        if (m%i==0) and (n%i==0):
            return i

m,n = input("Enter the two numbers whose GCD has to be calculated: ").split(" ")
m = int(m)
n = int(n)
print(gcd(m,n))

"""
Although the above mentioned code looks much simpler but it still take time
proportional to value of m and n
"""

"""
***** EUCLID ALGORITHM FOR GREATEST COMMON FACTOR *****

Suppose d divides both m and n, and m>n
Then m = ad and n = bd
So m-n = ad-bd = (a-b)d
Therefore d divides m-n as well
So gcd(m,n) = gcd(n,m-n)

Algorithm:
    1. Consider gcd(m,n) with m>n
    2. If n divides m, return n
    3. Otherwise compute gcd(n,m-n) and return that value
"""

# Euclid Algorithm Code - version 1

def gcd(m,n):
    if m<n: #Assume m >= n
        (m,n) = (n,m)
    
    if m%n == 0:
        return n
    else:
        diff = m-n
        #Since diff > n? Possible?
        return (gcd(max(n,diff), min(n,diff))) #Recursion is used here

m,n = input("Enter the two numbers whose GCD has to be calculated: ").split(" ")
m = int(m)
n = int(n)
print(gcd(m,n))

# Euclid Algorithm Code - version 2 using while loop

def gcd(m,n):
    if m<n: #Assume m >= n
        (m,n) = (n,m)
    
    while (m%n)!=0:
        diff = m-n
        (m,n) = (max(n,diff), min(n,diff))
    return n

m,n = input("Enter the two numbers whose GCD has to be calculated: ").split(" ")
m = int(m)
n = int(n)
print(gcd(m,n))

"""
This approach still takes time proportional to m and n
eg. gcd(101,2) will be computed in 50+ iterations
"""

"""
BETTER APPROACH:
1. Suppose n doesn't divide m
2. Then m = qn+r, where r is the remainder and q is the quotient when we 
   divide m by n.
3. Assume d divides both m and n
4. Then m=ad, n=bd
5. Putting these values of m and n in equation in step 2
   ad = q(bd) + r
6. Arguably as per step 3, d divides r as well. since r is also part of m
   r = cd 
"""

"""
***** IMPROVED EUCLID ALGORITHM *****
    1. Consider gcd(m,n) with m>n
    2. if n divides m, return n
    3. otherwise, let r = m%n
    4. Return gcd(n,r), r here will be definately less than n
"""

# Improved Euclid Algorithm Code - version 1

def gcd(m,n):
    if m<n: #Assume m >= n
        (m,n) = (n,m)
    if m%n == 0:
        return n
    else:
        return gcd(n,m%n) #m%n < n, always!

m,n = input("Enter the two numbers whose GCD has to be calculated: ").split(" ")
m = int(m)
n = int(n)
print(gcd(m,n))


# Improved Euclid Algorithm Code - version 2 using while loop

def gcd(m,n):
    if m<n: #Assume m >= n
        (m,n) = (n,m)
    while (m%n)!=0:
        (m,n) = (n,m%n)
    return n

m,n = input("Enter the two numbers whose GCD has to be calculated: ").split(" ")
m = int(m)
n = int(n)
print(gcd(m,n))

"""
EFFICIENCY:
    1. Can show that Naive algorithm takes time proportional to number of digits
       in m.
    2. If m is billion(10^9) then naive algorithm takes billion of steps,
       whereas improved algorithm takes tens of steps.
"""
