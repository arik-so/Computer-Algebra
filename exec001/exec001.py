__author__ = 'ariksosman'

def factorial_iterative_for(number): #fak1
    factorial = 1
    for i in range(2, number+1): # for some reason, number is not included in range
        factorial = factorial*i
    return factorial

def factorial_iterative_while(number): #fak2
    factorial = 1
    i = 2
    while i <= number:
        factorial = factorial*i
        i = i+1
    return factorial

def factorial_recursive(number): #fak3
    if number > 2:
        return number*factorial_recursive(number-1);
    return number;

def default_factorial_test(): # Aufgabe 1.2 a)
    print "Needs to be:"
    print 2*3*4*5*6
    for i in range(1, 7):
        print "Testing for: "
        print i
        print "Result:"
        print factorial(i)

# Aufgabe 1.2 c); die rekursive Funktion gibt schnell den Geist auf
def advanced_factorial_test():
    for i in range(1, 1001):
        print ""
        print "Testing for: ", i
        print "Result default: ", factorial(i)
        print "Result iterative, for-loop: ", factorial_iterative_for(i)
        print "Result iterative, while-loop: ", factorial_iterative_while(i)
        print "Result recursive: ", factorial_recursive(i)

#Aufgabe 1.3
def performance_test():
    for k in range(1, 6):
        for l in range(3, 6):
            print "k, l = "
            print k
            print l
            print "Time: (addition, multiplication)"
            timeBefore = cputime()
            x = 10 ^ (k * (10 ^ l))
            timeAfterProcessing = cputime()
            addition = x+x
            timeAfterAdding = cputime()
            product = x*x
            timeAfterMultiplying = cputime()
            timeForAdding = timeAfterAdding-timeAfterProcessing
            timeForMultiplying = timeAfterMultiplying-timeAfterAdding
            print timeAfterAdding
            print timeAfterAdding
            print ""
