# problem_32_Custom Pipeline using Map/Filter/Reduce
from functools import reduce

def process_numbers(lst):
    doubled = list(map(lambda x: x * 2, lst))
    odds = list(filter(lambda x: x % 2 != 0, doubled))
    product = reduce(lambda a, b: a * b, odds, 1)
    return doubled, odds, product

nums = [1, 2, 3, 4, 5, 6]
doubled, odds, product = process_numbers(nums)
print("Original:", nums)
print("Doubled:", doubled)
print("Odd numbers after doubling:", odds)
print("Product of odds:", product)
