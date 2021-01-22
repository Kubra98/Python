import random

bilgisayarinTuttuguSayi=random.randint(1,100)
denemeSayiyi=0
#print(bilgisayarinTuttuguSayi)
while True:
  denemeSayiyi+=1
  benimTahminEttigimSayi=int(input("Tuttuğum sayıyı tahmin et:"))
  if benimTahminEttigimSayi==bilgisayarinTuttuguSayi:
    print("Tebrik ederim {} denemede bildin !!".format(denemeSayiyi))
    break
  elif bilgisayarinTuttuguSayi>benimTahminEttigimSayi:
    print("Daha büyük sayı dene")
  else:
    print("Daha küçük sayı dene")