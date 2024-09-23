MOD = 10**9 + 7

def ToiUuHoa(n, k, mod):
    result = 1
    for i in range(n, n - k, -1):
        result = (result * i) % mod
    return result

def main():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    n = a ** b
    k = int(input("Nhập số k: "))
    if k <= 0 or k >= n or n > 10**9:
       print("Nhap Lai")
    else:
        p = ToiUuHoa(n, k, MOD)
        print(f"Chỉnh hợp lặp chập k của n là: {p}")

if __name__ == "__main__":
    main()