x = input()
x = ''.join(sorted(x))
x = x.replace("+","")
print(x.replace("", "+")[1:-1])


