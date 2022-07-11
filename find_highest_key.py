# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.


a={9:'ta',2:'kh',7:'nu',4:'ng',1:'ose'}
h1=0
h2=0
h3=0
for i in a:
    if i>h1:
        h1=i
for i in a:
    if i>h2 and i!=h1:
        h2=i
for i in a:
    if i>h3 and i!=h2 and i!=h1:
        h3=i
print(h1)
print(h2)
print(h3)