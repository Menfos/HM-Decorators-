# Write a decorator to memoize functions with an arbitrary set of arguments.
# Memoization is only possible if the arguments are hashable. Example function - Fibonacci.
#
# Memoization - if function was already called with this arguments, then get result from cache. if not - execute
#  function, store result in cache, and return result.
#
# If the wrapper is called with arguments which are not hashable, then the wrapped function should just be called
#  without caching.
#
# Note: To use args and kwargs as dictionary keys, they must be hashable, which basically means that they must be
#  immutable. args is already a tuple, which is fine, but kwargs have to be converted.
# One way is tuple(sorted(kwargs.items())).
#
# Such functions could be used to reduce cost of computation of some functions.
import functools
from collections import Hashable

def function_decorator(func):
    chache = []
    hashed_args = []
    @functools.wraps(func)
    def wraper(*args,**kwargs):
        is_hashed = True
        arg_array = []
        kkwargs = tuple(sorted(kwargs.items()))
        for number in args:
            arg_array.append(number)
        for number in kkwargs:
            arg_array.append(number)

        for argument in arg_array:
            if(argument.__hash__== False):
                is_hashed = False
                break;


        if(is_hashed):
            print(arg_array)
            try:
                result = chache[hashed_args.index(arg_array)]
                print("In Chache")
                return result
            except ValueError:
                hashed_args.append(arg_array)
                chache.append(func(*args,**kwargs))
                print("Chache miss")
                result = chache[hashed_args.index(arg_array)]
                return result

        else:
            print("Argument not hashable")
            return func(*args,**kwargs)

    return wraper

@function_decorator
def multiplicate(*args,**kwargs):
    x = 1
    for number in args:
        x = x * number
    for index in kwargs:
        x = x * kwargs[index]
    return x

print(multiplicate(1,3,y=2))
print("____________________")
print(multiplicate(1,3,y=2))
print("____________________")
print(multiplicate(2,6,3,1,3,4,222222))
print("____________________")
print(multiplicate(3,1,y=2))










