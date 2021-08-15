docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

#Can determine how many times something shows up - only looks for exact matches
print(docs.count('tuple'))

#Can identify the index where they are located
print(docs.index('tuple'))

teachers = ['Alena', 'Ashley', 'Nicole', 'Treasure', 'Nicole']
#index returns the first occurrence
print(teachers.index('Nicole'))
#throws error if value not in list
print(teachers.index('Alex'))
