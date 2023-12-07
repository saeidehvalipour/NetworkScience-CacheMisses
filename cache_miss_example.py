# cache_miss_example_revised.py
import random

def create_large_list(size):
    # Creating a smaller list
    return [random.randint(0, 1000) for _ in range(size)]

def access_pattern(lst, size):
    # Accessing the list in a random non-sequential manner
    for _ in range(size):
        index = random.randint(0, len(lst) - 1)
        lst[index] += 1

def main():
    size = 10**3  # 1 million elements, reduced from 10 million
    large_list = create_large_list(size)

    # Access the list in a pattern likely to cause cache misses
    access_pattern(large_list, size)

if __name__ == "__main__":
    main()
