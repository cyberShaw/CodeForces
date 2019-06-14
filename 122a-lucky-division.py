x = int(input())
if(x%4==0 or x%7==0):
    print("YES")
    exit()
else:
    x = str(x)
    for i in x:
        if(i!='7' and i!='4'):
            print("NO")
            exit()
    print("YES")
