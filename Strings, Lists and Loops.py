# -*- coding: utf-8 -*-
"""
Spyder Editor

Description: Information regarding Strings and lists Data structures.
"""

# Strings are immutable, where are lists are not.

# Float is stored in a sequence which is divided into Mantissa and exponent.

'''
Arithmatic Operators:
    / - Division
    // - Quotient
    % - Remainder
    ** - Raise to Power

Logical Operators: not, and, or
'''

# Division operator always leads to float.

# type(exp) function returns type of "exp"

# For string, Both single position and slice return strings.

# For lists, A single position returns a value and slice returns a list.

# List are mutable.

# int, float, bool and string are immutable.

'''
eg: Mutable and Immutable difference.

list1 = [1, 2, 3]

list2 = list1

list1[1] = 5

# Then

list1 = [1, 5, 3]

list2 = [1, 5, 3]

List2 gets updated automatically as in Python list1 and list2 are names of 
same list. Therefore lists are called mutable, where as string, int, float and
bool are immutable.

For immutable data structures a fresh copy is made during assignments where
as in mutable assignments they point to same location.

list1 --> [1,2,3] <-- list2

'''

'''
So how to make a copy of existing list.
Here slice comes to resque as slice creates a new sublist.

l[:k] is l[0:k]
l[k:] is l[k:len(l)]

omitting both ends points give a full slice.
l[:] == l[0:len(l)]

To copy a list it's better to use a full slice.
'''

'''
Example:

list1 = [1,3,5,7]
list2 = list1[:]

# Now list2 = [1,3,5,7]

list3 = list2

All 3 lists mentioned above are equal, but there is a difference.
1) list1 and list2 are two lists with same value.
2) list2 and list3 are two names for same list.
    
Note: 
    x==y checks if x and y has same value.
    x is y checks if x and y refers to same value. Any change in x will be
    reflected in y in this case.

list1 == list2 --> True
list2 == list3 --> True

list1 is list2 --> False
list2 is list3 --> True
'''

'''
Concatenation of list

list1 = [1,2,3]
list2 = [4,5,6]

list1 + list2 = [1,2,3,4,5,6]

+ operator creates a new list.

where as append function extends the list with a new value without creating
a new list.
'''

# Append Function: l1.append(x) - append takes a value as argument.

# Extent Function: l1.extent(l2) - extent takes another list as argument.

# Remove Function: l1.remove(x) - it removes the first occurance of x and will
#                                 through an error if no copy of x exists in l1.

# Reverse Function: l1.reverse() - reverse list l1.

# Sort Function: l1.sort() - sort l1 in ascending order.

# Index Function: l1.index(x) - find leftmost position of x in l1, will throw
#                               an error if x is not in l1.
#                 l1.rindex(x) - find right most position of x in l1.         

'''
Control Flow: Everything in Python is True except zero 0, empty string "" and
empty list []
'''

########################### List Operations ###############################
'''
1) map(f,l), applies function f to each element of l.
    [x1,x2] --> f(x1),f(x2)
    
    Output of map is not a list, we have to use list(map(f,l)) to get a list.
    And output can directly used in a for loop.
    
        for i in map(f,l):
    it is similar to range(i,j) and d.keys()

2) filter()
    filter(p,l), checks p for each element of l and output is sublist of values
    that satisfy p
'''

'''
Combining Map and Filter:
    eg. To find out squares of even numbers from 0 to 99
'''
def even(x):
    return x%2==0

def square(x):
    return x**2

print(list(map(square, filter(even,range(100)))))

########################### List Comprehension ###############################
'''
To find squares of all even numbers from 0 to 99
'''
def even(x):
    return x%2==0

def square(x):
    return x**2

print([square(x) for x in range(100) if even(x)])

'''
List comprehension for pythogorean triple: x^2 + y^2 = z^2
'''

l1 = [(x,y,z) for x in range(100) for y in range(100) for z in range(100) if (x*x + y*y == z*z)]
print(l1)

'''
The above mentioned list comprehension will leads to duplicates like
(3, 4, 5) and (4, 3, 5)
Therefore to remove duplicates
'''
l2 = [(x,y,z) for x in range(100) for y in range(x,100) for z in range(y,100) if (x*x + y*y == z*z)]
print(l2)

'''
List comprehension for initializing lists.

Initialize a 4x3 matrix.
    4 rows and 3 columns, stored row wise.
'''
l3 = [[0 for i in range(3)] for j in range(4)]
print("4x3 Matrix:", l3)

'''
Warning: Don't create a list and repeat it 4 times to create a matirx as it 
         will cause inapropiate results while updating list in future.
'''
zerolist = [0 for i in range(3)]
l = [zerolist for j in range(4)]

print(l)
# Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
l[1][1] = 1
# Output: [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
print(l)

# Reason behind such output is each row in l list points to same list zerolist



########################### IMPORTANT POINT ###############################
'''
A loop can also have an else: signals normal termination.

else statement can be used with both For or While loops.

example:
'''   
def findpos(l,v):
    for i in range(len(l)):
        if l[i] == v:
            position = i # EXIT and report position
            break
    else:
        position = -1 # No break, v is not in l
    return position

lin = list(input("Enter the input:"))
vin = str(input("Enter the number:"))
print(lin,vin)

print(findpos(lin, vin))

# Here else behaves as a special action for normal termination of loop.
# In other words else statement will only be executed if loops terminates in 
#  a normal way and break statement is not executed.


