course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

#Iterating dictionaries uses for loops
#prints only the key    
for item in course:
  print(item)
  
#print values
for item in course:
  print(course[item])
  
#Pythonic method to print keys and values
print(course.items())

#Use of multiple assginment - first assgined to key and second to value
for key, value in course.items():
  print(key)
  print(value)
