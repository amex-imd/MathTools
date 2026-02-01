import mathtools as mt

print(mt.number_primes(100))
for i in mt.Eratosthenes_sieve(100):
    print(i)