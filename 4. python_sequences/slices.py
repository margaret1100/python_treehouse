#slice has a start, stop, and step value
#slicing creates a mew sequence -  does not change an existing sequence
nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums_partial = nums[0::2]
print(nums_partial)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#starts at index 3 and stops right before stop value
colors_partial = colors[3:6]
colors_backwards = colors[::-1]
print(colors_partial)
print(colors_backwards)
