# Q14.Write a Python program to multiply all the items in a dictionary.



# a={1:9,2:2,3:7,4:6,5:2}
# m=1
# m1=1
# for i,j in a.items():
#     m*=i
#     # print(m)
#     m1*=j
# # print(m)
# print(m*m1)

a={1:9,2:2,3:7,4:6,5:2}
m=1
m1=1
for i,j in a.items():
    m*=i
    m1*=j
print(m*m1)