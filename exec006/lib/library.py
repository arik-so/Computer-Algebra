__author__ = 'ariksosman'

def eratosthenes(maximum): # diese Funktion ist jetzt superschnell
    primes = [true]*(maximum+1)
    primes[0] = false
    if 1<= maximum:
        primes[1] = false
    for i in range(2, maximum):
        if i%2 == 0 and i > 2:
            primes[i] = false
            continue
        if i*i > maximum:
            break
        minFactor = i
        maxFactor = ceil(maximum/i)
        for j in range(minFactor, maxFactor+1):
            if i*j > maximum:
                break
            else:
                primes[i*j] = false
    primeArray = []
    for i in range(2, maximum+1):
        isPrime = primes[i]
        if isPrime:
            primeArray.append(i)
    return primeArray