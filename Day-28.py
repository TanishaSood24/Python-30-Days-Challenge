def c(l):
    t = 0
    for i in l:
        t += i
    print("Total:", t)

c([10, 20, 30, 40])



def calculate_total(numbers: list[int]) -> int:
    """
    Returns the sum of a list of integers.
    """
    total = sum(numbers)
    print("Total:", total)
    return total

# Example usage
if __name__ == "__main__":
    scores = [10, 20, 30, 40]
    calculate_total(scores)

    