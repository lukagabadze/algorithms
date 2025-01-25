import random

# Function to generate a large unsorted list
def generate_large_list(size, lower_bound=1, upper_bound=10000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]