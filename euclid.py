"""

The plan:

Based on the problem description, we are going to need the following:

- Variables to store the two numbers input by the user.
- A loop to repeatedly apply Euclid's Algorithm (using modulo) until we find the GCD.
- Optionally, a list to track each step of the calculation if we want to log it.

Our Task(s):

1. Ask the user to input two positive integers.
2. Apply Euclid's Algorithm:
   - While the second number is not zero:
       a. Compute the remainder of the first number divided by the second number.
       b. Replace the first number with the second number, and the second number with the remainder.
3. Once the second number is zero, the first number is the GCD.
4. Print the GCD.
5. Optionally, print or save each step of the calculation to a file.

Programmer's Notes:

If you have two numbers, a and b, the GCD of a and b is the same as the GCD of b and the remainder when a is divided by b.

You repeat this process — replacing the pair (a, b) with (b, a % b) — until the remainder is zero.

When the remainder reaches zero, the other number (b at that point) is the GCD.

"""

# --------------------------------------------------------------------------------------------------------------------#

print("Welcome to the GCD Calculator, powered by Euclid's Algorithm!\n")

first_number = int(input("Enter the first positive integer: "))
second_number = int(input("Enter the second positive integer: "))

original_first = first_number
original_second = second_number

# Euclid's Algorithm ( Where the magic happens... :D )
while second_number != 0:
    remainder = first_number % second_number
    first_number = second_number
    second_number = remainder

# Print the result ( The GCD of the two numbers )
print(f"\nThe GCD of {original_first} and {original_second} is {first_number}.\n")
