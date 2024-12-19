user_input = input("Enter a tuple of elements (separated by commas): ")


original_tuple = tuple(user_input.split(","))


repeat_element = input("Enter an element to repeat: ")
repeat_times = int(input("Enter the number of times to repeat: "))


new_tuple = []
for element in original_tuple:
    if element == repeat_element:
        new_tuple.extend([element] * repeat_times)
    else:
        new_tuple.append(element)


print("Original Tuple:", original_tuple)
print("New Tuple:", tuple(new_tuple))
