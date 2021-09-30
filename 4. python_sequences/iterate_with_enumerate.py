groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

#number grocery list- not pythonic
index = 1
for item in groceries:
  #f string used to put numbers into string with curly braces
    print(f'{index}. {item}')
    index += 1

#enumerate is pythonic - add argument 1 to start at 1
for index, item in enumerate(groceries,1):
  #f string used to put numbers into string with curly braces
    print(f'{index}. {item}')
