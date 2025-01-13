#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
    result *= n
    n -= 1  # Diminue la valeur de n pour éviter une boucle infinie
    return result

    if __name__ == "__main__":
    try:
    if len(sys.argv) < 2:
    raise ValueError("Please provide a number as a command-line argument.")
    num = int(sys.argv[1])
    f = factorial(num)
    print(f"Factorial of {num} is {f}")
    except ValueError as e:
    print(f"Error: {e}")

