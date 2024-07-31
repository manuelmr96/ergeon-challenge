from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} times")
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper

# Example usage:
@count_calls
def say_hello():
    print("Hello!")

@count_calls
def add(a, b):
    return a + b

say_hello()
say_hello()
print(add(2, 3))
print(add(5, 7))