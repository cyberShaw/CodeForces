n = int(input())
x = list(map(int, input().split(' ')))
x = sorted(x,reverse=True)
total = sum(x)
sum = int(0)
for i in range(n):
    sum+=x[i]
    if(sum>(total-sum)):
        print(i+1)
        break