import time

# 🎯 Decorator to log function execution time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ Function '{func.__name__}' ran in {end - start:.4f} seconds\n")
        return result
    return wrapper

#  Function without arguments
@log_execution_time
def welcome_message():
    time.sleep(1)
    print("Welcome to the program!")

# ✅ Function with arguments: Multiply two numbers
@log_execution_time
def multiply(a, b):
    time.sleep(0.5)
    return a * b

#  Run both functions
welcome_message()

result = multiply(4, 5)
print("Multiplication Result:", result)


