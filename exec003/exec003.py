__author__ = 'ariksosman'

def eratosthenes_new(maximum): # diese Funktion ist jetzt superschnell
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

def calcBezoutIdentity(a, b):
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    q = ["null"]
    i = 1
    while r[i] > 0:
        r.append(r[i-1]%r[i])
        q.append(floor(r[i-1]/r[i]))
        s.append(s[i-1]-q[i]*s[i])
        t.append(t[i-1]-q[i]*t[i])
        i = i+1
#    for j in range(i):
#        print "i = ", j
#        print "r = ", r[j]
#        print "s = ", s[j]
#        print "t = ", t[j]
#        print "q = ", q[j]
#        print "sa + tb = ", s[j]*a + t[j]*b
#        print s[j],' * ',a,' + ',t[j],' * ',b,' = ',s[j]*a + t[j]*b
    return r[i-1], s[i-1], t[i-1]

def inv(a, n):
    bezout = calcBezoutIdentity(a, n)
    print bezout
    gcd = bezout[0]
    inverse = bezout[1]
    print inverse, '*', a, ' + ', bezout[2], '*', n, ' = ', gcd
    if gcd == 1:
        return inverse
    return false

def add(a, b, n):
    return (a+b) % n

def mult(a, b, n):
    return (a*b) % n

def lastDigits(factor, necessaryLast3Digits): # e. g. (67, 123), (67, 124), (68, 123), (68, 124)
    suitableAs = []
    for a in range(0, 1001):
        multiple = a*factor
        last3Digits = multiple%1000
        if last3Digits == necessaryLast3Digits:
            suitableAs.append(a)

    return suitableAs

def pow(n, b, e):
    necessaryFactors = []
    currentExponent = e
    currentBase = b
    while true:
        currentBase = currentBase%n
        if currentExponent == 1:
            break
        if currentExponent%2 == 1:
            necessaryFactors.append(currentBase)
        currentExponent = floor(currentExponent/2)
        currentBase = currentBase*currentBase
    result = currentBase
    for currentFactor in necessaryFactors:
        result = result*currentFactor
    return result%n

def modular_pow(base, exponent, modulus):
    c = 1
    for e_prime in range(1, exponent+1):
        c = (c * base) % modulus
    return c

def calcRSAModulus(maxProduct):
    maxFactor = sqrt(maxProduct)
    variance = maxFactor*0.75
    referenceInt = int(round(random()*variance+ maxFactor - variance/2));
    # availablePrimes = eratosthenes_new(maximum)
    # primeCount = len(availablePrimes)
    # p = int(round(random()*primeCount-1))
    # q = int(round(random()*primeCount-1))
    p = next_prime(referenceInt)
    q = next_prime(p)
    phi = (p-1)*(q-1)
    factors = 'too long to calculate'
    # factors = factor(phi)
    n = p*q
    print 'p =', p, ', q =', q, 'phi =', phi, ' =', factors
    # return p, q, n