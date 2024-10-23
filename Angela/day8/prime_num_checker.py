#if a num divisible by anything else other than 1 and itself than prime
# def prime_checker(n):
#   if n in [1,2,3]:
#     print("prime")
#   for i in range(2,n):
#     if(n%i == 0):
#       break
#   print("not prime")
  
#   prime_checker(100)
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for factors from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False  # If n is divisible by any number, it's not prime
    return True

# Example usage:
number = 1738737
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")