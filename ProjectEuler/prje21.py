#sum of amicable numbers under 10000

def d(num):
    x = 0
    for i in range(1,num+1):
        if num % i == 0:
            x += i
    return x - num

total = 0
for i in range(2,10000):
    a = d(i)
    b = d(a)
    if i == b and a != b: 
        total += i

print(total)
