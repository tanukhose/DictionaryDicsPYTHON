# a=3+2j
# b=4+3j
# print(b*a)



# i=1
# while i<=100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         print(i)
#     i+=1





# a=[2,34,21,43,32,5,45]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]%a[j]==0:
#             c+=1
#         j+=1
#     if c==2:
#         b.append(a[i])
#     else:
#         print(a[i])
#     i+=1
# print(b)



# a=[3,2,36,43,54,65,98,69]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# a=['tanu','meena','pavitra']
# b=[['khose',17],['meheto',18],['k',20]]
# f={}
# for i in range(len(a)):
#     # c[a[i]]=b[i]
#     c={}
#     for j in range(len(b)):
#         for g in range(len(b[j])):
#             # print(b[j][g])
#             # if b[j][g]==0:
#             c.update({'surname':b[j][0]})
#             # elif b[j][g]==1:
#             c.update({'age':b[j][1]})
#         f[a[i]]=c       

#         print(f)


# a=['tanu','meena','pavitra']
# b=[['khose',17],['meheto',18],['k',20]]
# f={}
# for i in range(len(a)):
#     c={}
#     v={}
#     v.update({'surname':b[i][0]})


#     c.update({"age":b[i][1]})
#     v.update(c)
#     f.update({a[i]:v})

# print(f)   



# a=['tanu','meena','pavitra']
# b=[['khose',17],['meheto',18],['k',20]]
# f={}
# for i in range(len(a)):
#     c={}
#     v={}
#     l=[]
#     v.update({'surname':b[i][0]})
#     c.update({"age":b[i][1]})
#     l.append(v)
#     l.append(c)
#     f.update({a[i]:l})
# print(f)   



# i=1
# while i<100:
#     if i%2!=0 and i%3!=0 and i%5!=0:
#         print(i,"prime")
#     elif i==2 or i==3 or i==5:
#         print(i,"prime")
#     # else:
#     #     print(i)
#     i=i+1           


# l=[1,3,5,7,9,10]
# l2=[1,2,4,6,8]
# list=[]



# l=[1,2,3,4,5,6]
# i=0
# b=[]
# while i<len(l)-1:
#   k=l[i+1]-l[i]
#   b.append(k)
#   i+=1
# # print(b)
# i=0
# c=0
# a=b[i]
# while i<len(b):
#   if b[i]==a:
#     c+=1
#   i+=1
# if c==len(b):
#   print("true")
# else:
# #   print("false")

# num=int(input("enter the length:-"))
# d={}
# for i in range(num):
#     a=input("enter the key:=")
#     d.update({a:len(a)})
# print(d)    

   


# # clear
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.clear()
# print(a)

# # pop
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.pop(3)
# print(a)

# # popitem
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.popitem()
# print(a)

# # update
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# a.update({10:"navgurukul"})
# print(a)

# # key
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.keys()
# print(b)

# # values
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.values()
# print(b)

# # items
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.items()
# print(b)

# # del
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# del a[1]
# print(a)

# # get
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.get(4)
# print(b)

# # # fromkeys
# # a={1:'ta',2:'kh',3:'ose',4:'nu'
# # print(a)

# # # copy
# a={1:'ta',2:'kh',3:'ose',4:'nu'}
# b=a.copy()
# print(b)


# i=1
# b=1
# s=0
# while i<=10:
#     if i<=5:
#         b*=i
#     elif i>=6:
#         s+=i
#     i+=1
# print(b)
# print(s)


a=int(input("enter the length:-"))
dic={}
for i in range(a):
    d={}
    n=input("enter the name")
    ag=int(input("enter the age"))
    d.update({'name':n})
    d.update({'age':ag})
    dic.update({i+1:d})
print(dic)
