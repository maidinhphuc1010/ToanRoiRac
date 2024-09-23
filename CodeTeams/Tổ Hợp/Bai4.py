mod = 10 ** 9 + 7

def XucXac(n, mod):
    dp = [0] * (2 * n + 1)
    dp[0] = 1
    for i in range(1, 2 * n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % mod
    return dp[2 * n]


def main():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    n = a**b
    if n >= 1 and n <= 10**6:
        quay = XucXac(n, mod)
        print(f"Số cách lắc: {quay}")
    else:
        print("Nhập lại")

if __name__ == "__main__":
    main()

