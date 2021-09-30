#dynamic number of parameters -  any number of arguments can be used to key word argument
def print_teacher(**kwargs):
  for key, value in kwargs.items():
    #f string to make formatting pretty
    print(f'{key}: {value}')
    
print_teacher(name = 'Ashley', job='Instructor', topic = 'Python', second_topic = 'javascript')
