##create a tuple using list with the help of tuple()
list1 = [1,23,'asd','d',32]
tuple1 = tuple(list1)
print("list1:  ",list1)
print("tuple1: ",tuple1)


########################

# Creating a Tuple
# with the use of loop

## for single value tuple we need to put a (,) comma ahead or after the value
Tuple1 = ('Tuple1',)
print("\n",Tuple1)
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)


##################

Tuple2 = ('a',213,'dfs',43,4, )
print("Tuple2: ",Tuple2)
for i in range(len(Tuple2)-1):
    Tuple3 = (Tuple2)
print("Tuple3: ",Tuple3)

################

# Concatenation of tuples
""" Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')

Tuple3 = Tuple1 + Tuple2"""


###################
# Deleting a Tuple

Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

print(Tuple1)

#ERROR occur becoz Tuple not exist

#####################

###   index( )	Find in the tuple and returns the index of the given value where it’s available
###   count( )	Returns the frequency of occurrence of a specified value


#####################


"""      all()	Returns true if all element are true or if tuple is empty
        any()	return true if any element of the tuple is true. if tuple is empty, return false
        len()	Returns length of the tuple or size of the tuple
        enumerate()	Returns enumerate object of tuple
        max()	return maximum element of given tuple
        min()	return minimum element of given tuple
        sum()	Sums up the numbers in the tuple
        sorted()	input elements in the tuple and return a new sorted list
        tuple()	Convert an iterable to a tuple.
"""
"""
Create a List of Tuples Using zip() function

Using the zip() function we can create a list of tuples from n lists.

    Syntax: list(zip(list1,list2,.,listn)

"""

"""
Create a List of Tuples Using Using zip() and iter() method

Here we are going to form a list of tuples using iter() function along with zip() function.

    Syntax: [x for x in zip(*[iter(list)])]

where x is the iterator to iterate in the list, 
zip is used to zip the list, and 
iter() is used to iterate through the entire  list

"""

#Create a List of Tuples Using map() function
##

##  Syntax: list(map(tuple, list_data))

"""
Create a List of Tuples Using list comprehension and tuple() method

Syntax:

    [tuple(x) for x in list_data]

"""



#########################

'''
Create a List of Tuples without using built-in functions

# Function to create a list of tuples

def create_list_of_tuples(lst1, lst2):
    result = []  # Empty list to store the tuples
    for i in range(len(lst1)):
        # Create a tuple from corresponding elements
        tuple_element = (lst1[i], lst2[i])
        result.append(tuple_element)  # Append the tuple to the list
    return result
 
 
# Example usage
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list_of_tuples = create_list_of_tuples(list1, list2)
print(list_of_tuples)



'''