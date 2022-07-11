# # Q16.Write a Python program to map two lists into a dictionary

# a=['o','t','th','f','s']
# b=[1,2,3,4,5]
# dic={}
# for i in range(len(a)):
#     dic.update({a[i]:b[i]})
#     # dic[a[i]]=b[i]
# print(dic)


a=['o','t','th','f','s']
b=[1,2,3,4,5]
dic={}
for i in a:
    for j in b:
        # dic[i]=j
        dic.update({i:j})
        b.remove(j)
        break
print(dic)
