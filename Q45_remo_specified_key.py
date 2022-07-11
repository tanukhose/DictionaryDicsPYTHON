# Q45.
# Write a Python program to remove a specified dictionary from a given list. 
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'},
#  {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},
#  {'id': '#808000', 'color': 'Olive'}]



a=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, 
{'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
l=[]
for i in a:
    if (i['id'])!='#FFFF00':
        l.append(i)
print(l)