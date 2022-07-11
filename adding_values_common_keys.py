# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
sum=0
n={}
for i in d1:
    for j in d2:
        if i==j:
            sum=d1[i]+d2[j]
            n.update({i:sum}) 

n.update({i:d1[i]})
n.update({j:d2[j]})

print(n)


# a={
#     1:'tanuja',
#     2:'khose'
#     }
# a[1]='khushboo'
# print(a)




























































