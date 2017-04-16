def verifyPrimeNumber(number):
    numbers = number.split(' ')
    s = int(numbers[0])
    e = int(numbers[1])
    
    primes=[]
    
    for n in xrange(s+1, e):
        for x in xrange(2, n):
            if not n % x:
                break
        else:
            primes.append(n)
    
    for prime in primes:
        print prime
        
    print ''

def testeCase(amount):
    for i in xrange(amount):
        verifyPrimeNumber(raw_input())
    
testeCase(int(raw_input()))
