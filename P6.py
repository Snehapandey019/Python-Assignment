def rev(num):
    return int(str(num)[::-1])

t = int(input())
for _ in range(t):
    a, b = input().split()
    ra = rev(a)
    rb = rev(b)
    s = ra + rb
    print(rev(s))
