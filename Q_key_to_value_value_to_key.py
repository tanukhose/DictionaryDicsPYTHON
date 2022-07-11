a={1:'tanu',2:'khose',3:'bulbul',4:'pavi'}
k=[]
v=[]
dic={}
for i in a:
    k.append(i)
    v.append(a[i])
    for j in range(len(k)):
        dic.update({v[j]:k[j]})
print(a)
print(dic)


