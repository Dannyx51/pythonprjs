from itertools import permutations

#finds primes in a ridiculously slow fashion
#for i in range(12,1000000):
#    for j in lp:
#        if i % j == 0 or i == 1:
#            break
#        if j == lp[len(lp)-1]:
#            lp.append(i)
#            print(i)

#i'll be honest i straight up ripped this from the interwebs but its a sieve of erastothenes (probably misspelt that)
n = 1000000

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

lc = []
for i in lp:
    j = list(permutations(str(i)))
    ap = []
    for k in j:
            t = ""
            for l in k:
                t += l  
            ap.append(int(t))
    z = 0
    for k in ap:
        if lp.count(k) != 0:
            z += 1
        if z == len(ap):
            for h in ap:
                if lc.count(h) == 0:
                    lc.append(h)
        
print(len(lc))