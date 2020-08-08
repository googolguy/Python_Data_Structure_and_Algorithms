# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:03:25 2020

Description: Functions.
"""
################# Functions Argument ######################################

'''
In a function, argument value is substituted for name.
eg. power(x,n):
        return(n)

power(3,5) goes to x=3 and n=5

although we can also assign value in any order.
like power(n=5,x=3)
'''

'''
Python also allows some arguments to be left out for default arguments.
eg. int(s) convert String to Integer

int("76") --> 76
int("A5") --> generates an error

Reason: int() function takes two arguments.
int(s,b) where s is string and b is base. b has default value of 10.

eg: int("A5",16) --> 165 (No error)
Calculation: 10*16^1 + 5*16^0 = 165
'''

'''
we can also assign a function to a new name.

def f(a,b,c):
    ....
g = f

Now g is another name for f.

It allows us to pass function as an argument to another function.
'''
################# Recursion Functions ######################################

# Function to find factors of a number
def factors(n):
    factor = []
    for i in range(1, n+1):
        if n%i == 0:
            factor.append(i)
    return factor

# Function to find wheather the number is Prime or not.
def isprime(n):
    return factors(n) == [1,n]

# Function to list all Prime numbers below the input number.
def primeupto(n):
    primelist = []
    for i in range(1,n+1):
        if isprime(i):
            primelist.append(i)
    return primelist

# Function to find prime number equal to input number.
def nprime(n):
    count, i, plist = 1,1,[]
    while (count <= n):
        if isprime(i):
            count += 1
            plist.append(i)
        i += 1
    return plist

number = input("User Input: ")

factor = factors(int(number))
print("Factors:",factor)

prime = isprime(int(number))
print("Prime Status of input number:",prime)

tillprime = primeupto(int(number))
print("Primes below input number:",tillprime)

nprimes = nprime(int(number))
print("First", number, "prime numbers:",nprimes)


################# Other Recursion Examples #################################

''' Factorial of a Number'''
def Factorial(n):
    if n == 0:
        return 1
    else:
        return (n * Factorial(n-1))


''' Multiply two numbers '''
def Multiply(m,n):
    if n == 1:
        return m
    else:
        return (m + Multiply(m,n-1))


''' Length of a list '''
def Length(l):
    if l == []:
        return 0
    else:
        return (1 + Length[1:])

''' Sum of list of Numbers '''
def Sumlist(l):
    if l == []:
        return 0
    else:
        return (l[0] + Sumlist(l[1:]))

