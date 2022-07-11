# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}



list=[1, 2, 3, 4]
a={}
for i in list:
    # print(a)
    a={list[-i]:a}
    # a.update({list[-i]:a})
print(a)

# list=[1, 2, 3, 4]
# n=a={}
# for i in list:
#     a[i]={}
#     a=a[i]
# print(n)
