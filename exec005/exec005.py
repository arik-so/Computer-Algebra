def pollardRhoMethod(n, cycleDetection):
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
    if (d == n and cycleDetection):
        print 'Failure'
        return false
    if (1<d and d < n):
        return d

def fermatFactorization():
    for n in range(5, 7): # ueber 6 als Maximalzahl laeuft der Test zumindest auf meinem Computer zu langsam, deswegen
                            # kann ich es derzeit nicht ganz ausfuehren. Muss ab 7 eine andere als die Rho-Methode
                            # ausgefuehrt werden? Vorerst schicke ich meinen Code in seinem jetzigen Zustand ab, bitte
                            # um Rueckmeldung
        fermatNumber = 2 ** (2 ** n) + 1
        # print fermatNumber
        print pollardRhoMethod(fermatNumber, true)