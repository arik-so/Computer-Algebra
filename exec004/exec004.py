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