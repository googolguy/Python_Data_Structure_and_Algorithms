# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:44:04 2020

Description: String Processing
"""
s = " abcdefghijklmnopqrstuvwxyz "

# Remove trailing whitespace
s.rstrip()

# Remove leading whitespace
s.lstrip()

# Remove leading and trailing whitespace
s.strip()

# To search for a pattern
s.find('xyz')
''' Returns first position in s where pattern occurs, -1 if no occurance of
pattern '''

s.find(pattern,start,end)
''' This search for pattern in slice s[start:end] '''

s.index(pattern)
s.index(pattern,start,end)
''' These works similar to find, but will raise ValueError if pattern not found '''

# To Search and Replace
s.replace(fromstr,tostr)
''' This returns copy of s with each occurance of fromstr replaced by tostr '''

s.replace(fromstr,tostr,n)
''' Replace atmost first n copies of fromstr by tostr '''

# Splitting a string
column = s.split(",")
''' We can split using any seperator string '''

column = s.split(":",n)
''' This will split in atmost n chunks '''

# Joining Strings
line = ",".join(columns)
''' Example: date = '16' month = '08' year = '2020' 
            today = "-".join([day,month,year])
            today = "16-08-2020" '''

# Converting Case
s.capitalize()
''' Returns new string with first letter uppercase rest lowercase '''

s.lower()
''' Convert all lowecase to uppercase '''

s.upper()
''' Convert all lowercase to uppercase '''

s.title()
''' Capitalize each word '''

s.swapcase()
''' Invert lowercase to upppercase and vice-versa '''

# Resizing String
s.center(n)
''' Returns a string of length n with s centered, rest blank '''

s.center(n,"*")
''' Fill the blank spaces with * '''

s.ljust(n)
s.ljust(n,"*")
s.rjust(n)
s.rjust(n,"*")
''' Similarly for left and right justify '''

# Other Functions
s.isalpha()
s.isnumeric()
''' To check the nature of characters in string '''

# String Format
'''
Replace argument by position in a message string.

"first:{0}, second:{1}".format(47,11)
output: "first:47, second:11"

"first:{1}, second:{0}".format(47,11)
output: "first:11, second:47"

we can also replace argument by name.

"first:{f}, second:{s}".format(f=47,s=11)
output: "first:47, second:11"
'''

'''
"Value: {0:3d}".format(4)

-> 3d describes how to display the value 4
-> d is a code specifies that 4 should be treated as integer value.
-> 3 is the width of area to show 4

output:'Value:   4'
3 spaces between 4 and : including 1 space already given in input string.
'''

'''
"Value: {0:6.2f}".format(47.523)

-> 6.2f describes how to display 47.523
-> f is a code specifying that 47 should be treated as a floating point value.
-> 6 is width of area to show 47.523
-> 2 is number of digits to show after decimal point.

output:'Value:  47.52'
decimal point is not considered while assigning width of 6
'''