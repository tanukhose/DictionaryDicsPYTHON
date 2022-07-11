# Q19.
# Write a Python program to remove duplicates from Dictionary.


student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
b=student_data['id2']['subject_integration']
b1=student_data['id2']['class']
b2=student_data['id2']['name']
print(b,b1,b2)

# Sample output:

# {'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4': {'subje
# ct_integration': ['english, math, science'], 'class': ['V'], 'name': ['Surya']}, 'id1': {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}} 
