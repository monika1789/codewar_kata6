# Find the number is preime or nit
import math

def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
             if num % i == 0:
                return False
                break
        return True