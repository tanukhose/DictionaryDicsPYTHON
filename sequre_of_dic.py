# Q3.Write a Python script to generate and print a dictionary that contains 
# a number (between 1 and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

a=int(input("enter the number"))
dic={}
for i in range(1,a):
    v=i*i
    dic[i]=v
    # dic.update({i:v})
print(dic)


# Q4. Write a Python script to print a dictionary where the keys are numbers    
# between 1 and 15 (both included) and the values are square of keys.
# Simple Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 
# 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}.

dic={}
for i in range(1,16):
    # dic.update({i:i*i})
    dic[i]=i*i
print(dic)


# Q10.Write a Python script to print a dictionary where the keys are numbers between 1 
# and 15 (both included) and the values are square of keys. 
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 
# 12: 144, 13: 169, 14: 196, 15: 225}
dic={}
for i in range(1,16):
    v=i*i
    # dic[i]=v
    dic.update({i:v})
print(dic)