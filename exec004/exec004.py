__author__ = 'ariksosman'

def pseudoRandom(maximum):
    lastRandomNumber = ''
    lastRandomFileReadingHandle = open('lastRandom.txt', 'r') # get last random number
    for line in lastRandomFileReadingHandle:
        lastRandomNumber = lastRandomNumber + line # append read content to random number
    if lastRandomNumber == '':
        lastRandomNumber = (int)(random()*maximum) # there was no last random number, so let's initialize
    else:
        lastRandomNumber = int(lastRandomNumber) # there was one, converting it from string to int

    b = (int)(random()*maximum) # creating a new random number
    a = 0
    while(gcd(a, b) != 1):
        a = (int)(random()*b) # finding an a that is coprime to b


    newRandomNumber = (a*lastRandomNumber+b) % maximum # creating the new random number

    lastRandomFile = open('lastRandom.txt', 'w') # saving that new random number
    lastRandomFile.write(str(newRandomNumber)) # int needs to be converted to string
    lastRandomFile.close() # saving

    return newRandomNumber

def fermatTest(allegedPrime, testCount):
    for i in range(testCount):
        a = (int)((random()*(allegedPrime-2))+1) # we generate an a satisfying 1 <= a < allegedPrime
        indicator = pow(allegedPrime, a, allegedPrime-1)
        isPrime = (gcd(indicator, allegedPrime) == 1)
        if(isPrime == false):
            return false
    return true

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
