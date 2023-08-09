c1 = input()
c2 = input()
c3 = input()

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
m = 10**(color.index(c3))
r = int(str(color.index(c1))+str(color.index(c2)))*m
print(r)