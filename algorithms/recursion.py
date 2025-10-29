"""
Recursion: A function that calls itself, until it doesn't.
- The process of what we do in the function is the same, but with a different input.
- At each step, we make the problem smaller, until we finally get to the base case.
- Base case: When the function does not call itself and returns.
- Recursive case: When the function calls itself.

Call stack: The stack of function calls that are waiting to return.
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)