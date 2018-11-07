#!/usr/bin/env python3

def my_function(x, y):
    return x + y


def my_print_function(name):
    print("Hello, my name is " + name)


# creates a new variable with the output of the function my_function
# then prints the result
x_plus_y = my_function(x, y)
print(x_plus_y)

# calls the function my_print_function for the name "Sam"
my_print_function("Sam")
