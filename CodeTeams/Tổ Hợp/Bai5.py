mod = 10 ** 9 + 7

def ModKetHop(n, k, mod):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], mod - 2, mod) 
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def SoNghiem(n, m, Y, mod):
    m -= sum(Y)
    if m < 0:
        return 0 
    return ModKetHop(m + n - 1, n - 1, mod) 

def main():
    n = int(input("Nhập n: "))
    m = int(input("Nhập m: "))
    y = list(map(int, input(f"Nhập {n} giá trị của danh sách Y, cách nhau bởi dấu cách: ").split()))
    
    if 1 <= n <= 100 and 1 <= m <= 100 and len(y) == n and sum(y) <= m:
        GiaiPhap = SoNghiem(n, m, y, mod)
        print(f"Số nghiệm là: {GiaiPhap}")
    else:
        print("Nhập lại.")

if __name__ == "__main__":
    main()