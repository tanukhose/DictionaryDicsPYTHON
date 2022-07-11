# Q17.Write a Python program to sort a dictionary by key.


a={3:'rf',1:'gr',7:'hg',4:'yh',2:'le',8:'ld'}
l=[]
for i in a.items():
    l.append(i)
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                t=l[i]
                l[i]=l[j]
                l[j]=t
                # l[i],l[j]=l[j],l[i]
print(l)
# d={}
# for h in l:
#     print(h)
# for g in a.values():
#     print(g)
#     if h==a[g]:
#         d.update({h:g})
# print(d)