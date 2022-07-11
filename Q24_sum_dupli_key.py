# Q24.
# Write a Python program to combine values in python list of dictionaries. 
# Sample data: 
#   [{'item': 'item1', 'amount': 400}, 
#   {'item': 'item2', 'amount': 300},
#   {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

a=[{'item': 'item1', 'amount': 400}, 
  {'item': 'item2', 'amount': 300},
  {'item': 'item1', 'amount': 750}]
b={}
sum=0
for i in a:
    # print(i) 
    if i['item'] not in b:
        b[i['item']]=i['amount']
    else:
        f=b[i['item']]+i['amount']
        b[i['item']]=f
print(b)