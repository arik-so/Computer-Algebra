__author__ = 'ariksosman'

# from SAGE_PATH+lib import library as goodies # fuck sage, wieso geht das nicht?!

def dixon(n, l, c, methodNum):

    factorBase = eratosthenes(l)

    exponentVectors = []
    smoothCount = 0

    start = ceil(sqrt(n))
    for i in range(start, n):

        if(smoothCount >= c):
            break

        testSubject = (int(random()*(n-start)+start))**2 % n

        for j in range(0, len(factorBase)):

            p = factorBase[j] # we look for a prime such that testSubject squared = p squared (mod n)

            if p**2 % n == testSubject:
                exponentVectors.append([testSubject, p])

    factors = []

    if(methodNum == 3):

        for i in range(len(exponentVectors)):
            factor = gcd(exponentVectors[i][0]-exponentVectors[i][1],n)
            if(factor != 1):
                if (factor in factors) == false:
                    factors.append(factor)

    if(methodNum == 1):

        for i in range(floor(sqrt(n))-c, floor(sqrt(n))+c):
            distance = i - (floor(sqrt(n))-c)
            x = floor(sqrt(n))+floor(distance/2)*((((distance+1)%2)-0.5)*2) # for the alternating position
            for j in range(0, len(factorBase)):
                p = factorBase[j]
                y = f(x+p, n)/p
                if y == 0:
                    factors.append(x) # this never seems to be the case? I am confused


    print factors

def f(x, n):
    return (x+floor(sqrt(n)))**2 - n

def fermat(n):
    return 2 ** (2 ** n) + 1


def fermatFactorization(l, c, methodNum):
    for n in range(5, 8):
        fermatNumber = fermat(n)
        print dixon(fermatNumber, l, c, methodNum)




# Fuer die ganzen tests brauchen die Funktionen lediglich mit den entsprechenden Paramtern aufgerufen werden. Der
# offensichtliche Unterschied zwischen Dixon und rho ist, dass rho lediglich den kleinsten Faktor zurueckgibt. Eine
# gute Wahl fuer L ist exp(0.5*ln(n)*ln(ln(n)))




def eratosthenes(maximum):
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
