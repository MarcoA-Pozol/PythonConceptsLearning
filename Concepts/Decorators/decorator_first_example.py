# Support for emojis
import sys
sys.stdout.reconfigure(encoding='utf-8')


"""
    Decorator: A decorator is a function that wraps another function to enhance or modify its behavior.
"""

# Basic decorator example
def my_decorator(parameter_funct):
    def wrapper():
        print("Decorating")
        parameter_funct()
        print("Decorated")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello() 
""" Output: 
    Decorating
    Hello!
    Decorated
"""



#-------------Examples-------------#
# Decorators
def shouting(function):
    def wrapper(*args, **kwargs):
        return f"{function(*args, **kwargs)} 😡!!!".upper()
    return wrapper

def whispering(function):
    def wrapper(*args, **kwargs):
        return f"{function(*args, **kwargs)} 🙈".lower()
    return wrapper


# Decorating
@shouting
def speaking(sentence:str):
    return sentence

print(speaking('I am angry, I wanna eat'))

"""Output:
    I AM ANGRY, I WANNA EAT !!!
"""

@whispering
def speaking(sentence:str):
    return sentence

print(speaking('Could you please give me food?'))

"""Output:
    Could you please give me food? 🙈 
"""