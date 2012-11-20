__author__ = 'ariksosman'

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