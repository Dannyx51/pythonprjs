
#i'll be honest i straight up ripped this from the interwebs but its a sieve of erastothenes (probably misspelt that)
n = 30

prime = [True for i in range(n+1)] 
p = 2
while (p * p <= n): 
        
    # If prime[p] is not changed, then it is a prime 
    if (prime[p] == True): 
            
        # Update all multiples of p 
        for i in range(p * p, n+1, p): 
            prime[i] = False
    p += 1

lp = []
for i in range(2, len(prime)):
    if prime[i] == True:
        lp.append(i)

print(lp)