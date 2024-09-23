def ToHop(n, k):
    if k == 0 or n == 0:
        return 1
    return ToHop(n - 1, k - 1) + ToHop(n - 1, k)

n = int(input("Nhập số n: "))
k = int(input("Nhập số k:"))

C = ToHop(n, k)

print(f"Tổ hợp chập {k} của {n} là: {C}")