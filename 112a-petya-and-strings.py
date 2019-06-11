x, y = input().lower(), input().lower()
ans = int(0)
for i in range(len(x)):
    if(x[i]>y[i]):
        ans = 1
        break
    elif(y[i]>x[i]):
        ans = -1
        break
if (ans>0):
    print(1)
elif (ans<0):
    print(-1)
else: 
    print(0)
    