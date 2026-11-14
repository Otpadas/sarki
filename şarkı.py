nota = str(input("4 notalık bir beste dilimi giriniz: (Örnek: Do-Re-Mi-Fa)")).lower().split("-")

if len(nota) != 4:
    print("4 adet nota girmeniz gerekmekte.")
    exit()

if nota[0] == nota[3]:
    print("İlk nota ile son nota aynı. Armoni çakışması.")
    exit()

bpm = int(input("Şarkı temposunu BPM(Beats Per Minute) cinsinden giriniz:"))

min_hz = 200 / (1 + bpm / 100)
max_hz = 800 / (1 + bpm / 100)

print(f"Doğru frekans değerleri için {min_hz} ile {max_hz} arasında bir değeri seçiniz.")
hz = float(input("Baz frekans değerini giriniz:"))

sure = 60 / bpm 
pikhz = hz * (1 + bpm / 100)

if pikhz > 800:
    print(f"Kulak tırmalayıcı frekans 800'den fazla olamaz sizinki {pikhz:.2f} oldu")
    exit()

if pikhz < 200:
    print(f"Ses duyulmuyor 200'den fazla olması önerilir sizinki {pikhz:.2f} oldu")
    exit()

tur = ""

if hz * 3 < 120:
    if nota[0] not in ["re", "la"]:
        soru = str(input("Şuanki girişlerine göre size bir tek pop türünde şarkı yapabiliriz onaylıyor musunuz? (Evet/Hayır)")).lower()
        if soru == "evet":
            print("Tamamdır.")
            tur = "POP"
        elif soru == "hayır":
            print("Kapattım.")
            exit()
        else:
            print("Hatalı giriş.")
            exit()
    else:
        tur = str(input("Müzik türü seçiniz: (Rock/Pop)")).upper()
        if tur not in ["ROCK", "POP"]:
            print("Hatalı giriş yaptınız.")
            exit()

if hz * 3 >= 120:
    if nota[0] not in ["re", "la"]:
        tur = str(input("Müzik türünü giriniz: (Edm/Pop)")).upper()
        if tur == "EDM":
            print("Tamamdır.")
        elif tur == "POP":
            print("Tamamdır.")
        else:
            print("Hatalı giriş.")
            exit()
    else:
        tur = str(input("Müzik türü seçiniz: (Edm/Rock/Pop)")).upper()
        if tur not in ["ROCK", "EDM", "POP"]:
            print("Hatalı giriş yaptınız.")
            exit()

if tur == "EDM":
    bas = hz * 3
elif tur == "ROCK":
    bas = hz * 1.5
else:
    bas = hz

print("-" * 25)
print(f"Tür:\t{tur}\nBeste Notası:\t{nota}\nVuruş Süresi:\t{sure:.2f} sn\nPik Frekansı:\t{pikhz:.2f} Hz\nNet Bas Gücü:\t{bas:.2f}")

