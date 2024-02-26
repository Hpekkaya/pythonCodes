def find_primes(n):
    primes = []  # We'll store the prime numbers we find in this list

    # We'll check each number from 2 up to 'n' to see if it's prime
    for num in range(2, n + 1):
        is_prime = True  # Assume 'num' is prime unless proven otherwise

        # To check if 'num' is prime, we'll try dividing it by every number from 2 to its square root
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # If 'num' is divisible by 'i', then it's not prime
                is_prime = False
                break

        # If 'num' is still marked as prime after the inner loop, add it to our list of prime numbers
        if is_prime:
            primes.append(num)

    return primes


# Example usage:
up_to = 20
print("Prime numbers up to", up_to, "are:", find_primes(up_to))
