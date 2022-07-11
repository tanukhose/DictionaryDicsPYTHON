# Q42.
# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False


a={'Cierra Vega':12, 'Alden Cantrell':12,'Kierra Gentry':12,'Pierre Cox':12}
val=int(input("enter the number:-"))
for i in a:
    print(end="")
if a[i]==val:
    print("true")
else:
    print("false")
