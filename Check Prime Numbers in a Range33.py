# 2. Check Prime Numbers in a Range
def primes_in_range(n1, n2):
    for num in range(n1, n2 + 1):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")

primes_in_range(10, 50)
