def ThapHaNoi(Coc1, Coc2):
    a = {"A", "B", "C"}
    return (a - {Coc1, Coc2}).pop()
    
def ThapDiChuyen(SoTam, CocGoc, CocDich):
    if SoTam == 1:
        print(CocGoc + " -> " + CocDich)
    else:
        CocTrungGian = ThapHaNoi(CocGoc, CocDich)
        ThapDiChuyen(SoTam - 1, CocGoc, CocTrungGian)
        ThapDiChuyen(1, CocGoc, CocDich)
        ThapDiChuyen(SoTam - 1, CocTrungGian, CocDich)

n = int(input("Nhập số tấm: "))
ThapDiChuyen(n, "A", "C")