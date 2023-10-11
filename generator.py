def generate_primes(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = [False] * len(sieve[p*p::p])
    return [str(i) for i, is_prime in enumerate(sieve) if is_prime]

def solution(n):
    # Concatenate prime numbers and find the next five digits
    primes = ''.join(generate_primes(50000))  # Generate enough prime numbers
    return primes[n:n+5]

if __name__ == "__main":
    try:
        n = int(input("Enter a digit between 0 and 10000: "))
        if 0 <= n <= 10000:
            result = solution(n)
            print("The next five prime digits starting at", n, "are:", result)
        else:
            print("Input is out of the valid range (0 - 10000).")
    except ValueError:
        print("Invalid input. Please enter a valid digit between 0 and 10000.")
