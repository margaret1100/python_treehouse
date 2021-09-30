#dictionary
teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}
#function
def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)


#To use the function - function call with **before argument
#** unpacks all the key-value pairs in the dictionary into three keyword arguments.
print_teacher(**teacher)
