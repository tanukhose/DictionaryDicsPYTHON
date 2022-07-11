# Q36.Write a Python program to match key values in two dictionaries. 
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y



a={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
b={}
c={}
dic={}
for i in a:
    b.update(a[0])
    c.update(a[1])
    for i in c.items():
        for j in b.items():
            if i==j:
                print(i)
                # dic.update({i:j})
                
            else:
                pass
# print(dic)