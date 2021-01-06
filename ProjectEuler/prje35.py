from itertools import permutations

#finds primes in a ridiculously slow fashion
#for i in range(12,1000000):
#    for j in lp:
#        if i % j == 0 or i == 1:
#            break
#        if j == lp[len(lp)-1]:
#            lp.append(i)
#            print(i)

#using sieve of eratosthenes to find primes
lp = []
for i in range(2,1000000):
    lp.append(i)

for i in range(490475):
    print(i)
    if lp[i] % 2 == 0: 
        lp.pop(i)
        i -= 1
    if lp[i] % 3 == 0: 
        lp.pop(i)
        i -= 1
    if lp[i] % 5 == 0: 
        lp.pop(i)
        i -= 1
    if lp[i] % 7 == 0: 
        lp.pop(i)
        i -= 1

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