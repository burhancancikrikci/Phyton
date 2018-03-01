print("---------------------------------------------------------------")
print("------------------------Hesap Makinesi-------------------------")
sayi1=input("sayi gir : ")
sayi2=input("sayi gir : ")
print("---------------------------------------------------------------")
print("Toplama Islemi(1)")
print("Cikarma Islemi(2)")
print("Bolme   Islemi(3)")
print("Carpma  Islemi(4)")
print("---------------------------------------------------------------")
islem=input("NO : ")
if islem == 1 :
    print("sonuc",sayi1+sayi2)
elif islem==2:
    print("sonuc",sayi1-sayi2)
elif islem==4:
    print("sonuc",sayi1*sayi2)
elif islem==3:
    print("sonuc",sayi1/sayi2)
print("---------------------------------------------------------------")

