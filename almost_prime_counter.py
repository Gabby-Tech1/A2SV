def count_almost_primes(n):
    """
    Counts the number of almost prime numbers from 1 to n inclusive.
    An almost prime number has exactly two distinct prime divisors.
    
    Args:
        n: The upper limit (inclusive)
        
    Returns:
        The count of almost prime numbers between 1 and n
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    count = 0
    
    for num in range(2, n + 1):
        distinct_prime_divisors = 0
        
        for prime in range(2, num + 1):
            if not is_prime[prime]:
                continue
                
            if num % prime == 0:
                distinct_prime_divisors += 1
                
                while num % prime == 0:
                    num //= prime
        
        if num > 1:
            distinct_prime_divisors += 1
            
        if distinct_prime_divisors == 2:
            count += 1
            
    return count
