# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# dic={"a":1,"b":17}
# b=dic.get("a")
# print(b)


a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for i in range(3):
    k=input("enter the key")
    b=a.get(k)
    print(k,b)