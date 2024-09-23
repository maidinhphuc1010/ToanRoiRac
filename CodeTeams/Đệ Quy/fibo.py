def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
    

def main():
    n = int(input("Nhập số N chia hết cho 6 và nhỏ hơn 1000: "))
    if n % 6 == 1 or n > 1000:
        print("Nhập lại số N")
    else:
        fib1 = fibonacci(1)
        fib_n3 = fibonacci(n // 3)
        fib_n2 = fibonacci(n // 2)
        fib_n = fibonacci(n)

        print(f"Fibonacci thứ 1: {fib1}")
        print(f"Fibonacci thứ {n//3}: {fib_n3}")
        print(f"Fibonacci thứ {n//2}: {fib_n2}")
        print(f"Fibonacci thứ {n}: {fib_n}")

if __name__ == "__main__":
    main()

