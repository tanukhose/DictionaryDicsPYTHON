# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.

# a={'nav':'gurukul','place':'pune','name':'tanu','form':'maharastra'}
# b=input("enter the key")
# if b in a:
#     print("exists")
# else:
#     print("not exists")


a={'nav':'gurukul','place':'pune','name':'tanu','form':'maharastra'}
b=input("enter the value")
for i in a:
    if b in a[i]:
        print("exists")
    else:
        print("not exists")
        
