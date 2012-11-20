#ich hoffe, diese Funktionen helfen euch dabei, effiziente Algorithmen zu finden, insbesondere fuer den Plotter. Arik

def calcGCD(a, b):
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
    #for j in range(i):
        #print "i = ", j
        #print "r = ", r[j]
        #print "s = ", s[j]
        #print "t = ", t[j]
        #print "q = ", q[j]
        #print "sa + tb = ", s[j]*a + t[j]*b
        #print ""
    # return r, s, t
    return r[i-1]

def naiveGCD(a, b): # naive Faktorisierungsmethode
    factorsA = factor(a)
    factorsB = factor(b)
    aCount = len(factorsA)
    bCount = len(factorsB)
    gcd = 1
    minBIndex = 0
    for aIndex in range(aCount):
        aPair = factorsA[aIndex]
        aBase = aPair[0]
        aExponent = aPair[1]
        for bIndex in range(minBIndex, bCount):
            bPair = factorsB[bIndex]
            bBase = bPair[0]
            bExponent = bPair[1]
            if bBase < aBase:
                continue
            minBIndex = bIndex
            if bBase == aBase:
                gcd = gcd * pow(aBase, min(aExponent, bExponent))
                break
            elif bBase > aBase:
                break
    return gcd

def testGCDPerformance():
    aMinimum = 950
    aMaximum = 1000
    bMinimum = 1000
    bMaximum = 1050
    loopCount = 0
    sageTime = 0
    ownTime = 0
    smartTime = 0
    naiveTime = 0
    for a in range(aMinimum, aMaximum+1):
        for b in range(bMinimum, bMaximum+1):
            print "a, b = ", a, ", ", b
            loopCount = loopCount+1
            sageStart = cputime()
            print "sage: ", gcd(a, b)
            sageEnd = cputime()
            sageTime = sageTime+sageEnd-sageStart
            ownStart = cputime()
            print "own: ", calcGCD(a, b)
            ownEnd = cputime()
            ownTime = ownTime+ownEnd-ownStart
            naiveStart = cputime()
            print "naive: ", naiveGCD(a, b)
            naiveEnd = cputime()
            naiveTime = naiveTime+naiveEnd-naiveStart
            print ""
    sageAverage = sageTime/loopCount
    ownAverage = ownTime/loopCount
    naiveAverage = naiveTime/loopCount
    print "save average: ", sageAverage*1000
    print "own average: ", ownAverage*1000
    print "naive average: ", naiveAverage*1000

    
def fiboExperiment():
    n = 100
    m = 50
    return gcd(fibonacci(n), fibonacci(m)), fibonacci(gcd(n, m))
    
def smartGCD(a, b): #rekrusive Methode
    if a == 1:
        return b
    if b == 1:
        return a
    if a%2 == 0 and b%2 == 0:
        return 2*smartGCD(a/2, b/2)
    if a%2 == 0:
        return smartGCD(a/2, b)
    if b%2 == 0:
        return smartGCD(a, b/2)
    if a > b:
        return smartGCD((a-b)/2, b)
    if b > a:
        return smartGCD((b-a)/2, a)
    return gcd(a, b)

def plot_prime_count(maximum): # plottet pi(n), berechnet es allerdings nur einmal. sehr effizient
    primes = eratosthenes_old(maximum)
    highestPrimeCount = len(primes)
    count = [0]*(maximum+1)
    lastCount = 0
    lastIndex = 0
    for i in range(highestPrimeCount):
        currentPrime = primes[i]
        for j in range(lastIndex, currentPrime):
            count[j] = lastCount
        lastIndex = currentPrime+1
        lastCount = lastCount+1
        count[currentPrime]=lastCount
    for i in range(lastIndex, maximum+1):
        count[i] = lastCount
    return plot_step_function([(i, count[i]) for i in range(maximum)]), plot_step_function([(i, i/ln(i)) for i in range(2, maximum)])

def eratosthenes_old(maximum): # meine jetzige, schnellere Funktion nimmt am Wettbewerb teil, daher moechte ich sie noch nicht veroeffentlichen
    primes = [true]*(maximum+1)
    primes[0] = false
    if(1 < maximum):
        primes[1] = false
    for i in range(maximum+1):
        if i%2 == 0 and i > 2:
            primes[i] = false
    maxSquare = ceil(sqrt(maximum))
    for i in range(3, maxSquare+1):
        if(i%2 == 0):
            continue
        minFactor = i
        maxFactor = ceil(maximum/i)
        for j in range(minFactor, maxFactor+1):
            if i*j <= maximum:
                primes[i*j] = false
    primeArray = []
    for i in range(2, maximum+1):
        isPrime = primes[i]
        if isPrime:
            primeArray.append(i)
    return primeArray