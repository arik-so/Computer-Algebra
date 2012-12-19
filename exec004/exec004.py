__author__ = 'ariksosman'

def pseudoRandom(maximum, a, b, firstX):

    if b >= maximum:
        print 'b >= maximum'
        return false

    if a >= maximum:
        print 'a >= maximum'

    if gcd(a, b) != 1:
        print 'a not coprime to b'
        return false

    lastMaximum = ''
    lastNFileReadingHandle = open('lastMaximum.txt', 'r') # get last random number
    for line in lastNFileReadingHandle:
        lastMaximum = lastMaximum + line # append read content to random number
    if lastMaximum != '':
        lastMaximum = (int)(lastMaximum) # there was one, converting it from string to int

    lastRandomNumber = firstX
    if lastMaximum == maximum: # only then can previous values be used
        lastRandomNumber = ''
        lastRandomFileReadingHandle = open('lastRandom.txt', 'r') # get last random number
        for line in lastRandomFileReadingHandle:
            lastRandomNumber = lastRandomNumber + line # append read content to random number
        if lastRandomNumber == '':
            lastRandomNumber = firstX # there was no last random number, so let's initialize
        else:
            lastRandomNumber = int(lastRandomNumber) # there was one, converting it from string to int

    if lastRandomNumber >= maximum:
        print 'firstX >= maximum'
        return false

    newRandomNumber = (a*lastRandomNumber+b) % maximum # creating the new random number

    lastRandomFile = open('lastRandom.txt', 'w') # saving that new random number
    lastRandomFile.write(str(newRandomNumber)) # int needs to be converted to string
    lastRandomFile.close() # saving

    lastNFile = open('lastMaximum.txt', 'w') # saving that new random number
    lastNFile.write(str(maximum)) # int needs to be converted to string
    lastNFile.close() # saving

    return newRandomNumber

def calculateFermatWitnesses(e):

    f = 2**(2**e) + 1

    witnesses = []

    a = 1
    while true:
        a = a+1
        if a > 250:
            break
        remainder = gcd(pow(f, a, f-1), f)
        if remainder != 1:
            witnesses.append(a)

    return witnesses

def fermatTest(allegedPrime, testCount):

    for i in range(testCount): # simply repeating the process

        a = (int)((random()*(allegedPrime-2))+1) # we generate an a satisfying 1 < a < allegedPrime

        if gcd(pow(allegedPrime, a, allegedPrime-1), allegedPrime) != 1:
            return false # one indicator of inpramility suffices

    return true

def executeMultipleFermatTests(poolSize):

    probablePrimes = []
    wrongPrimes = []

    for i in range(poolSize):
        n = (int)(random()*(10**6) + 10*(10**6))
        print '\nCurrent number:',n
        for k in range(1, 11):
            error = 1.0/(2.0**k)
            trials = (int)((1.0-error)*(n-1)) # number of necessary counts for correct probability
            isProbablyPrime = fermatTest(n, trials)
            if isProbablyPrime:
                print 'Current error:',error,'trueish'
                probablePrimes.append(n)
                if is_prime(n) == false:
                    wrongPrimes.append(n)
            else:
                print 'Current error:',error,'false'
                break

    return probablePrimes, wrongPrimes

def millerRabinTest(allegedPrime, trials):

    for i in range(trials):

        if allegedPrime%2==0:
            return false

        a = (int)((random()*(allegedPrime-2))+2) # we generate an a satisfying 1 < a < allegedPrime

        multipleOfTwo = allegedPrime-1
        factors = factor(multipleOfTwo)

        j = factors[0][1]
        d = multipleOfTwo/(2**j)

        print 'n-1 = d * 2 ^ j =',d,'*','2 ^',j,'=',multipleOfTwo

        simplePower = gcd(pow(allegedPrime, a, d), allegedPrime)

        print 'a ^ d mod n =',a,'^',d,'mod',allegedPrime,'=',simplePower

        if simplePower==1:
            continue

        for r in range(0, j+1):
            if gcd(pow(allegedPrime, a, d*(2**r)), allegedPrime) == -1:
                print 'here'
                break

        return false

def executeMultipleRabinTests(poolSize):

    probablePrimes = []
    wrongPrimes = []

    for i in range(poolSize):
        n = (int)(random()*(10**6) + 10*(10**6))
        print '\nCurrent number:',n
        for k in range(1, 11):
            error = 1.0/(2.0**k)
            trials = (int)((1.0-error)*(n-1)) # number of necessary counts for correct probability
            isProbablyPrime = fermatTest(n, trials)
            if isProbablyPrime:
                print 'Current error:',error,'trueish'
                probablePrimes.append(n)
                if is_prime(n) == false:
                    wrongPrimes.append(n)
            else:
                print 'Current error:',error,'false'
                break

    return probablePrimes, wrongPrimes

# old functions

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

def pow(modulus, base, exponent):
    necessaryFactors = []
    currentExponent = exponent
    currentBase = base
    while true:
        currentBase = currentBase % modulus
        if currentExponent == 1:
            break
        if currentExponent%2 == 1:
            necessaryFactors.append(currentBase)
        currentExponent = floor(currentExponent/2)
        currentBase = currentBase*currentBase
    result = currentBase
    for currentFactor in necessaryFactors:
        result = result*currentFactor
    return result%modulus
