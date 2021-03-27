from functools import reduce

reached = set([0,1])
class Tree:
    global reached
    def __init__(self, value, children = []):
        reached.add(value)
        self.value = value
        self.children = children

    def __str__(self, x = 0, level = 0):
        tl = 1 if level > 0 else 0
        
        if not x:
            sep = '\u251C\u2500 '
        else:
          sep = '\u2514\u2500 '

        ret = sep*tl+repr(self.value)+"\n"

        for x in range(len(self.children)):
            ret += f"   "*(level) + self.children[x].__str__(x == len(self.children) - 1,level+1)

        return ret

    def __repr__(self):
        return f"<tree object, v = {self.value}, numChildren = {len(self.children)}>"
    
    def expand(self, level = 0):
        self.children = self.retChild(self)
        if level >= 0:
            for x in range(len(self.children)):
                self.children[x].expand(level-1)
    
    def retChild(self,root) -> list:
        v = root.value
        a = v * 2
        b = (v - 1) // 3 if (v-1) % 3 == 0 else None
        b = None if b in [0,1] else b
        
        ret = [Tree(x) for x in [a,b] if x != None and x not in reached]

        return ret

trunk = Tree(2)
trunk.expand(30)

# Making a whole lot of list and string garbage to insert bars for proper trees
l = trunk.__str__()

l = l.split('\n')
for x in range(len(l)):
    l[x] = [i for i in l[x]]

for i in range(len(l)):
    for x in range(len(l[i])):
        if l[i][x] == '\u251C':
            y = i+1
            while y < len(l):
                if l[y][x] != '\u2514':
                    l[y][x] = '\u2506'
                else: break
                y += 1

for i in range(len(l)):
    l[i] = "".join(l[i])

print(*l, sep = '\n')