class PersegiPanjang:

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
     return f"Persegi Panjang dengan panjang {self.panjang} dan lebar {self.lebar}"


panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

if panjang == 0 or lebar == 0:
    print("Panjang dan lebar tidak boleh nol.")
else:
    pp = PersegiPanjang(panjang, lebar)
    print(f"Keliling: {pp.keliling()} cm")
    print(f"Luas: {pp.luas()} cm²")
