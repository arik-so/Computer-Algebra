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

def calcRSAModulus(maxProduct): # als Parameter wird das hoechste n, gegeben, d. h. p * q <= n

    maxFactor = sqrt(maxProduct) # ich bestimme die Wurzel aus dem hoechsten n, um es als den Wert zu haben, in dessen
    # Naehe die beiden Primzahlen liegen muessen.

    variance = maxFactor*0.75 # ich berechne die Umgebung um jenen Wurzelwert, in der ich die beiden Primzahlen suche

    referenceInt = int(round(random()*variance+ maxFactor - variance/2)) # ich lasse zufaellig einen Wert in der
    # Varianz-Umgebung generieren. random() liefert eine zufaellige Kommazahl zwischen 0 und 1. Diese multipliziere ich
    # mit der Groesse der Umgebung, dann habe ich einen Wert zwischen 0 und der Umgebungsgroesse. Dies verschiebe ich
    # dann so, ich einen Wert zwischen dem Wurzelwert - Varianz/2 und Wurzelwert + Varianz/2 habe.
    # Da dies immer noch eine Kommazahl ist, runde ich sie einfach mit round(), was jedoch immer noch eine Kommazahl ist
    # wie 5.0 oder 2.0, weshalb ich sie mit int() zu einem echten Integer konvertiere.

    p = next_prime(referenceInt) # ich lasse mir von Sage die naechste Primzahl nach jener zufaelligen Zahl finden
    q = next_prime(p) # und die danach
    # wohlgemerkt, es ist nicht gegeben, dass p*q <= n sind, aber auf jeden Fall irgendwo in der Naehe, und das reicht mir

    phi = (p-1)*(q-1) # ich berechne die Anzahl der zu p*q teilerfremden Zahlen. Weil p, q Primzahlen sind, gilt:
    # phi(n) = (p-q)*(q-1)

    n = p*q # ich berechne n

    e = 4 # e ist nicht wirklich 4. Es soll teilerfremd zu phi(n) sein, das ist am einfachsten mit Primzahlen zu
    # erreichen. Ich lasse es einfach bei 4, einer Nicht-Primzahl, starten, und in der Schleife erklaere ich weiter

    d = 0 # ich lege d einfach nur fest, damit es schon ausserhalb der Schleife festgelegt ist;
    # d ist das Modulo-inverse von e mit dem Modulus n

    while true: # diese Schleife laeuft so lange, bis die wichtigen Bedingungen erfuellt sind, naemlich:
        e = next_prime(e)
        if gcd(e, phi) == 1: # e soll teilerfremd zu phi(n) sein, und mindestens 5. Deshalb startete es bei 4
            d = inv(e, phi)
            if d > 0: # und d soll groesser als 0 sein, weil dies als Exponente verwendet wird
                break
    print '\n\n p =', p, '\n\n q =', q, '\n\n phi =', phi, '\n\n e =', e, '\n\n d =', d

    m = int(random()*500000+500000) # hier ist einfach nur ein Beispiel, das berechnet wird. C ist eine Nachricht, sie
    #wird zufaellig generiert

    c = pow(n, m, e) # c ist die verschluesselte Nachricht, c = m^e mod n
    m2 = pow(n, c, d) # m' ist die aus c entschluesselte Nachricht, mit m' = c^d mod n
    print '\n\nExample:'
    print '\nSei m =', m
    print '\nc = m^e (mod n) =', c
    print '\nm\' = c^d (mod n) =', m2, '\n'

    # return p, q, n