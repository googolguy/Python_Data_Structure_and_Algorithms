# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:02:51 2020

Description: File Handling
"""

# Opening a File
fh = open("gcd.py","r")

'''
Second argument is MODE of opening file.
1) Read, "r": Open a file for reading only.
2) Write, "w": Create an empty file to write to.
3) Append, "a": Append to an existing file.
'''

# Reading through File Handles
content = fh.read()
''' Note: Reads entire file into name as a single string '''

content = fh.readline()
'''Note: Read one line into name. Line end with '\n', string include '\n' unlike
input() '''

content = fh.readlines()
'''Note: Reads entire file as list of strings. each string is one line.
ending with '\n' '''

# Reading Files
fh.seek()
''' Move pointer to position n, i.e. move back and forth in reading operation '''

block = fh.read(12)
''' Reads a fixed number of characters '''

# End of File
''' When reading incremently, important to know, when file has ended
    The following both signal end of file 
    1) fh.read() returns empty string ""
    2) fh.readline() returns empty string "" 
'''

# Writing to a file
fh.write(s)
''' It writes string s to file and returns number of characters written.
we have to include '\n' explicitely to go to a new line. '''

fh.writelines(l)
''' It write list of lines l to file. we must include '\n' explicitely to each
string. '''

# Closing a file
fh.close()
''' It flushes output buffer and decouples file handle. All pending writes
are copied to disk '''

fh.flush()
''' Manually forces write to disk '''

# Processing file line by line
''' Method - 1 '''
contents = fh.readlines()
for l in contents:
    # Process Code

''' Method - 2 '''
for l in fh.readlines():
    # Process Code

# Copying a file
''' Method - 1 '''
infile = open("input.txt","r")
outfile = open("output.txt","w")
for line in infile.readlines():
    outfile.write(line)
infile.close()
outfile.close()

''' Method - 2 '''
infile = open("input.txt",'r')
outfile = open('output.txt','w')
contents = infile.readlines()
outfile.writelines(contents)
infile.close()
outfile.close()

# Strip newline character '\n'
'''
1) Getting rid of trailing '\n'
    contents = fh.readlines()
    for line in contents:
        s = line[:-1]

2) Instead use rstrip() to remove trailing whitespace
    for line in contents:
        s = line.rstrip()

3) Also strip() - removes from both sides.
        lstrip() - removes from left side.
'''