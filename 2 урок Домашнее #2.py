x = int(input('Input 6 digit number: '))
y = x//1000
z = x % 1000

n1 = y // 100
n2 = y // 10 % 10
n3 = y % 10
n4 = z // 100
n5 = z // 10 % 10
n6 = z % 10

print(n6, n5, n4, n3, n2, n1, sep='')
