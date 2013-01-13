def pollardRhoMethod(n):
    if(n%2 == 0):
        return 2
    x = 2
    y = 2
    d = 1
    i = 0
    while (d==1):
        i = i+1
        # print 'x =',x,'\ny =',y,'\nd =',d,'\n'
        x = (x**2 + 1) % n
        y = ((y**2 + 1)**2 + 1) % n
        d = gcd(abs(x-y), n)
    # print 'x =',x,'\ny =',y,'\nd =',d,'\n'
    print 'i =',i
    if (d == n):
        print 'Failure'
        return false
    if (1<d and d < n):
        return d

def fermatFactorization():
    for n in range(5, 13):
        fermatNumber = 2 ** (2 ** n) + 1
        # print fermatNumber
        print pollardRhoMethod(fermatNumber)