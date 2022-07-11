# Q29.Write a Python program to sort a list alphabetically in a dictionary.


a=['d','j','s','a','c','b','e','f','t']
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print(a)
dic={}
c=0
for i in a:
    c=c+1
    dic[c]=i 
print(dic)