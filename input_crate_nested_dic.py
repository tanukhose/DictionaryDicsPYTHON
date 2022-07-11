
dict={}
a=int(input("enter the length:="))
for i in range(a):
    n=input("enter the name")
    g=int(input("enter the age"))
    key={}
    key.update({'name':n})
    key.update({'age':g})
    dict.update({i+1:key})
print(dict)
    

# a=int(input("enter the langth:-"))
# dic={}
# for i in range(a):
#     x=input("enter the name")
#     y=int(input("enter the class"))
#     z=int(input("enter the age"))
#     d={}
#     d.update({'name':x})
#     d.update({'class':y})
#     d.update({'age':z})
#     dic.update({i+1:d})
# print(dic)