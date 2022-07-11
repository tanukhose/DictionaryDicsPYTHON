# Q26.
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# Sample Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11

my_dict=[[1,2,3],[5,6,7],[9,10,11]]
s=[]
i=0
# for i in my_dict:
while i<len(my_dict):
    # print(i,end=" ")
    j=0
    k=[]
    while j<len(my_dict[i]):
        # print(my_dict[j][i],end=" ")
        k.append(my_dict[j][i])
        j+=1

    i+=1
    print(k) 
# i=0
# while i<len(l):
#     j=0
#     while j<len(l):
#         print(l[j][i])
#         j+=1
#     i+=1 



a={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
_1=[]
_2=[]
_3=[]
_4=[]
for i in a:
    # print(i,end="")
    _4.append(i)
    _1.append(a[i][0]) 
    _2.append(a[i][1])
    _3.append(a[i][2])
print(_4)
print(_1)
print(_2)
print(_3) 
print(_4)