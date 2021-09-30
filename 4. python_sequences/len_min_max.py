nums = (1,2,3,4,5,6,7,8,9,10)
#length of the list
print(len(nums))
#max value of list
print(max(nums))
#min value of list
print(min(nums))

#These functions can be used on strings
my_string = 'treehouse'
#prints the length of the string
print(len(my_string))
#gets the max value (unicode order)
print(max(my_string))
#gets the min value (unicode order)
print(min(my_string))

mixed = 'treehouse2019'
#python uses lexigraphical order nums lower than letters
print(len(mixed))
#gets the max value (lexigraphical order)
print(max(mixed))
#gets the min value (lexigraphical order)
print(min(mixed))
