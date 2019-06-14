s = input()
x = ['h','e','l','l','o']
i = -1
for c in x:
    i = s.find(c,i+1)
    if i==-1:
        print("NO")
        exit()
print("YES")