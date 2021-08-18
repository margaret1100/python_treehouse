#If number of arguments is not known
def my_function(*args):
    for val in args:
        print(val)
    
my_function("Hello", "I", "love", "python")
