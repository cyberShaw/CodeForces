n = int(input())
s = []
for i in range(n):
    s.append(input())
for st in s[0:]:
    if(len(st)>10):
        print(st[0]+str(len(st)-2)+st[-1])
    else:
        print(st)