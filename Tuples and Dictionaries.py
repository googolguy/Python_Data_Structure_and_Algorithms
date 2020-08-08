# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:00:17 2020

@author: Tuples and Dictionaries
"""

############################ Tuples ####################################
'''
Tuples are immutable sequences

point = (3.5,4.8)
date = (16,7,2013)

We can perform operations like slice and position extraction on it.

x = point[0]
y = date[1:]

At the same time tuples are immutable.

date[1] = 8, will throw an error
'''

############################ Dictionaries ####################################
'''
PROPERTIES:
    1) Allows keys other than range(0,n)
    2) Keys could be a string like test['abc'] = 10
    3) Any immutable value can be a key.
    4) Can update dictionaries in place, they are mutuable like lists.
    5) Empty dictionary is possible like test1 = {}
    6) Key can be any immutable values- int,float,bool,string,tuple. But not
       list or dictionary
    7) Dictionaries can be nested.
'''
score = {}
score["test1"] = {}
score["test2"] = {}

score["test1"]["Dhawan"] = 84
score["test2"]["Dhawan"] = 100
score["test2"]["Kohli"] = 27

print(score)
# Output: {'test1': {'Dhawan': 84}, 'test2': {'Dhawan': 100, 'Kohli': 27}}

'''
Operating on Dictionaries:
    1) d.keys() --> returns sequence of keys of dictionary d
        
        for k in d.keys():
            # Process d[k]
        
        d.keys() are not in predictable order.
        
        for k in sorted(d.keys()):
            # Process d[k]
        
        Note: sorted(l) returns sorted copy of list l, while l.sort() sorts l in
        place.
        
        d.keys() is not a list, we have to use list(d.keys())
    
    2) d.values() --> is a sequence of values in d
        
        eg. To add all the values in a dictionary
        
        total = 0
        for s in test1.values():
            total = total + s
    
    3) Like lists 'in' can be used in dictionaries keys as well
    
    4) Unlike a list we can insert an entry to a unknown key.
    
        eg. d = {}
            d[0] = 7 # will be executed fine with no error.
    
    5) Structure of dictionary is internally optimised for key-based lookup
       we must use sorted(d.keys()) to retrieve keys in predictable order.
'''