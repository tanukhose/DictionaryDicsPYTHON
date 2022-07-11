# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}



a={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={}
for i in a:
    if i!='c3':
        b.update({i:a[i]})
print(b)