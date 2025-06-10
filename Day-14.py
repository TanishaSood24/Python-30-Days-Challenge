def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
num_1 = 5
print("Factorial of", num_1, "is", factorial(num_1))

num_2=6
print("Factorial of", num_2, "is", factorial(num_2))

