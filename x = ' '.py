x = ' '
y = '*'

n = int(input())

for i in range(1, n+1):
    m = n - i
    print(x*m + y*i)
