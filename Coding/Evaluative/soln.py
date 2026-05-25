# take in the number
coef = input()
coef = coef.split()
a = [int(a) for a in coef]

x = input()
x = int(x)

poly = 0
for i in range(0,len(a)):

    term = a[i]*pow(x,i)
    poly+=term


# print answer
print(poly)
