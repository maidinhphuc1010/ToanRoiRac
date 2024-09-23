mod = 10 ** 9 + 7
def SoMatThuTu(n, mod):
    if n == 1:
        return 0
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % mod
    return dp[n]

def  main():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    n = a**b 
    if n >= 1 and n <= 10**6:
        d = SoMatThuTu(n, mod)
        print(f"Số mất thứ tự là {d}")
    else:
        print("Nhập lại")


if __name__ == "__main__":
    main()
