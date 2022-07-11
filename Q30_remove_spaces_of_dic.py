# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 




a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# b=list(a.keys())
new={}
for i,j in a.items():
    for x in " ":
        k=i.replace(x,"")
        new[k]=j
print(new)
