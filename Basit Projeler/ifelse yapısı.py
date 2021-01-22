while True:
    print( "Matematik  (1)" )
    print( "Fizik  (2)" )
    print( "Kimya (3)" )
    print( "Biyoloji (4)" )
    print( "Geometri  (5)" )
    print( "Türk dili ve edebiyatı (6)" )

    dersadı = input( "Hangi dersi almak istiyorsunuz: " )
    isim = input( "İsminiz " )

    if dersadı == "Matematik" or dersadı == "m" or dersadı == "M":
        print( "Matematik dersine hoşgeldin", isim )
        break


    elif dersadı == "Fizik" or dersadı == "f" or dersadı == "F":
        print( "Fizik dersine hoşgeldin", isim )
        break


    elif dersadı == "Kimya" or dersadı == "K" or dersadı == "k":
        print( "Kimya dersine hoşgeldin", isim )
        break


    elif dersadı == "Biyoloji" or dersadı == "B" or dersadı == "b":
        print( "Biyoloji dersine hoşgeldin", isim )
        break

    elif dersadı == "Geometri" or dersadı == "G" or dersadı == "g":
        print( "Geometri dersine hoşgeldin", isim )
        break

    elif dersadı == "Türk dili ve edebiyatı " or dersadı == "T" or dersadı == "t" or dersadı == "E" or dersadı == "e":
        print( "Türk dili ve edebiyatı dersine hoşgeldin", isim )
        break

    else:
        print( "Yanlış ders adı girdiniz.Lütfen şartlara uyan bir ders adı giriniz." )
        break