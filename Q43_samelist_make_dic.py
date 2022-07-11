# Q43.Write a Python program to create a dictionary grouping a sequence of
# key-value pairs into a dictionary of lists. 
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}







def dic(l):
    b={}
    for i, j in l:
        b.setdefault(i,[]).append(j)
    return b
a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(dic(a))