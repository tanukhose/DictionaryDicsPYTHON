# Q37.Write a Python program to create a dictionary of keys x, y, and z where 
# each key has as value a list from 11-20, 21-30, and 31-40 respectively. 
# Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]


x=[11, 12, 13, 14, 15, 16, 17, 18, 19]
y=[21, 22, 23, 24, 25, 26, 27, 28, 29]
z=[31, 32, 33, 34, 35, 36, 37, 38, 39]
dic={}
a=[]
b=[]
c=[]
for i in range(len(x)):
    a.append(x[i])
    b.append(y[i])
    c.append(z[i])
    dic.update({'x':a})
    dic.update({'y':b})
    dic.update({'z':c})
print(dic)


# x=[11, 12, 13, 14, 15, 16, 17, 18, 19]
# y=[21, 22, 23, 24, 25, 26, 27, 28, 29]
# z=[31, 32, 33, 34, 35, 36, 37, 38, 39]
# dic={}
# for i in range(len(x)):
#     dic.update({'x':x[i]})
#     dic.update({'y':y[i]})
#     dic.update({'z':z[i]})
# print(dic)