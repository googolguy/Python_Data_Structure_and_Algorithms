# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:35:17 2020

Description: Exception Handling.
"""

'''
try:
    # code where errors may occur
except IndexError:
    # what to do with index error
except (NameError, KeyError):
    # Common code to handle multiple errors
except:
    # Catch all exceptions
else:
    # execute if try terminates normally i.e. No errors

'''

'''
Positive use of Exceptions:
'''
# To add a new entry to this dictionary
scores = {'Dhawan': [3,22],'Kohli': [200,3]}

# Conditions: if Batsman 'b' already exists then append the entry to the list
#             else create a fresh entry for batsman 'b'

b = 'Dhawan' # 1st Condition

b = 'Dhoni' # 2nd Condition

# Traditional Approach
if b in scores.keys():
    scores[b].append(100)
else:
    scores[b] = [100]
print("Traditional:",scores)

# Using Exceptions
try:
    scores[b].append(100)
except KeyError:
    scores[b] = [100]
print("Using Exception:",scores)

'''
Summary:
    1) Exception handling allow us to gracefully deal with run-time errors.
    2) Can check type of error and take appropriate action based on type.
    3) Can change coding style to exploit exception handling.
    4) When dealing with files, Input/Output exception handling becomes very important.
'''

'''
Using Exception Handling to deal with strandard Input and Output
'''
while True:
    try:
        userdata = input("Enter a number:")
        usernum = int(userdata)
    except ValueError:
        print("Not a number, Try again")
    else:
        break
print("Userdata:", userdata, "Usernum:", usernum)

