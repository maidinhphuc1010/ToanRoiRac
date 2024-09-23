
def main():
    
    n = int(input("Nhập số n: "))
    k = int(input("Nhập số k: "))
    primes = list(map(int, input(f"Nhập {k} số nguyên tố khác nhau, cách nhau bởi dấu cách: ").split()))
    
    if 1 <= n <= 10**12 and 1 <= k <= 10 and len(primes) == k:
        divisible_count = count_divisible(n, primes)
        result = n - divisible_count 
        print(f"Số các số không chia hết cho bất kỳ số nguyên tố nào là: {result}")
    else:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
