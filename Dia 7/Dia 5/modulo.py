from functools import reduce
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def find_lcm_of_list(lst):
    return reduce(lcm, lst)