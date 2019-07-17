n = int(input())
pn = []
o = ''
pn = list(map(int, input().split()))
for i in range(0,len(pn)):
    l = pn.index(i+1) + 1
    o += str(l) + ' '
print(str(o))