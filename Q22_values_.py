# Q22. Write a Python program to create and display all combinations of letters, 
# selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

a={'1':['a','b'], '2':['c','d']}
b=list(a.values())
for i in b[0]:
    for j in b[1]:
        print(i+j)
