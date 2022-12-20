# Decorators are taking a function and modifying that function.
# It takes a function and returns a modified version of the function
# This is known as a functional programming paradigm where functions are themselves values.

def announce(f):
    def wrapper():
        print("Taking the function...")
        f()
        print("Done with the function.")
    return wrapper    

@announce
def hello():
    [print("Hello everyone!")]    