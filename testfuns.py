import string

file1 = open('names.txt','r', encoding="utf-8")
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print( str(line))