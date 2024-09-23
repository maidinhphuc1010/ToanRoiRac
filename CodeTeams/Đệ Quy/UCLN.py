def ucln(m, n):
    if n == 0:
        return m
    return ucln(n, m % n)

m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

uc = ucln(m, n)
print(f"Ước chung lớn nhất của {m} và {n} là: {uc}") 
