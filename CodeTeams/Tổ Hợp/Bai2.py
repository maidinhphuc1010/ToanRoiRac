MOD = 10**9 + 7

def GiaiThua(n, mod):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    return fact

def Mod_NghichDao(x, mod):
    return pow(x, mod - 2, mod)
                                                                                                                                  

def KetHop(n, k, mod):
    if k > n:
        return 0
    fact = GiaiThua(n, mod)
    return fact[n] * Mod_NghichDao(fact[k], mod) % mod * Mod_NghichDao(fact[n - k], mod) % mod

def main():
    
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))
    
    if 0 <= k <= n <= 100:
        result = KetHop(n, k, MOD)
        print(f"Số tổ hợp chập {k} của {n} là: {result}")
    else:
        print("Nhập lại.")

if __name__ == "__main__":
    main()
