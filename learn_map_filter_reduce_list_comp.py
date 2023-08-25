import functools
# MAP
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
extra = [12,23,23,234,]
def square_of_i(x):
    return "i" * x

new_example_list = list(map(square_of_i, example_list))
print(new_example_list)

# FILTER 

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_example_list = list(filter(lambda x: x > 2, example_list))
print(new_example_list)

# REDUCE
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def add(x, y):
    return x + y

new_example_list = functools.reduce(add, example_list)
print(new_example_list)

# LIST COMPERIHENSIVE
example_list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
example_list= [i if not i == 0 else "This is zero number and index" for i in example_list]
print(example_list)
