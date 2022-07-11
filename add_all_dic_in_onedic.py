# Q7.
# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
new={}
new.update(dic1)
new.update(dic2)
new.update(dic3)
print(new)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
new={}
new.update({1:dic1})
new.update({2:dic2})
new.update({3:dic3})
print(new)

