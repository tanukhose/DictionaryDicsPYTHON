# Q13.Write a Python program to sum all the items in a dictionary.


a={1:23,2:12,3:45,4:32,5:10}
sum=0
sum1=0
for i in a.keys():
    sum+=i
print(sum)
for j in a.values():
    sum1+=j
print(sum1)
print(sum+sum1)
        

a={1:23,2:12,3:45,4:32,5:10}
sum=0
sum1=0
for i,j in a.items():
    sum+=i
    sum1+=j
print(sum+sum1)
        
