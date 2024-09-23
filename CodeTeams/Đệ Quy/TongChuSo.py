def SoChuSo(n):
    if n == 0:
        return 0
    return 1 + SoChuSo(n // 10)

def Tong(n):
     if n == 0:
         return 0
     return n % 10 + Tong(n // 10)

n = int(input("Nhập số dãy n: "))

TongSoChuSo = SoChuSo(n)
TongSo = Tong(n)

print(f"Tổng số chữ số của dãy số là: {TongSoChuSo} ")
print(f"Tổng của dãy số: {TongSo}")