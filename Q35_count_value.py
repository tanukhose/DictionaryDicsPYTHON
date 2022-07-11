# Q35. Write a Python program to count the number of items in a dictionary value that is a list.
# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Sample output: 5


# dict={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# b=list(dict.values())
# c=0
# for i in b:
#     for j in i:
#         c+=1
#         print(j)
# print(c)


b={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for i in b:
    for j in b[i]:
        c+=1
        print(j)
print(c)