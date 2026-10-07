# -*- coding: utf-8 -*-
"""
kocaelitikaligideracma.com veri katmanı.

⛔ Üretilen HTML'i ELLE DÜZENLEME — build.py her çalıştığında üzerine yazar.
   Değişiklik BURAYA yapılır, sonra:  python3 _src/build.py && python3 _src/denetim.py
"""

# ── Firma ───────────────────────────────────────────────────────────────────
# Kullanıcı 2026-10-05'te verdi. ⛔ Uydurma bilgi ekleme.
SITE = {
    "marka":      "Kocaeli Tıkalı Gider Açma",
    "alan":       "https://kocaelitikaligideracma.com",
    "cname":      "kocaelitikaligideracma.com",
    "tel_goster": "0535 815 18 04",
    "tel_link":   "+905358151804",
    "wa":         "905358151804",
    "adres":      "Kılıçarslan Mah. Hürriyet Cad. No:1, Başiskele / Kocaeli",
    "adres_sema": {"streetAddress": "Kılıçarslan Mah. Hürriyet Cad. No:1", "addressLocality": "Başiskele",
                   "addressRegion": "Kocaeli", "addressCountry": "TR"},
    # "acik" | "koyu" — hero ve başlık çubuğunun teması (2026-10-05: kullanıcı "heroyu da açık yap bakalım" dedi)
    "hero_tema":  "koyu",
    "harita":     "https://www.google.com/maps/search/?api=1&query=K%C4%B1l%C4%B1%C3%A7arslan+Mah.+H%C3%BCrriyet+Cad.+No%3A1+Ba%C5%9Fiskele+Kocaeli",
}

# Google Ads — boşken etiket basılmaz, tıklama dinleyicisi hiçbir şey göndermez.
ADS = {"etiket": "AW-18498023870", "tel": "", "wa": ""}

# ✅ ONAYLI — kullanıcı 2026-10-05'te seçti ("Teyitli") + aynı gün verdiği tanıtım metninden:
ONAYLI = ["7/24 hizmet", "ortalama 30 dakikada ulaşım", "kırmadan kameralı tespit", "fiyat işe başlamadan söylenir",
          "sorun giderilmeden ücret alınmaz, ödeme iş bitince", "yılların tecrübesi", "Başiskele ofisi ziyaret edilebilir"]
# ⚠️ Kullanıcının metninde "Hizmetlerimiz garantili" var ama garanti SÜRESİ/KAPSAMI verilmedi → Ticari Reklam Yönetmeliği
#    garanti ifadesinde kapsam ister. Kapsam gelene kadar "garantili" YAZILMIYOR (TEYITSIZ'de), yerine "sorun giderilmeden ücret almıyoruz".

# ⛔ Referans tasarımlarda vardı, kullanıcı TEYİT ETMEDİ → denetim HATA verir.
TEYITSIZ = ["%100", "5000+", "mutlu müşteri", "garanti veriyoruz", "garantili", "lisanslı", "sigortalı",
            "yıllık deneyim", "yıllık tecrübe", "robot"]

# ⛔ Üstünlük iddiası (Ticari Reklam Yönetmeliği ispat ister) → denetim HATA.
YASAK_IDDIA = ["en iyi", "en ucuz", "lider", "bir numara", "1 numara", "rakipsiz", "en kaliteli", "en hızlı"]


# ── Türkçe ek tablosu ───────────────────────────────────────────────────────
# ⛔ Kodda "{ad}'da" gibi elle ek YAZMA → build.ek(i, "loc|dat|gen|abl")
#                 loc(-de)  dat(-e)  gen(-in)  abl(-den)
ILCE_EK = {
    "izmit":      ("'te",  "'e",   "'in",   "'ten"),
    "basiskele":  ("'de",  "'ye",  "'nin",  "'den"),
    "golcuk":     ("'te",  "'e",   "'ün",   "'ten"),
    "derince":    ("'de",  "'ye",  "'nin",  "'den"),
    "korfez":     ("'de",  "'e",   "'in",   "'den"),
    "kartepe":    ("'de",  "'ye",  "'nin",  "'den"),
    "karamursel": ("'de",  "'e",   "'in",   "'den"),
}


# ── İlçeler (kullanıcının seçtiği 7 ilçe) ───────────────────────────────────
# Metin bu alanlardan türetilir; ilçe adını değiştirip kopya üretmek DEĞİL.
#   yapi  : yapı stoğu          gider : daire içi gider/kolon karakteri
#   rogar : bahçe/bina dışı hat ve rögar   saha : ekibin sahada dikkat ettiği şey
#   mahalle: banner'lardaki ve bilinen mahalleler — ⛔ sayfa AÇILMAZ, sadece metinde geçer
#   banner : kullanıcının ilçe görseli (yoksa saha fotoğrafı)
# ⚠️ Gölcük banner'ındaki "Topçular Mah." Gölcük'e ait değil → listeye alınmadı.
ILCELER = [
 {"ad":"İzmit","slug":"izmit","komsu":["derince","kartepe","basiskele"],
  "banner":"izmit-gider-acma-servis-numarasi",
  "mahalle":["Yahyakaptan","Alikahya","Kuruçeşme","Yenişehir","Gültepe","Tavşantepe","Ömerağa","Cedit"],
  "yapi":"İzmit'te Ömerağa, Cedit ve Kozluk gibi eski merkez mahallelerinde dar sokaklara dizilmiş eski apartmanlar var; Yahyakaptan, Alikahya ve Kuruçeşme tarafında ise 1999 depreminden sonra yapılmış site ve bloklar çoğunlukta.",
  "gider":"Körfeze bakan yamaçlara kurulan binalarda düşey kolonlar uzun ve dik iniyor; eski binalarda kolonun yatay hatta döndüğü dirsekte yağ ve tortu birikip alt katlardan geri tepme başlıyor.",
  "rogar":"Eski bahçeli apartmanlarda bina rögarı ile sokak hattı arasındaki borular yaşlı; çatlak ve ek yerlerinden giren ağaç kökleri rögarın sürekli dolmasının en sık sebebi.",
  "saha":"Merkezde park yeri bulmak zor olduğu için taşınabilir makineyle çıkıyor, aracı uzağa bırakmamız gerekse de ekipmanı daireye elde taşıyoruz."},
 {"ad":"Başiskele","slug":"basiskele","komsu":["izmit","kartepe","golcuk"],
  "banner":"basiskele-tikali-gider-acma",
  "mahalle":["Kılıçarslan","Yeniköy","Bahçecik","Sepetlipınar","Karadenizliler","Yuvacık","Kullar","Şehit Ekrem"],
  "yapi":"Başiskele körfezin güney kıyısında; Yeniköy ve Bahçecik tarafında yeni siteler, iç kesimde Yuvacık ve Kullar'a doğru bahçeli müstakil evler ağırlıkta. Adresimiz de burada, Kılıçarslan Mahallesi'nde.",
  "gider":"Müstakil ve iki-üç katlı evlerde daire içi hat kısa ama evden çıkan gider bahçeden uzun bir yol izliyor; kıyıya yakın düz arazide eğim az olduğu için tortu yavaş akıp birikiyor.",
  "rogar":"Bahçeli evlerde yağmur suyu ile pis su hattının aynı rögara bağlandığı durumlar sık; sağanakta rögar taşıyorsa önce bu bağlantıyı kontrol ediyoruz.",
  "saha":"Merkezimiz Başiskele'de olduğu için ilçe içindeki çağrılara genellikle en kısa sürede bu ilçede ulaşabiliyoruz."},
 {"ad":"Gölcük","slug":"golcuk","komsu":["basiskele","karamursel"],
  "banner":"golcuk-gider-acma-servisi",
  "mahalle":["Değirmendere Yalı","Halıdere","Merkez","Donanma","Hisareyn","Şirinköy","Yazlık","İhsaniye","Yavuz Sultan Selim"],
  "yapi":"Gölcük merkezinin büyük kısmı 1999 depreminden sonra yeniden yapıldı; Değirmendere ve Halıdere tarafında sahil boyunca apartmanlar, Hisareyn ve İhsaniye'de yamaca kurulu konutlar var.",
  "gider":"Sahile yakın binalar deniz seviyesine çok yakın kotta; bu binalarda bodrum ve zemin kat giderleri yoğun yağışta ya da ana hat dolduğunda geri tepebiliyor.",
  "rogar":"Düşük kotlu sahil şeridinde bina rögarı ile şehir hattı arasındaki eğim az olduğu için çamur ve kum birikiyor; rögar yıkaması burada diğer ilçelere göre daha sık gereken bir iş.",
  "saha":"Değirmendere'den İhsaniye'ye kadar sahil yolu tek aks olduğu için adres tarifini telefonda netleştirip doğru girişten geliyoruz."},
 {"ad":"Derince","slug":"derince","komsu":["izmit","korfez"],
  "banner":"derince-gider-acma-servisi",
  "mahalle":["Çenedağ","Deniz","Fatih","İbni Sina","Kaşkafayaz","Mersincik","Sırrıpaşa","Yenikent","Çavuşlu","Geredeli","Karagöllü","Kayalar","Tahtalı","Terziler","Toylar"],
  "yapi":"Derince'nin sahil kesiminde liman ve sanayi bölgesinin çevresinde apartmanlar, Yenikent'te yeni konutlar, kuzeyde Tahtalı, Geredeli ve Toylar tarafında köy dokusundan kalan müstakil evler var.",
  "gider":"Sahil kesimindeki apartmanlarda dükkân ve iş yeri giderleri konut giderleriyle aynı kolona bağlı olabiliyor; tıkanıklık bu binalarda genellikle en alt kattan başlıyor.",
  "rogar":"Kuzeydeki kırsal mahallelerde bazı evler hâlâ şehir kanalizasyonu yerine fosseptiğe bağlı olabiliyor; rögar şikâyetinde önce hattın nereye bağlandığını soruyoruz.",
  "saha":"Liman ve sanayi trafiğinin yoğun olduğu saatlerde güzergâhı buna göre seçiyor, kırsal mahallelerde adresi konum paylaşımıyla netleştiriyoruz."},
 {"ad":"Körfez","slug":"korfez","komsu":["derince","izmit"],
  "banner":"kocaeli-tikali-gider-acma-servisi",
  "mahalle":["Hereke","Yarımca","Tütünçiftlik","Kirazlıyalı","Mimar Sinan"],
  "yapi":"Körfez'de rafineri ve sanayi tesislerinin çevresinde büyüyen orta katlı apartmanlar, Hereke tarafında eski yerleşim ve sahile yakın yeni siteler bir arada.",
  "gider":"Çok daireli eski apartmanlarda kolon çapları bugünkü kullanım için dar kalıyor; mutfak giderlerindeki yağ zamanla kolonu daraltıyor ve tıkanıklık birden fazla daireyi etkiliyor.",
  "rogar":"Ana yola yakın binalarda bina rögarına yol tozu ve kum taşınıyor; rögar dibinde biriken bu tortu hattı ağırlaştırdığı için yıkamadan sonra kamerayla hattın devamını kontrol ediyoruz.",
  "saha":"Hereke ile Yarımca arasındaki mesafe uzun olduğu için çağrıyı alırken hangi tarafta olduğunuzu sorup ekibi ona göre yönlendiriyoruz."},
 {"ad":"Kartepe","slug":"kartepe","komsu":["izmit","basiskele"],
  "banner":"kartepe-gider-acma-servis",
  "mahalle":["Köseköy","Uzuntarla","Maşukiye","Arslanbey","Uzunçiftlik"],
  "yapi":"Kartepe'de Köseköy ve Uzuntarla tarafında son yıllarda yapılmış siteler, Maşukiye ve Arslanbey'e doğru villa, dağ evi ve hafta sonu evleri ağırlıkta.",
  "gider":"Hafta sonu ya da mevsimlik kullanılan evlerde giderler uzun süre kullanılmadığı için sifon suyu kuruyor, koku ve kuruyup sertleşen birikinti ilk kullanımda tıkanıklığa dönüşüyor.",
  "rogar":"Villa ve müstakil evlerde gider hattı bahçe içinde uzun bir yol alıyor; kışın donma ve kök girişi bu hatlarda rögar tıkanıklığının iki ana sebebi.",
  "saha":"Yükseklerdeki adreslerde kış koşullarında yolu önceden soruyor, kapalı sitelerde güvenliğe giriş bilgisini önceden bildiriyoruz."},
 {"ad":"Karamürsel","slug":"karamursel","komsu":["golcuk","basiskele"],
  "banner":"karamursel-tikaniklik-acma-servisi",
  "mahalle":["Merkez","Ereğli","Kızderbent"],
  "yapi":"Karamürsel'de merkezdeki apartmanların yanında sahil şeridi boyunca uzanan yazlık siteler var; yazın ilçenin nüfusu belirgin şekilde artıyor.",
  "gider":"Yazlık sitelerde kışın kapalı kalan dairelerde sezon başında giderler aynı anda yoğun kullanılmaya başlıyor; biriken tortu ilk haftalarda tıkanıklık olarak geri dönüyor.",
  "rogar":"Sitelerde birçok bloğun bağlı olduğu ortak rögar ve bahçe hatları var; yaz yoğunluğunda bu ortak hat dolduğunda sorun tek dairede değil bütün blokta görülüyor.",
  "saha":"Sezon içinde yazlık sitelere gelen çağrılarda site yönetimiyle konuşup ortak rögarın yerini baştan öğreniyoruz."},
]


# ── Hizmetler (kullanıcı kararı: 4 hizmet, her ilçede ayrı sayfa) ──────────
# "alan": ilçe sayfasında hangi ilçe alanlarının öne çıkacağı.
# "galeri": gerçek saha fotoğrafları (images/<ad>-480|960.webp) + dürüst alt metin (ilçe adı YAZILMAZ — o ilçede çekilmedi).
HIZMETLER = [
 {"slug":"tikali-gider-acma","ad":"Tıkalı Gider Açma","kisa":"Tıkalı gider açma","ikon":"damla",
  "h1":"{ad} Tıkalı Gider Açma","title":"{ad} Tıkalı Gider Açma | Lavabo, Mutfak, Banyo · 7/24",
  "hub_h1":"Tıkalı Lavabo, Mutfak ve Banyo Gideri Açma","hub_neden":"Lavabo, mutfak ve banyo gideri neden tıkanır?",
  "hub_title":"Tıkalı Lavabo, Mutfak ve Banyo Gideri Açma | Kocaeli 7/24",
  "alan":["gider","yapi"],
  "ozet":"Lavabo, evye, duş, küvet ve balkon giderlerindeki tıkanıklığı kırmadan, makineyle açıyoruz.",
  "galeri":[("tikali-gider-acma-servisi","Gider ağzından spiralle çıkarılan saç ve tortu birikintisi"),
            ("kirmadan-tikaniklik-acma","Yer giderinin kapağı açılarak kırmadan tıkanıklık açma"),
            ("kocaeli-gider-acma","Banyoda kullanılan elektrikli gider açma makinesi"),
            ("kocaeli-tikali-gider-acma-servisi","Gider açma ekipmanının taşındığı servis aracı")],
  "isler":[
   ("Lavabo ve banyo gideri","Saç, sabun ve diş macunu birikimiyle yavaşlayan ya da tamamen tıkanan lavabo giderlerini sifonu söküp hattı makineyle açıyoruz."),
   ("Mutfak evyesi","Mutfak hattında tıkanıklığın asıl sebebi yağ. Yağ soğuyunca boru çeperine yapışıyor; spiral ve gerekirse su basıncıyla çeperi temizliyoruz."),
   ("Duş ve küvet gideri","Duş teknesi ve küvet giderinde saç topaklarını çıkarıyor, süzgeç altındaki dar dirseği temizliyoruz."),
   ("Balkon ve yer süzgeci","Balkon ve banyo yer süzgeçlerinde biriken kum, toz ve yaprağı alıp hattı yıkıyoruz."),
   ("Kolon tıkanıklığı","Birden fazla dairede aynı anda gider yavaşlıyorsa sorun bina kolonundadır; kolonu temizleme ağzından makineyle açıyoruz."),
   ("Tekrarlayan tıkanıklık","Aynı gider kısa sürede yine tıkanıyorsa hattı kamerayla görüp kalıcı sebebi buluyoruz."),
  ],
  "belirti":[
   "Lavabo ya da duş suyu geç gidiyor, tabanda su birikiyor",
   "Giderden fokurdama ya da hırıltı sesi geliyor",
   "Mutfakta bulaşık makinesi çalışınca evye doluyor",
   "Banyoda ya da mutfakta gider kokusu var",
   "Bir giderde su boşaltınca başka bir giderden su çıkıyor",
   "Kimyasal açıcı denediniz ama gider bir iki gün sonra yine yavaşladı",
   "Alt kattaki komşu kendi giderinden su geldiğini söylüyor",
  ],
  "oneri":[
   "Tıkalı gidere su dökmeye devam etmeyin; dolan su taşarsa hem ıslaklık hem kirlilik büyür.",
   "Tuz ruhu ve kostik gibi kimyasalları üst üste kullanmayın; karışınca zehirli gaz çıkabiliyor, makine açarken de geri sıçrama riski oluşuyor.",
   "Lavabo sifonunu çıkarabiliyorsanız altına kova koyup açın; tıkanıklık çoğu zaman tam bu dirsekte olur.",
   "Durumu kısa bir video ile WhatsApp'tan gönderin; gelmeden önce hangi ekipmanın gerektiğini görebiliriz.",
  ],
  "sss":[
   ("{ad}{loc} tıkalı gider açma için ne kadar sürede geliyorsunuz?","Ekiplerimiz Kocaeli'de adrese ortalama 30 dakikada ulaşıyor. Trafik ve iş yoğunluğuna göre süre değişebilir; arama sırasında size tahmini süreyi söylüyoruz."),
   ("Gider açmak için fayans ya da duvar kırılıyor mu?","Hayır. Tıkanıklığı gider ağzından ya da temizleme kapağından makineyle açıyoruz. Kırma gerektiren durum genellikle borunun kırılmış ya da çökmüş olmasıdır; bunu da önce kamerayla görüp size gösteriyoruz."),
   ("Fiyatı ne zaman öğrenirim?","Video ya da fotoğrafla yaklaşık bilgi verebiliyoruz. Kesin fiyatı usta yerinde baktıktan sonra, işe başlamadan önce söylüyor."),
   ("Kimyasal gider açıcı işe yaramıyor, neden?","Kimyasal açıcılar yüzeydeki saç ve sabunu kısmen eritir ama boru çeperine yapışmış yağı, kireci ya da sert bir cismi çözmez. Su yolu açılsa bile birikinti yerinde kaldığı için tıkanıklık kısa sürede geri döner."),
   ("Gece ya da hafta sonu geliyor musunuz?","Evet. 7 gün 24 saat çalışıyoruz; telefonla arayabilir ya da WhatsApp'tan yazabilirsiniz."),
  ]},

 {"slug":"tuvalet-tikanikligi-acma","ad":"Tuvalet Tıkanıklığı Açma","kisa":"Tuvalet tıkanıklığı açma","ikon":"klozet",
  "h1":"{ad} Tuvalet Tıkanıklığı Açma","title":"{ad} Tuvalet Tıkanıklığı Açma | Kırmadan · 7/24",
  "hub_h1":"Kocaeli Tuvalet Tıkanıklığı Açma","hub_neden":"Tuvalet neden tıkanır?","hub_title":"Kocaeli Tuvalet Tıkanıklığı Açma | Klozet, Alaturka · 7/24",
  "alan":["gider","yapi"],
  "ozet":"Klozet, alaturka tuvalet ve tuvalet hattındaki tıkanıklığı kırmadan, klozeti sökmeden açıyoruz.",
  "galeri":[("tuvalet-tikanikligi-acma","Tuvalet hattına kameralı tespit cihazı sürülürken"),
            ("kocaeli-tuvalet-tikanikligi-acma","Klozet sökülmüş banyoda gider ağzı ve kamera ekipmanı"),
            ("tuvalet-tikanikligi","Tıkanan tuvaletten taşan suyun banyo zeminine yayılması"),
            ("cihazla-tikaniklik-acma","Klozet yanında ekranlı cihazla tuvalet hattının kontrolü")],
  "isler":[
   ("Klozet tıkanıklığı","Islak mendil, hijyenik ped, kâğıt havlu ya da düşen bir cisimle tıkanan klozeti çoğu durumda yerinden sökmeden açıyoruz."),
   ("Alaturka tuvalet","Alaturka tuvaletlerde sifon dirseği dar ve derin; tıkanıklığı spiral makineyle bu dirsekten geçerek açıyoruz."),
   ("Gömme rezervuarlı klozet","Asma klozetlerde arkadaki bağlantı duvarın içinde. Klozeti sökmek gerekirse contasını yenileyip sızdırmazlığı kontrol ederek geri takıyoruz."),
   ("Tuvaletten koku","Koku tıkanıklık olmadan da gelebilir: kuruyan sifon, gevşeyen klozet contası ya da havalandırma hattı. Sebebi ayırıp ona göre çözüyoruz."),
   ("Kolondan gelen tıkanıklık","Sifon çekince klozette su yükseliyorsa ve alt katlarda da benzer şikâyet varsa sorun bina kolonundadır; kolonu açıyoruz."),
   ("Düşen cisim","Telefon, oyuncak ya da diş fırçası gibi bir cisim düştüyse kamerayla yerini görüp çıkarmaya çalışıyoruz."),
  ],
  "belirti":[
   "Sifonu çekince su klozette yükseliyor ve geç iniyor",
   "Tuvaletten fokurdama ya da hava sesi geliyor",
   "Tuvalet suyu tamamen boşalmıyor ya da hiç gitmiyor",
   "Banyo yer süzgecinden tuvalet suyu geri geliyor",
   "Tuvaletten sürekli kötü koku geliyor",
   "Klozete yanlışlıkla bir cisim düştü",
  ],
  "oneri":[
   "Su yükseliyorsa sifonu tekrar çekmeyin; rezervuardaki su da eklenince klozet taşar.",
   "Rezervuarın altındaki ara musluğu kapatın; sızdıran rezervuar klozeti yavaş yavaş doldurmaya devam eder.",
   "Klozet etrafına havlu serin; taşma olursa zeminin ve alt katın ıslanmasını azaltır.",
   "Pompa ile denediyseniz zorlamayı bırakın; aşırı basınç eski klozet contasını kaçırtabiliyor.",
  ],
  "sss":[
   ("{ad}{loc} tuvalet tıkanıklığı için ne kadar sürede gelirsiniz?","Ekiplerimiz Kocaeli'de adrese ortalama 30 dakikada ulaşıyor. Tuvalet tıkanıklığı acil bir iş olduğu için arama sırasında size tahmini varış süresini söylüyoruz."),
   ("Tuvalet açarken klozet sökülüyor mu?","Çoğu durumda hayır; tıkanıklığı klozetin içinden makineyle açıyoruz. Asma klozette ya da sert bir cisim sıkıştığında sökmek gerekebilir; sökersek contayı yenileyip yerine takıyoruz."),
   ("Tuvalete ıslak mendil atmak tıkanıklık yapar mı?","Evet, tuvalet tıkanıklığının en sık sebeplerinden biri. Islak mendil tuvalet kâğıdı gibi suda dağılmıyor; dirseklerde ve kolonun dönüş noktasında toplanıp tıkaç oluşturuyor."),
   ("Fiyatı önceden söylüyor musunuz?","Evet. Usta yerinde durumu gördükten sonra, işe başlamadan önce fiyatı söylüyor; onayınız olmadan işe başlamıyoruz."),
   ("Gece tuvalet tıkanırsa arayabilir miyim?","Evet. 7/24 hizmet veriyoruz; gece yarısı da hafta sonu da arayabilirsiniz."),
  ]},

 {"slug":"rogar-temizleme","ad":"Rögar Temizleme ve Açma","kisa":"Rögar temizleme","ikon":"rogar",
  "h1":"{ad} Rögar Temizleme ve Rögar Açma","title":"{ad} Rögar Temizleme ve Rögar Tıkanıklığı Açma · 7/24",
  "hub_h1":"Kocaeli Rögar Temizleme ve Rögar Açma","hub_neden":"Rögar neden tıkanır ve taşar?","hub_title":"Kocaeli Rögar Temizleme, Rögar Açma ve Yıkama · 7/24",
  "alan":["rogar","yapi"],
  "ozet":"Taşan rögarı açıyor, rögarı ve bahçe hattını yüksek basınçlı suyla yıkayıp tortudan arındırıyoruz.",
  "galeri":[("rogar-temizleme","Rögar içinde yüksek basınçlı hortumla hat temizliği"),
            ("rogar-yikama","Rögar borusuna basınçlı su püskürten yıkama başlığı"),
            ("rogar-temizlik","Bahçe rögarı açılırken basınçlı suyla yıkama"),
            ("rogar-tikanikligi-acma","Bahçede kazı yapılan noktada rögar hattına makineyle müdahale")],
  "isler":[
   ("Taşan rögarın açılması","Rögar dolup taşıyorsa önce rögar ile sokak hattı arasındaki tıkanıklığı açıp suyun akmasını sağlıyoruz."),
   ("Basınçlı su ile yıkama","Rögar dibinde biriken çamur, kum ve yağ tabakasını yüksek basınçlı suyla söküp hattı yıkıyoruz."),
   ("Kök temizliği","Ek yerlerinden içeri giren ağaç köklerini makinenin kesici ucuyla temizliyoruz; kökün nereden girdiğini kamerayla gösteriyoruz."),
   ("Bahçe ve bina dışı hat","Bina ile rögar, rögar ile sokak arasındaki dış hatları açıp yıkıyoruz."),
   ("Site ve apartman ortak rögarı","Birçok dairenin bağlı olduğu ortak rögarlarda yönetimle birlikte planlı temizlik yapıyoruz."),
   ("Yıkama sonrası kontrol","Yıkamadan sonra hattın akışını test ediyor, gerekirse kamerayla çökme ya da kırık olup olmadığına bakıyoruz."),
  ],
  "belirti":[
   "Bahçedeki ya da bina önündeki rögar taşıyor",
   "Rögar kapağının çevresinden kötü koku geliyor",
   "Yağmurdan sonra bodrum ya da zemin kat giderleri geri tepiyor",
   "Binadaki bütün giderler aynı anda yavaşladı",
   "Rögar kapağını açınca suyun durgun beklediğini görüyorsunuz",
   "Bahçede rögara yakın bir noktada sürekli ıslaklık var",
  ],
  "oneri":[
   "Rögar taşıyorsa binada su kullanımını azaltın; çamaşır ve bulaşık makinesini çalıştırmayın.",
   "Rögar kapağını açtıysanız çevresini işaretleyin; açık rögar özellikle çocuklar için tehlikelidir.",
   "Rögara içine girerek ya da eğilerek müdahale etmeyin; kapalı rögarda zehirli gaz birikebilir.",
   "Sokaktaki belediye hattı taşıyorsa bu sizin rögarınızın değil şebekenin sorunudur; İSU'ya haber verin.",
  ],
  "sss":[
   ("{ad}{loc} rögar temizliği ne kadar sürer?","Rögarın derinliğine ve hattın uzunluğuna göre değişiyor. Tek bir bahçe rögarını açmak ve yıkamak çoğu zaman kısa süren bir iş; site ortak rögarlarında süre uzayabiliyor. Gelince yerinde bakıp süreyi ve fiyatı söylüyoruz."),
   ("Rögar ile şehir kanalizasyonu arasındaki hat kime ait?","Parsel içindeki rögar ve bina bağlantı hattı mülk sahibinin sorumluluğundadır; yoldaki ana kanalizasyon ise Kocaeli'de İSU'nun sorumluluğundadır. Taşma sokaktaki ana hattan geliyorsa İSU'yu aramanız gerekir."),
   ("Rögar neden sürekli doluyor?","En sık sebepler ek yerlerinden giren ağaç kökleri, dipte biriken çamur ve kum, yağmur suyunun pis su hattına bağlanması ve borunun çökmesidir. Kamerayla bakmadan hangisi olduğunu kesin söylemek zor."),
   ("Rögar yıkaması kokuyu keser mi?","Koku rögarda biriken tortudan geliyorsa yıkamadan sonra belirgin şekilde azalır. Koku kapak sızdırmazlığından ya da havalandırmadan geliyorsa ayrıca bakmak gerekir."),
   ("Fiyatı ne zaman söylüyorsunuz?","Usta rögarı açıp durumu gördükten sonra, işe başlamadan önce fiyatı söylüyor."),
  ]},

 {"slug":"kamerali-goruntuleme","ad":"Kameralı Görüntüleme","kisa":"Kameralı gider görüntüleme","ikon":"kamera",
  "h1":"{ad} Kameralı Gider Görüntüleme","title":"{ad} Kameralı Gider ve Tıkanıklık Görüntüleme · Kırmadan",
  "hub_h1":"Kocaeli Kameralı Gider Görüntüleme","hub_neden":"Kameralı görüntüleme ne zaman gerekir?","hub_title":"Kocaeli Kameralı Gider Görüntüleme ve Tıkanıklık Tespiti",
  "alan":["gider","rogar"],
  "ozet":"Gider hattının içine kamera sokup tıkanıklığın yerini, sebebini ve borunun durumunu kırmadan görüyoruz.",
  "galeri":[("kamerali-tikaniklik-goruntuleme","Duş giderine sürülen makaralı kameranın ekran ünitesi"),
            ("tikaniklik-acma-cihazi","Banyo giderinde ekranlı kamerayla hat içinin izlenmesi"),
            ("cihazla-tikaniklik-acma","Tuvalet yanında kamera kontrol ünitesiyle görüntüleme"),
            ("cihazla-goruntuleme","Banyo duvarında termal kamerayla tesisat kontrolü")],
  "isler":[
   ("Tıkanıklığın yerini bulma","Kamerayı gider ağzından sürüp tıkanıklığın kaç metre ileride olduğunu ve hangi dirsekte durduğunu görüyoruz."),
   ("Sebep tespiti","Yağ, kireç, kök, düşen cisim, çökmüş ya da kırık boru; kamera hangisi olduğunu gösteriyor, buna göre doğru yöntemi seçiyoruz."),
   ("Kırmadan karar","Kırma gerekip gerekmediğine görüntüye bakarak karar veriyoruz; gerekiyorsa yalnızca sorunlu noktayı işaretliyoruz."),
   ("Açma sonrası kontrol","Gider açıldıktan sonra hattı yeniden görüntüleyip birikintinin tamamen temizlendiğini doğruluyoruz."),
   ("Ev alırken ya da tadilat öncesi","Tadilattan ya da ev almadan önce gider hatlarının durumunu görmek isteyenler için hat kontrolü yapıyoruz."),
   ("Görüntüyü sizinle paylaşma","Ekranda gördüğümüzü sizinle birlikte izliyoruz; isterseniz görüntüyü telefonunuza da gönderiyoruz."),
  ],
  "belirti":[
   "Aynı gider kısa aralıklarla tekrar tekrar tıkanıyor",
   "Gider açıldı ama su yine yavaş gidiyor",
   "Duvarda ya da zeminde sebebi bilinmeyen nem ve koku var",
   "Klozete ya da gidere bir cisim düştü",
   "Tadilat yapacaksınız ve gider hattının durumunu bilmek istiyorsunuz",
   "Bahçe hattında kök ya da çökme olduğundan şüpheleniyorsunuz",
  ],
  "oneri":[
   "Tıkanıklık tekrar ediyorsa en son ne zaman ve hangi giderde olduğunu not edin; kamerayla nereye bakacağımızı belirlemeyi kolaylaştırır.",
   "Kırma kararı vermeden önce görüntüleme isteyin; çoğu tıkanıklık kırmadan açılabiliyor.",
   "Düşen bir cisim varsa o gideri kullanmayın; cisim ilerledikçe çıkarması zorlaşır.",
   "Yapı ve tadilat planlarınız varsa hat görüntülemesini işin başında yaptırın.",
  ],
  "sss":[
   ("{ad}{loc} kameralı gider görüntüleme yapıyor musunuz?","Evet. Kamera ekipmanı servis aracımızda bulunuyor; tıkanıklık açarken ya da ayrıca hat kontrolü için kameralı görüntüleme yapıyoruz."),
   ("Kameralı görüntüleme için bir yer kırılıyor mu?","Hayır. Kamerayı gider ağzından, sifon yerinden ya da rögardan sürüyoruz. Amacımız zaten kırmadan önce sorunu görmek."),
   ("Kamera ne kadar uzağı görüyor?","Kameranın kablo uzunluğu ve hattın dirsek sayısı belirleyici. Ev içi giderler ve bina çıkışına kadar olan hatlar için genellikle yeterli; çok uzun dış hatlarda rögardan ikinci bir giriş yapıyoruz."),
   ("Görüntüyü bana verebilir misiniz?","Ekranda gördüğümüzü sizinle birlikte izliyoruz; isterseniz kaydı ya da ekran görüntüsünü telefonunuza gönderiyoruz."),
   ("Fiyatı önceden öğrenebilir miyim?","Evet. Usta yerinde hattı görüp işin kapsamını belirledikten sonra, işe başlamadan önce fiyatı söylüyor."),
  ]},
]

# ── Hizmete göre ilçe sayfası köprü cümlesi (ilçe alanlarını hizmete bağlar) ──
KOPRU = {
 "tikali-gider-acma":   "{ad}{loc} tıkalı gidere geldiğimizde önce tıkanıklığın yalnızca sizin dairenizde mi yoksa binanın ortak kolonunda mı olduğunu ayırıyoruz; yöntemi buna göre seçiyoruz.",
 "tuvalet-tikanikligi-acma": "{ad}{loc} tuvalet tıkanıklığında önce sorunun klozetin kendi dirseğinde mi, daireden kolona giden hatta mı yoksa kolonun kendisinde mi olduğunu ayırıyoruz.",
 "rogar-temizleme":     "{ad}{loc} rögar çağrısında önce rögarı açıp suyun nereden geldiğine ve nereye gidemediğine bakıyor, sorun parsel içinde mi şehir hattında mı onu netleştiriyoruz.",
 "kamerali-goruntuleme":"{ad}{loc} kameralı görüntülemeyi en çok tekrarlayan tıkanıklıklarda ve kırma kararı verilmeden önce yapıyoruz; görüntü, gereksiz kırmanın önüne geçiyor.",
}

# ── Müşteri yorumları ───────────────────────────────────────────────────────
# ⛔ YALNIZ GERÇEK yorum (Google İşletme Profili vb.). Uydurma yorum = Google yaptırımı + Ticari Reklam Yönetmeliği.
# Biçim: ("Ad S.", "İlçe", puan 1-5, "yorum metni", "Google yorumu")   Boşken bölüm sitede görünmez.
YORUMLAR = []
