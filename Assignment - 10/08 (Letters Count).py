def saydir(metin):
    metinKücült = metin.lower()
    harfler = set("abcçdefgğhiıjklmnoöprsştuüvyzxwq")
    rakamlar = set("0123456789")
    karakterler = set("é^#><$½&/=)(=?_-|/*-+!")
    bosSozluk = dict()
   
    for i in metinKücült :
        if i in harfler:
            toplamHarf = list(metinKücült).count(i)
            bosSozluk[i] = toplamHarf
        elif i in rakamlar :
            toplamRakam = list(metinKücült).count(i)
            bosSozluk[i] = toplamRakam
        elif i in karakterler :
            toplamKarakter = list(metinKücült).count(i)
            bosSozluk[i] = toplamKarakter
            
    return bosSozluk