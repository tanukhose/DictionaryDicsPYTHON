# Q41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}



a={'Cierra Vega':(6.2, 70),'Alden Cantrell':(5.9, 65),'Kierra Gentry':(6.0, 68),
'Pierre Cox':(5.8, 66)}
b={}
for i in a:
    if a[i][0]>=6 and a[i][1]>=70:
        print(i,":",a[i])