# Testing the number 20 for the Collatz operation

n = 20

# Keeps looping until we reach 1. This assumes that the Collatz conjecture is true.
while n !=1:
  print(n)
  # Checking if n is even
  if n % 2 == 0:
    n = n /2
  else:
    n = ( 3 * n) + 1

print(n)