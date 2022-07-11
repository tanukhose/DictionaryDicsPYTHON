# Q44.Write a Python program to split a given dictionary of lists into list of 
# dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, 
# {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]




l={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
a,b=l.values()
# print(a,b)
list=[]
for i in range(len(a)):
    dic={}
    # print(b[i])
    dic.update({'Science':a[i]})
    dic.update({'Language':b[i]})
    list.append(dic)
print(list)