def ThapHaNoi(Coc1, Coc2):
    a = {"A", "B", "C"}
    return (a - {Coc1, Coc2}).pop()
    
def DiChuyen(SoTam, CocNguon, CocToi):
    if SoTam == 1:
        print(CocNguon + " -> " + CocToi)
    else:
        CocTrungGian = ThapHaNoi(CocNguon, CocToi)
        DiChuyen(SoTam - 1, CocNguon, CocTrungGian)
        DiChuyen(1, CocNguon, CocToi)
        DiChuyen(SoTam - 1, CocTrungGian, CocToi)


def main():
    n = int(input("Nhập số đĩa n: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương n.")
        return
    
    print(f"\nGiải bài toán tháp Hà Nội với {n} đĩa:")
    Cac_Buoc = DiChuyen(n, 'A', 'C')

    Tong_So_Buoc = 2**n - 1
    print(f"\nTổng số bước di chuyển là: {Tong_So_Buoc}")

if __name__ == "__main__":
    main()