import random
enKucukDeger=1
enBuyukDeger=100
while True:
  print("{}-{}".format(enKucukDeger,enBuyukDeger))
  bilgisayarinTahmini=random.randint(enKucukDeger,enBuyukDeger)

  cevap=input("{} tuttuğun sayı olabilir mi? [e]vet / daha [b]üyük / daha [k]üçük".format(bilgisayarinTahmini))

  if cevap=="e":
    print("Oley bildim!!")
    break
  elif cevap=="b":
    enKucukDeger=bilgisayarinTahmini+1
  else:
    enBuyukDeger=bilgisayarinTahmini-1