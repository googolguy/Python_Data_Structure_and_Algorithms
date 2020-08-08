# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:29:50 2020

Description: Pass Delete and None
"""
# pass
'''
we can use pass for a null statement in blocks such as except:, else:,...
that cannot be left empty.
'''
while True:
    try:
        udata = input("Enter a number:")
        unum = int(udata)
    except ValueError:
        pass # Do Nothing
    else:
        break
print("Number entered: ",unum)

# del()
'''
del is used to remove a entry.
'''
l = list(range(10))
print("Before:",l)
del(l[4])
print("After:",l)
''' This removes l[4] from list and automatically contracts the list. '''

'''
This also works with dictionaries.
del(d[k]) - remove the key k and its associated value.

In general del(x) removes the value associated with x, makes x undefined
'''
x = 5
del(x)
y = x+5

''' Output: NameError: name 'x' is not defined '''

# None
'''
It is a special value used to denote "nothing"

Use it to initialize a name and letter checks if it has been assigned a valid 
value
'''

x = None
if x is not None:
    y = x

''' Python has exactly one value None.
x is None is same as x == None
'''

# Summary
'''
1) Use pass for an empty block.
2) Use del() to remove elements from a list or dictionary.
3) Use the special value None to check if a name has been assigned a valid value.
'''