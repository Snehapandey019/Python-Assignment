import math

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    gcd = math.gcd(x, y)
    lcm = (x * y) // gcd
    
    print(gcd, lcm)
