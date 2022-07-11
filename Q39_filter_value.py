# Q39.Write a Python program to filter a dictionary based on values. 
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}



a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
b={}
for i in a:
    if a[i]>170:
        b.update({i:a[i]})
print(b)