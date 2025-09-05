def primes_in_range(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return primes

print(primes_in_range(10, 50))
