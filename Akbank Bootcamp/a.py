class Library:
    def __init__(self):
        self.dosya = open("books.txt", "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.read().splitlines()
        for kitap in kitaplar:
            bilgiler = kitap.split(',')
            print(f"Kitap Adı: {bilgiler[0]}, Yazar: {bilgiler[1]} Yayın Yılı: {bilgiler[2]} Sayfa Sayisi: {bilgiler[3]}")
        

    # def kitap_ekle(self):
    #     ad = input("Kitap adını giriniz: ")
    #     yazar = input("Yazar adını giriniz: ")
    #     yil = input("Yayın yılını giriniz: ")
    #     sayfa = input("Sayfa sayısını giriniz: ")
    #     bilgi = f"\n {ad},{yazar},{yil},{sayfa}"
    #     self.dosya.write(bilgi)
    #     print("Kitap başarıyla eklendi.")
   
    def kitap_ekle(self, kitap_adi):
        with open("books.txt", "a") as file:
            file.write(kitap_adi + "\n")

    def kitap_sil(self, silinecek_kitap):
        with open("books.txt", "r") as file:
            lines = file.readlines()
        with open("books.txt", "w") as file:
            for line in lines:
                if line.strip() != silinecek_kitap:
                    file.write(line)


    # def kitap_sil(self):
    #     silinecek_ad = input("Silmek istediğiniz kitabın adını giriniz: ")
    #     self.dosya.seek(0)
    #     kitaplar = self.dosya.readlines()
    #     yeni_kitaplar = []
    #     for kitap in kitaplar:
    #         bilgiler = kitap.strip().split(',')
    #         if bilgiler[0] != silinecek_ad:
    #             yeni_kitaplar.append(kitap)
    #     self.dosya.seek(0)
    #     self.dosya.truncate()
    #     for kitap in yeni_kitaplar:
    #         self.dosya.write(kitap)

lib = Library()

print("*** MENÜ ***")
print("1) Kitapları Listele")
print("2) Kitap Ekle")
print("3) Kitap Sil")
print("4)Programı sonlandır")

secim = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3/4): ")

if secim == "1":
    lib.kitaplari_listele()
elif secim == "2":
    lib.kitap_ekle()
elif secim == "3":
    lib.kitap_sil()
elif secim == "4":
     print("Program sonlandı.")
else:
    print("Geçersiz giriş! Lütfen sadece 1, 2 veya 3 girin.")
