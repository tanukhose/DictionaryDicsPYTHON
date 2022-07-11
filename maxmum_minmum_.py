# Q18.Write a Python program to get the maximum and minimum value in a dictionary.


a={'a':23,'b':12,'c':45,'d':32,'e':10}
max=0
min=0
for i in a:
    if a[i]>max:
        max=a[i]
        k=i
    else:
        min=a[i]
        k2=i
print(max,k)
print(min,k2)
