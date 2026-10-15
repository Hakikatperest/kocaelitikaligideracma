# -*- coding: utf-8 -*-
"""
Mahalle sayfaları (pSEO, 2026-10-15 kullanıcı kararı: "Tam istek: mahalle × kelime") — metin havuzu.
Veri: _src/mahalleler.json (OSM admin_level=8, 301 resmî mahalle; merkez koordinatı + open-meteo rakımı).
Sayfa: /<ilce>-<mahalle>-<kelime>/   ·   dizin: /<ilce>-mahalleleri/

Farklılaştırma GERÇEK veriyle: ofise kuş uçuşu mesafe + yön, rakım kuşağı, en yakın 6 mahalle, ilçe metni.
⛔ Uydurma vaka/rakam yok · ✅ su kaçağı: kırmadan, görüntülü TESPİT + TAMİR, 7/24 (kullanıcı 2026-10-15) · ⛔ kombi/musluk-batarya teyit edilmedi → "yapmıyoruz" listesinde
⛔ aggregateRating yok · ⛔ gövdede yeni Ara/WhatsApp butonu yok (hero + #teklif + yüzen butonlar yeter)
Tarih SABİT (kullanıcı kararı 2026-10-15): günlük tazelik cron'u bu sayfalara dokunmaz → depo şişmez.

Yer tutucular: {M} "Cedit Mahallesi" · {Mloc} 'nde · {Mdat} 'ne · {Mgen} 'nin · {Mabl} 'nden · {Mkisa} "Cedit"
               {I} ilçe · {Iloc} {Idat} {Igen} {Iabl} · {km} · {yon} · {r} rakım · {k} kelime (küçük harf)
"""
TARIH = "2026-10-15T02:45:00+00:00"   # mahalle sayfalarının ilk yayın anı (commit af97330); ⛔ GELECEK zaman yazma

# slug, H1'deki ad, cümle içi, ilgili hizmet sayfası, tip
KELIMELER = [
 ("tikaniklik-acma",         "Tıkanıklık Açma",         "tıkanıklık açma",         "tikali-gider-acma",        "genel"),
 ("gider-acma",              "Gider Açma",              "gider açma",              "tikali-gider-acma",        "genel"),
 ("tikali-gider-acma",       "Tıkalı Gider Açma",       "tıkalı gider açma",       "tikali-gider-acma",        "genel"),
 ("su-tesisatcisi",          "Su Tesisatçısı",          "su tesisatçısı",          "tikali-gider-acma",        "su"),
 ("en-yakin-su-tesisatcisi", "En Yakın Su Tesisatçısı", "en yakın su tesisatçısı", "tikali-gider-acma",        "su"),
 ("acil-tesisatci",          "Acil Tesisatçı",          "acil tesisatçı",          "tikali-gider-acma",        "acil"),
 ("gider-acma-ustasi",       "Gider Açma Ustası",       "gider açma ustası",       "tikali-gider-acma",        "usta"),
 ("banyo-gideri-acma",       "Banyo Gideri Açma",       "banyo gideri açma",       "tikali-gider-acma",        "banyo"),
 ("mutfak-gideri-acma",      "Mutfak Gideri Açma",      "mutfak gideri açma",      "tikali-gider-acma",        "mutfak"),
 ("tuvalet-gideri-acma",     "Tuvalet Gideri Açma",     "tuvalet gideri açma",     "tuvalet-tikanikligi-acma", "tuvalet"),
]
KISA_ETIKET = {"tikaniklik-acma": "Tıkanıklık", "gider-acma": "Gider açma", "tikali-gider-acma": "Tıkalı gider",
               "su-tesisatcisi": "Su tesisatçısı", "en-yakin-su-tesisatcisi": "En yakın", "acil-tesisatci": "Acil",
               "gider-acma-ustasi": "Usta", "banyo-gideri-acma": "Banyo", "mutfak-gideri-acma": "Mutfak",
               "tuvalet-gideri-acma": "Tuvalet"}

# ── hero giriş cümlesi ──────────────────────────────────────────────────────
GIRIS = {
 "genel": [
  "{Mloc} {k} için 7 gün 24 saat ulaşabileceğiniz ekibiz. Lavabo, mutfak, banyo, tuvalet ya da rögar fark etmez; tıkanıklığı kırmadan açıyor, ödemeyi iş bitince alıyoruz.",
  "{I} {M} için {k} servisi: gideriniz tıkandıysa sabahı beklemeyin. Ekiplerimiz {Iloc} adrese ortalama 30 dakikada ulaşıyor, fiyatı işe başlamadan söylüyoruz.",
  "{Mloc} giderden su gitmiyor, tuvalet ya da rögar doluyorsa arayın. Tıkanıklığın yerini gerektiğinde kamerayla görüp kırmadan açıyoruz; 7/24 açığız.",
 ],
 "su": [
  "{Mloc} {k} arıyorsanız doğru yerdesiniz. Tıkalı gider, tuvalet, rögar ve taşma için 7/24 geliyoruz; su kaçağını da kırmadan, görüntülü cihazla bulup tamirini yapıyoruz. Kombi işi yapmıyoruz.",
  "{I} {M} için {k} mı lazım? Su gitmiyor, geri geliyor ya da taşıyorsa tıkanıklığı kırmadan açıyoruz; duvarda nem, tavanda leke ya da gizli bir sızıntı varsa kaçağın yerini kırmadan bulup tamir ediyoruz. İkisi için de 7/24 açığız.",
 ],
 "acil": [
  "{Mloc} gece yarısı tuvalet taştı, gider geri tepiyor, rögar doldu ya da bir yerden su mu kaçıyor? 7 gün 24 saat açığız; aradığınızda önce suyu nasıl durduracağınızı anlatıyoruz.",
  "{I} {M} için acil tesisatçı arıyorsanız ve sorun tıkanıklık, taşma ya da su kaçağıysa hemen arayın. Gece, hafta sonu, bayram fark etmez; ödemeyi iş bitince alıyoruz.",
 ],
 "usta": [
  "{Mloc} gider açma ustası çağıracaksanız cihazı olan, fiyatı işe başlamadan söyleyen ve kırmadan çalışan bir ekip arayın. Biz tam olarak böyle çalışıyoruz; 7/24.",
  "{I} {M} için gider açma ustası: spiral makinesi, basınçlı yıkama ve kamera araçta geliyoruz. Kırmadan açıyor, sorun giderilmeden ücret almıyoruz.",
 ],
 "banyo": [
  "{Mloc} lavabo, duş ya da küvet gideri yavaş akıyor veya hiç gitmiyorsa arayın. Saç ve sabun birikimini kırmadan, makineyle açıyoruz; 7/24.",
  "{I} {M} için banyo gideri açma: lavabo, duş teknesi, küvet ve yer süzgeci. Tıkanıklığı söküp temizliyor, akışı sizinle birlikte test ediyoruz.",
 ],
 "mutfak": [
  "{Mloc} mutfak evyesi doluyor, bulaşık makinesinin suyu geri geliyorsa sebep çoğu zaman borunun çeperine yapışmış yağ. Kırmadan, makineyle açıyoruz; 7/24.",
  "{I} {M} için mutfak gideri açma: evyeden kolona kadar hattı açıyor, yağ birikimini gerekirse basınçlı suyla temizliyoruz. Fiyatı işe başlamadan söylüyoruz.",
 ],
 "tuvalet": [
  "{Mloc} tuvalet tıkandı, su yükseliyor mu? Sifonu bir daha çekmeyin, rezervuarın ara musluğunu kapatıp bizi arayın. Klozeti çoğu zaman sökmeden açıyoruz; 7/24.",
  "{I} {M} için tuvalet gideri açma: klozet, alaturka ve tuvaletten kolona inen hat. Islak mendil ve sıkışan cisimleri kırmadan çıkarıyoruz.",
 ],
}

# ── mesafe / yön ────────────────────────────────────────────────────────────
ULASIM = [  # (üst sınır km, metin)
 (4,   "Ofisimiz Başiskele Kılıçarslan'da ve {M} buraya kuş uçuşu yaklaşık {km} km mesafede, ofisimizin {yon} yönünde. Yani neredeyse komşuyuz :) Ekip çoğu zaman birkaç dakikada yola çıkmış oluyor."),
 (12,  "Ofisimiz Başiskele Kılıçarslan'da; {M} ofisimizin {yon} yönünde, kuş uçuşu yaklaşık {km} km uzaklıkta. Ekiplerimiz {Iloc} adrese ortalama 30 dakikada ulaşıyor; arayınca o anki tahmini süreyi de söylüyoruz."),
 (22,  "{M} ofisimizin {yon} yönünde, kuş uçuşu yaklaşık {km} km uzaklıkta. Arayınca ekibi ofisten değil, o an size en yakın noktadan yönlendiriyor ve tahmini varış süresini baştan söylüyoruz."),
 (999, "{M} ofisimizden kuş uçuşu yaklaşık {km} km uzakta, {yon} yönünde. Mesafe uzun olduğu için arayınca ekibin o an nerede olduğuna bakıp size dürüst bir varış süresi veriyoruz; söz verdiğimiz saatte orada oluyoruz."),
]
ULASIM_EK = [
 "Ararken mahalle ve sokak adını, mümkünse bina ya da site adını söylemeniz ekibi doğru girişe yönlendirmemizi kolaylaştırıyor.",
 "WhatsApp'tan konum atarsanız ekip adresi aramakla vakit kaybetmiyor; bir de kısa video atarsanız hangi makineyle geleceğimize oradan karar veriyoruz.",
 "Site ya da apartmansa güvenlik ya da yönetici bilgisini önceden verirseniz kapıda beklemeden işe başlıyoruz.",
]

# ── rakım kuşağı → tıkanıklık karakteri ─────────────────────────────────────
ARAZI = [  # (üst sınır m, ad, metin)
 (25,  "kıyı", "Harita verisine göre {Mgen} merkezi deniz seviyesinden yaklaşık {r} metre yukarıda; yani alçak ve düz bir kesim. Düz arazide gider hatlarının eğimi az olduğu için su yavaş akıyor, yağ ve tortu yolda kalıp birikiyor. Yoğun yağışta ana hat dolduğunda zemin kat ve bodrum giderlerinden geri tepme de alçak kotta daha sık görülüyor."),
 (120, "etek", "Harita verisine göre {Mgen} merkezi yaklaşık {r} metre rakımda; düzlükle yamacın buluştuğu bir kesim. Yamaçtan inen hatlar düzlüğe geçtiği yerde yavaşlıyor; tıkanıklık çoğu zaman bu geçiş noktasında, bina rögarında ya da kolonun yatay hatta döndüğü dirsekte çıkıyor."),
 (350, "yamaç", "Harita verisine göre {Mgen} merkezi yaklaşık {r} metre rakımda, eğimli bir bölgede. Eğim suyu hızlandırsa da dik inen kolonlar ve uzun bahçe hatları dirseklerde tortu bırakıyor; bahçeli evlerde ağaç kökünün ek yerlerinden hatta girmesi de sık karşılaştığımız bir durum."),
 (9999, "yüksek", "Harita verisine göre {Mgen} merkezi yaklaşık {r} metre rakımda, ilçenin yüksek kesimlerinde. Kışın soğuk gecelerde dış hatlarda donma, bahçe hatlarına kök girmesi ve bazı evlerde şehir hattı yerine fosseptiğe bağlı gider bu kesimde karşımıza çıkan durumlar; arayınca önce hattın nereye bağlı olduğunu soruyoruz."),
]
ARAZI_NOT = "Mahallenin her sokağı aynı değil; bu bilgi genel bir fikir verir. Kesin sebebi yerinde, gerekirse kamerayla görerek söylüyoruz."

# ── kelimeye özel "ne yapıyoruz" bölümü ─────────────────────────────────────
NE_H2 = {
 "genel":  ["{Mloc} {k}: hangi işlere geliyoruz?", "{M} {k} hizmetinde neler yapıyoruz?"],
 "su":     ["{Mloc} {k} arayanlar için: hangi işleri yapıyoruz, hangilerini yapmıyoruz?"],
 "acil":   ["{Mloc} acil durumda ilk 5 dakika", "{M} acil tıkanıklık: usta gelene kadar ne yapmalısınız?"],
 "usta":   ["{Mloc} gider açma ustası çağırırken nelere dikkat etmelisiniz?"],
 "banyo":  ["{Mloc} banyo giderinde hangi işleri yapıyoruz?"],
 "mutfak": ["{Mloc} mutfak giderinde hangi işleri yapıyoruz?"],
 "tuvalet":["{Mloc} tuvalet giderinde hangi işleri yapıyoruz?"],
}
SU_YAPIYORUZ = ["Lavabo, evye, duş, küvet ve yer süzgeci tıkanıklığı", "Tuvalet ve klozet tıkanıklığı, alaturka dahil",
                "Bina kolonu ve bahçe hattı tıkanıklığı", "Rögar açma ve basınçlı suyla yıkama",
                "Kameralı gider görüntüleme ile tıkanıklığın yerini ve sebebini bulma",
                "Kırmadan, görüntülü cihazla su kaçağı tespiti ve kaçağın tamiri"]
SU_YAPMIYORUZ = ["Musluk, batarya, rezervuar iç takımı değişimi",
                 "Kombi, termosifon ve kalorifer tesisatı"]
SU_METIN = [
 "\"Su tesisatçısı\" diye arayanların önemli bir kısmı aslında giderin tıkanması, suyun geri gelmesi, tuvaletin taşması ya da duvardan gelen bir sızıntı için arıyor. Bunların hepsi bizim işimiz. Su kaçağında önce yerini kırmadan, görüntülü cihazla buluyor, sonra yalnızca o noktayı açıp tamir ediyoruz; böylece bütün duvarı ya da zemini kırmak gerekmiyor. Kombi, musluk ve batarya işi ise yapmıyoruz.",
 "Tesisatın iki tarafı var: eve temiz suyu getiren hat ve kullanılmış suyu götüren gider hattı. Gider tarafında tıkanıklık açıyoruz: su gitmiyorsa, geri tepiyorsa ya da taşıyorsa bizi arayın. Temiz su tarafında ise su kaçağını tespit edip tamir ediyoruz: duvarda nem, tavanda leke, sebebi belli olmayan bir sızıntı ya da birden yükselen su faturası varsa kaçağın yerini kırmadan, görüntülü cihazla buluyoruz.",
]
ACIL_ADIM = {
 "Tuvalet taşıyorsa": "Sifonu bir daha çekmeyin; rezervuarın altındaki ara musluğu kapatın.",
 "Mutfak gideri doluyorsa": "Bulaşık makinesini ve çamaşır makinesini durdurun; evyeye su dökmeyin.",
 "Rögar taşıyorsa": "Evde su kullanımını azaltın; kapağın çevresini işaretleyin, içine eğilmeyin.",
 "Alt kata su gidiyorsa": "O hatta bağlı bütün giderleri kullanmayı bırakın ve komşunuza haber verin.",
}
ACIL_METIN = [
 "Acil tesisatçı aradığınız durum bir tıkanıklık, geri tepme, taşma ya da su kaçağıysa doğru yerdesiniz; 7/24 geliyoruz. Su kaçağında önce ana vanayı kapatın; kaçağın yerini kırmadan bulup tamir ediyoruz. Kombi arızası için ise kombi servisine ulaşın.",
 "Bizim acil işlerimiz: taşan tuvalet, dolan rögar, geri tepen mutfak gideri ve su kaçağı. Bu durumlarda gece de hafta sonu da arayabilirsiniz. Su borusu patladıysa ana vanayı kapatın ve bizi arayın; kaçağın yerini kırmadan bulup tamir ediyoruz. Kombi su kaçırıyorsa kombi servisine ulaşın.",
]
BANYO_ISLER = ["Lavabo ve banyo gideri", "Duş ve küvet gideri", "Balkon ve yer süzgeci", "Tekrarlayan tıkanıklık"]
MUTFAK_ISLER = ["Mutfak evyesi", "Kolon tıkanıklığı", "Tekrarlayan tıkanıklık"]
MUTFAK_EK = "Mutfakta en sık yapılan hata yağı sıcakken lavaboya dökmek. Sıcak yağ akar ama borunun soğuk bölümünde donup çepere yapışır; birkaç ay içinde boru çapı daralır. Kızartma yağını bir kaba alıp çöpe atmak bu işin yarısını çözüyor."
BANYO_EK = "Banyoda tıkanıklığın bir numaralı sebebi saç. Süzgeç altına bir saç tutucu takmak ve ayda bir sifonu söküp temizlemek, usta çağırma ihtiyacınızı ciddi şekilde azaltıyor."

# ── SSS havuzu (sayfa başına 3) ─────────────────────────────────────────────
SSS = {
 "ortak": [
  ("{Mdat} ne kadar sürede gelirsiniz?", "Ofisimiz Başiskele'de ve {M} buraya kuş uçuşu yaklaşık {km} km. Ekiplerimiz Kocaeli'de adrese ortalama 30 dakikada ulaşıyor; trafik ve o anki iş yoğunluğuna göre değişebileceği için arayınca tahmini süreyi söylüyoruz."),
  ("{Mloc} gece ya da hafta sonu geliyor musunuz?", "Evet. 7 gün 24 saat çalışıyoruz; gece, hafta sonu ve bayram fark etmez."),
  ("Ücreti ne zaman ödüyorum?", "Sorun tamamen giderilmeden ücret talep etmiyoruz; ödemeyi işlem tamamlandıktan sonra alıyoruz. Fiyatı ise usta yerinde gördükten sonra, işe başlamadan söylüyor."),
  ("Belediye {Mloc} evimin giderini açar mı?", "Hayır. Ev ve bina içindeki tesisat mülk sahibinin sorumluluğundadır; {I} Belediyesi bu işe ekip göndermez. Sokaktaki ana kanalizasyon hattı ise İSU'nundur, ona ALO 185'ten 7/24 ulaşabilirsiniz."),
  ("Kırma yapmadan açabiliyor musunuz?", "Çoğu tıkanıklığı gider ağzından makineyle, kırmadan açıyoruz. Kırma ancak boru kırılmış ya da çökmüşse gündeme gelir; bunu da önce kamerayla size gösteriyoruz."),
  ("Telefonda fiyat verebilir misiniz?", "Kesin fiyatı telefonda vermiyoruz çünkü her tıkanıklık farklı. WhatsApp'tan fotoğraf ya da video atarsanız yaklaşık bilgi verebiliyoruz; kesin fiyatı usta yerinde görüp işe başlamadan söylüyor."),
 ],
 "su": [("Su borum patladı, geliyor musunuz?", "Evet, 7/24 geliyoruz. Önce ana vanayı kapatın, sonra arayın. Kaçak duvarın ya da zeminin içindeyse yerini kırmadan, görüntülü cihazla buluyor, yalnızca o noktayı açıp tamir ediyoruz.")],
 "acil": [("Gece yarısı arasam gelir misiniz?", "Evet. Gece yarısı da sabaha karşı da arayabilirsiniz; telefonu bir usta açar, önce suyu nasıl durduracağınızı anlatır, sonra ekip yola çıkar.")],
 "tuvalet": [("Klozeti sökmeniz gerekir mi?", "Çoğu zaman hayır. Tıkanıklığı klozetin içinden makineyle açıyoruz; sert bir cisim sıkışmışsa ya da asma klozetse söküm gerekebilir, bunu işe başlamadan söylüyoruz.")],
 "mutfak": [("Bulaşık makinesinin suyu evyeden geri geliyor, sebep ne?", "Genelde evye ile kolon arasındaki hatta yağ birikmiştir; makine suyu bastığında gidecek yer bulamayıp evyeden geri gelir. Hattı açıp yağı temizliyoruz.")],
 "banyo": [("Duşta su birikiyor ama lavabo çalışıyor, sorun nerede?", "Büyük ihtimalle duş teknesinin süzgecinin altındaki dar dirsekte saç birikmiştir. O noktayı söküp temizliyor, gerekirse hattı makineyle açıyoruz.")],
 "usta": [("Ustanın cihazı olması neden önemli?", "Cihazı olmadan gider açmaya çalışmak çoğu zaman tıkanıklığı daha ileri iter ya da eski boruya zarar verir. Biz spiral makinesi, basınçlı yıkama ve kamerayla geliyoruz.")],
}
