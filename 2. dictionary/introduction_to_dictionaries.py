course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}
# get the teacher name
print(course['teacher'])
#obtain keys for a dictionary
print(course.keys())
#print values 
print(course.values())
#print sorted keys
print(sorted(course.keys()))
#print sorted values
print(sorted(course.values()))
#change value for the teacher key
course['teacher'] = 'Treasure'
# change level from beginner to intermediate
course['level'] = 'Intermediate'
# add to the dictonary
course['stages'] = 2
# add new key/value pair
course['track']  = 'Data Science'
print(course)
#remove from dictionary
del(course['stages'])
print(course)
