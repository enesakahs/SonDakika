#pip install GoogleNews

from GoogleNews import GoogleNews
gn=GoogleNews() 
gn=GoogleNews(lang='tr',period='7d')
gn.search("Türkiye")
haberler=gn.result()

for i in haberler:
    print("HABER BASLIGI: ", i['title'])
    print("ZAMAN: ", i['date'])
    print("ACIKLAMASI: ", i['desc'])
    print("İLGİLİ HABER LİNKİ: ", i['link'])


