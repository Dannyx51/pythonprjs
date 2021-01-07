#ok this one's tough so lets break it down danno
#"123456789" needs to be permutated, so we can import permutations from itertools
from itertools import permutations
#next, the type of sets we are looking for is "123x456=789"
#9 digits total, so we can thing about it as a way to look for products
#in a "2x3=4" or a "3x2=4" scenario, bc nothing else will work
#number to find == 45228


s = list(permutations("123456789"))
l = []
for p in s:
    n1 = int(p[0] + p[1])
    n2 = int(p[2] + p[3] + p[4])
    n3 = int(p[5] + p[6] + p[7] + p[8])
    if n2 * n1 == n3 and l.count(n3) == 0:
        l.append(n3)
    
print(l)
total = 0
for i in l:
    total+=i
print(total)