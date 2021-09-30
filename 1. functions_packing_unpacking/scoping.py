#global variable -  highest level
num = 10

def set_num():
    num = 5
    #local variable
    letter = 'a'
    print(letter)

set_num()
#prints global variable not local
print(num)

