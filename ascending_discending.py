# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.

# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}


# numlist=[]
# listlength=int(input("enter length of list: "))
# for i in range(listlength):
#     value=int(input("enter value of elements:"))
#     numlist.append(value)
# for i in range (listlength):
#     for j in range(listlength):
#         if numlist[i]<numlist[j]:
#             temp=numlist[i]
#             numlist[i]=numlist[j]
#             numlist[j]=temp
# print("asscending",numlist)


# sort dictionary by value Ascending. 
# d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4} 
# a = sorted(d.items(), key=lambda x: x[1]) 
# print(a)



a={-1: 2, -3: 4, -4: 3, -2: 1, 6: 0}
l=[]
d={}
for i in a:
    l.append(a[i])
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
print(l)
n={}
for h in l:
    for g in a:
        if a[g]==h:
            n.update({g:h})
print(n)



# a={2:43,5:23,7:76,1:54,6:65,4:56}
# l=[]
# for i in a:
#     l.append(i)
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if l[i]<l[j]:
#                 l[i],l[j]=l[j],l[i]
# print(l)
# # d={}
# # for g in l:
# #     for h in a:
# #         if a[h]==g:
# #             d.update({h:g})
# # print(d)


# descending


a={1:21,2:34,3:54,4:65,5:84}
l=[]
for i in a:
    l.append(a[i])
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
print(l)
d={}
for h in l:
    for g in a:
        if a[g]==h:
            d.update({g:h})
print(d)




