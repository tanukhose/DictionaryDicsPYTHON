# Q17.Write a Python program to sort a dictionary by key.


a={9:'ta',2:'kh',7:'nu',4:'ng',1:'ose'}
c=0
num=[]
for i in a.items():
    c+=1
    num.append(i)
for i in range (c):
    for j in range(c):
        if num[i]<num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
             
print(num)



# a={9:'ta',2:'kh',7:'nu',4:'ng',1:'ose'}
# b=sorted(a.items())
# print(b)


        
        