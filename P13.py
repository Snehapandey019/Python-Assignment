N = int(input())
i = 1

while True:
    
    if N <= i:
        print("Ramesh")
        break
    N -= i


    if N <= 2 * i:
        print("Suresh")
        break
    N -= 2 * i

    i += 1
