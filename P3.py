
a = int(input("Enter first term (a): "))
d = int(input("Enter common difference (d): "))
n = int(input("Enter number of terms (n): "))


nth_term = a + (n - 1) * d


sum_n = (n / 2) * (2 * a + (n - 1) * d)

print("Nth term =", nth_term)
print("Sum of n terms =", sum_n)
