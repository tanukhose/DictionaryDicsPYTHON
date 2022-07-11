# Q6.
# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# a={0: 10, 1: 20}
# a[2]=30
# print(a)

# a={0: 10, 1: 20}
# b={}
# b.update(a)
# b.update({2:30})
# print(b)

a={0: 10, 1: 20}
a.update({2:30})
print(a)
