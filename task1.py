# Task 1.
#
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args and **kwargs
#  and print them both):
#
# >>> func(4, 4, 4)
# you called func(4, 4, 4)
# it returned 6 6
#
# Such decorators could be useful for debugging.

import functools

def function_decorator(func):
    @functools.wraps(func)
    def function_wraper(*args,**kwargs):
        if (args):
            for number in args:
                print("Your list is:{0}".format(number))
        if (kwargs):
            for key in kwargs:
                print("Your dictionary is:{0}".format(kwargs[key]))
        else:
            pass


        return func(*args,**kwargs)
    return function_wraper


@function_decorator
def up_to_square(*args,**kwargs):
    values = []
    for x in args:
        values.append(x**2)
    for y in kwargs:
        values.append(kwargs[y]**2)
    return values

print(up_to_square(3,2,4,1,3,y=3))
m = [3,2,3,1]
print()