x = int(input('Input 4 digit number: '))

n1 = x //1000
n2 = x %10
n3 = (x%100)//10
n4 = (x//100)%10

print(n1)
print(n4)
print(n3)
print(n2)
