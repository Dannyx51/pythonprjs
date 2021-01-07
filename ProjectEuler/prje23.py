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
  print(i)
  if d(i) > i:
      ab.append(i)

#create list of all possible creations
#computing the numbers themselves takes too long so gonna try something else

outloop = 0
pc = [False for i in range(28124)]
print(len(ab))
for i in ab:
  outloop += 1
  print(outloop)
  for x in ab:
    if (i + x) > 28123:
      break
    pc[i + x] = True

#finding the not possible numbers
np = []
for i in range(1,28124):
  if pc[i] == False:
    np.append(i)

#summate
total = 0
for i in np:
  total += i
print(total)
