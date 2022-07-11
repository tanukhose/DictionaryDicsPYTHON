# Q20.Write a Python program to check a dictionary is empty or not.


# Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
sum=0
dic={}
for i in d1:
    for j in d2:
        if i==j:
            sum=d1[i]+d2[j]
            dic.update({i:sum})

dic.update({j:d2[j]})
dic.update({i:d1[i]})
print(dic)