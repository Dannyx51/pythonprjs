#find abundant numbers first
#find all numbers that can be made out of them
#invert the list
#summate

def d(num):
    x = 0
    for i in range(1,num+1):
        if num % i == 0:
            x += i
    return x - num

#create list of [ab]undant numbers
ab = []
for i in range(1, 28124):
    if d(i) > i:
        ab.append(i)

#create list of all possible creations
pc = []
for i in ab:
    stop = False
    pc.append(i)
    #while(not stop):
        