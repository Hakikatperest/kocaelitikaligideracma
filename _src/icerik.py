# -*- coding: utf-8 -*-
"""
Makale içerikleri — kullanıcının ağzından (ghostwrite, 2026-10-05: "içlerine benim dilimle makaleler yaz").
Üslup: samimi, dürüst, "siz" hitabı, yer yer :) — kutucuklar "Tavsiyemiz:", "Dikkat:".

⛔ Uydurma vaka/rakam YOK: "geçen hafta X Mahallesi'nde…" gibi olay anlatma; yalnız sık karşılaşılan durumu anlat.
⛔ "garantili" yazma (kapsam verilmedi) → "sorun giderilmeden ücret almıyoruz".
⛔ Fiyat RAKAMI yok (kullanıcı vermedi) → fiyatı belirleyen etkenler + "fiyat işe başlamadan, ödeme iş bitince".
İSU bilgisi doğrulandı (2026-10-05): ALO 185, 7/24; sınır kuralı parsel bacası.

Metin içi bağlantı: [[yol|metin]]  → yol "hizmet:<slug>" (aynı ilçenin o hizmet sayfası, ilçe yoksa hub),
                                      "ilce:<slug>" (ilçe sayfası), ya da düz göreli yol ("iletisim/").
"""

# ── İlçe makaleleri ─────────────────────────────────────────────────────────
ILCE_METIN = {
 "basiskele": {
  "ulasim": "Başiskele bizim evimiz; ofisimiz Kılıçarslan Mahallesi, Hürriyet Caddesi No:1'de. Bizi telefonla arayabilir, WhatsApp'tan yazabilir ya da yolunuz düşerse ofise uğrayabilirsiniz. Arayınca mahallenizi ve sokağınızı söyleyin, mümkünse sorunun kısa bir videosunu atın. Videoya bakıp hangi makineyle geleceğimize karar veriyoruz; böylece gelip \"o cihaz araçta kaldı\" demiyoruz :)",
  "gece": "Başiskele'de gece gelen çağrılarda en büyük avantajımız ofisin ilçenin içinde olması. Gece yarısı taşan bir tuvalet ya da sabaha karşı dolan bir rögar için aradığınızda ekip ilçe dışından değil, Başiskele'nin içinden yola çıkıyor.",
  "belediye": "Başiskele Belediyesi evinizin ya da apartmanınızın gider tesisatına ekip göndermez; sokaktaki ana kanalizasyon hattı da belediyenin değil İSU'nun sorumluluğundadır. Yeniköy ya da Bahçecik'te bahçenizdeki rögar taşıyorsa önce sokaktaki rögara bakın: sokak rögarı boşsa sorun sizin parselinizdedir ve bizi aramanız gerekir; sokak rögarı da doluysa İSU'yu ALO 185'ten arayın.",
  "fiyat": "Başiskele'de fiyatı en çok etkileyen şey bahçe hattının uzunluğu. Müstakil evlerde gider evden çıkıp bahçede uzun bir yol aldığı için tıkanıklık bazen evin içinde değil, bahçe rögarı ile sokak arasında çıkıyor. Bu iş ile bir lavabo sifonunu açmak aynı emek değil; o yüzden usta yerinde görüp fiyatı işe başlamadan söylüyor.",
  "acil": "Acil durumda sizden tek ricamız şu: arayınca önce telefonda söylediğimiz şeyi yapın. Tuvalet taşıyorsa rezervuarın ara musluğunu, mutfak gideri doluyorsa bulaşık makinesini kapatın; bahçe rögarı taşıyorsa evde su kullanımını durdurun. Biz yoldayken bu birkaç dakika hasarı yarıya indirir; Başiskele içinden çıkan ekip de çoğu zaman siz bunları yaparken kapıda olur.",
  "yakin": "Başiskele'de en yakın tıkanıklık açma servisini arıyorsanız adresimiz zaten ilçenin içinde: Kılıçarslan Mahallesi. Yuvacık'tan Yeniköy'e kadar ilçenin her yerine ekip ilçe içinden çıkıyor. Yine de söz verdiğimiz şey ortalama 30 dakika; trafiğe ve o anki iş yoğunluğuna göre değişebiliyor, arayınca size tahmini süreyi söylüyoruz.",
  "yerel": {
   "tikali-gider-acma": "Başiskele'de lavabo ve mutfak gideri şikâyetlerinde sık gördüğümüz durum şu: daire içindeki hat kısa ve temiz, ama evden çıkan gider bahçede eğimi az bir yoldan geçiyor. Kıyıya yakın düz arazide su yavaş aktığı için mutfak yağı bu bölümde soğuyup birikiyor. Lavaboyu açıp geçmiyoruz; gerekirse bahçe hattına da bakıyoruz.",
   "tuvalet-tikanikligi-acma": "Başiskele'de iki-üç katlı müstakil evlerde tuvalet tıkanıklığı çoğu zaman klozetin kendisinde değil, tuvaletten çıkan borunun bahçeye döndüğü dirsekte oluyor. Islak mendil ve kâğıt havlu tam bu dönüşte takılıyor. Klozeti sökmeden önce hattı makineyle açmayı deniyoruz; gerekirse kamerayla dirseğe bakıyoruz.",
   "rogar-temizleme": "Başiskele'nin bahçeli evlerinde rögar şikâyetinin bir kısmı aslında yağmurla geliyor: yağmur suyu borusu pis su hattıyla aynı rögara bağlıysa sağanakta rögar kapasitesini aşıyor ve taşıyor. Rögarı yıkıyoruz ama asıl yaptığımız iş bu bağlantıyı size göstermek; çünkü bağlantı değişmezse rögar her sağanakta yine taşar.",
   "kamerali-goruntuleme": "Başiskele'de kamerayı en çok bahçe hattında kullanıyoruz. Yuvacık ve Kullar tarafındaki eski evlerde ağaç kökü, yeni sitelerde ise inşaattan kalan harç parçaları hattı daraltabiliyor. Kamera ikisini birbirinden ayırıyor; kök varsa kesici uçla, harç varsa farklı bir uçla çalışıyoruz."
  }},
 "izmit": {
  "ulasim": "İzmit'teki çağrılar için ofisimizden körfezin doğu ucunu dolanarak geliyoruz. Arayınca mahallenizi ve mümkünse bir yer tarifi söyleyin; Ömerağa ya da Cedit'in dar sokaklarında aracı nereye bırakacağımızı baştan bilmek işi hızlandırıyor. WhatsApp'tan konum ve kısa bir video atarsanız ekip yola hazırlıklı çıkıyor.",
  "gece": "İzmit merkezde gece arayan müşterilerimizin çoğu apartmanda oturuyor ve sorun alt kattaki komşuya taşmadan çözülmek zorunda. Bu yüzden gece çağrılarında önce telefonda neyi kapatmanız gerektiğini söylüyor, sonra yola çıkıyoruz. 7/24 açığız; gece yarısı da hafta sonu da arayabilirsiniz.",
  "belediye": "İzmit Belediyesi dairenizdeki ya da apartmanınızdaki tıkanıklığı açmaz; sokaktaki ana kanalizasyon hattı İSU'nun sorumluluğundadır. Apartmanda birkaç daire birden etkileniyorsa önce bina kolonuna bakılır: kolon tıkalıysa bu bina içi bir iştir ve bizi aramanız gerekir. Sokaktaki rögar taşıyorsa İSU'yu ALO 185'ten arayın.",
  "fiyat": "İzmit'te fiyatı etkileyen iki şey öne çıkıyor: yamaçtaki eski binalarda uzun ve dik inen kolonlar ve merkezdeki erişim zorluğu. Kolonun temizleme kapağı yoksa ya da yıllar içinde kapatılmışsa işe başka bir noktadan girmek gerekiyor. Bunları yerinde görüp fiyatı işe başlamadan söylüyoruz, ödemeyi sorun giderildikten sonra alıyoruz.",
  "acil": "İzmit'te acil tıkanıklık çağrılarının çoğu apartmandan geliyor ve asıl acele, suyun alt kattaki komşuya ulaşmadan durdurulması. Aradığınızda önce hangi vanayı kapatacağınızı, hangi gideri kullanmayacağınızı söylüyoruz; ekip bu arada yola çıkıyor.",
  "yakin": "İzmit'e en yakın tıkanıklık açma servisini arıyorsanız şunu bilin: ofisimiz İzmit'in hemen güneyindeki Başiskele'de, körfezin karşı kıyısında. Yahyakaptan, Alikahya ya da Kuruçeşme fark etmez; ekiplerimiz İzmit'e ortalama 30 dakikada ulaşıyor. Trafiğin yoğun olduğu saatlerde arayınca size gerçekçi bir süre söylüyoruz.",
  "yerel": {
   "tikali-gider-acma": "İzmit'te mutfak gideri şikâyetlerinin büyük kısmı eski apartmanlardan geliyor. Kolonun yatay hatta döndüğü dirsekte yağ ve tortu birikiyor; üst katlarda sadece yavaşlık olan sorun alt katlarda evyeden geri tepmeye dönüşüyor. Bu yüzden tek bir lavaboyu açıp gitmiyor, sorunun daire içinde mi kolonda mı olduğunu ayırıyoruz.",
   "tuvalet-tikanikligi-acma": "İzmit'in eski merkez mahallelerinde tuvalet tıkanıklığının sık sebebi, alaturkadan klozete dönüştürülmüş tuvaletlerde kalan dar ve derin dirsek. Klozet yeni ama altındaki eski bağlantı dar kalınca mendil ve kâğıt kolayca takılıyor. Makineyle açıyor, gerekiyorsa kamerayla bu dirseği size gösteriyoruz.",
   "rogar-temizleme": "İzmit'te rögar çağrıları daha çok eski bahçeli apartmanlardan geliyor. Bina rögarı ile sokak hattı arasındaki eski borularda ek yerlerinden giren ağaç kökleri rögarın sürekli dolmasına yol açıyor. Rögarı basınçlı suyla yıkıyor, kökü kesici uçla temizliyor, kökün nereden girdiğini kamerayla gösteriyoruz.",
   "kamerali-goruntuleme": "İzmit'te kameralı görüntülemeyi en çok, aynı tıkanıklık için defalarca usta çağırmış apartmanlarda kullanıyoruz. Yamaçtaki binalarda kolon uzun ve dirsekli; sorun bazen kat aralarında değil zemine indiği noktada. Kamerayı sürünce tıkanıklığın kaçıncı metrede olduğunu görüyor, gereksiz kırmanın önüne geçiyoruz."
  }},
 "golcuk": {
  "ulasim": "Gölcük Başiskele'nin batısındaki komşumuz; ofisimizden körfezin güney kıyısındaki sahil yolu üzerinden doğrudan geliyoruz. Arayınca hangi mahallede olduğunuzu söyleyin: Değirmendere ile İhsaniye arasında sahil yolu tek aks olduğu için doğru girişi baştan bilmek zaman kazandırıyor. WhatsApp'tan konum ve video atarsanız daha da iyi.",
  "gece": "Gölcük'te gece en çok rögar ve bodrum kat giderleri için arıyorsunuz; özellikle yoğun yağışın olduğu gecelerde sahile yakın binalarda giderler geri tepebiliyor. 7/24 açığız ve gece çağrısında da gündüzkü ekipmanla geliyoruz. Arayınca önce suyu nasıl durduracağınızı telefonda anlatıyoruz.",
  "belediye": "Gölcük Belediyesi evinizdeki tuvalet ya da lavabo tıkanıklığına ekip göndermez; sokaktaki ana kanalizasyon hattı da belediyenin değil İSU'nun sorumluluğundadır. Sahile yakın binalarda yağmur sonrası taşma görüyorsanız önce sokaktaki rögara bakın: sokak rögarı da doluysa şebeke dolmuştur ve İSU'yu ALO 185'ten aramanız gerekir; sokak boşsa sorun bina hattınızdadır ve bu iş bize düşer.",
  "fiyat": "Gölcük'te fiyatı en çok etkileyen şey binanın kotu. Deniz seviyesine yakın binalarda rögar ile şehir hattı arasındaki eğim az olduğu için çamur ve kum birikiyor; bu durumda sadece açmak yetmiyor, basınçlı suyla yıkamak gerekiyor. Ne gerektiğini yerinde görüp fiyatı işe başlamadan söylüyor, ödemeyi iş bitince alıyoruz.",
  "acil": "Gölcük'te acil tıkanıklık açma servisi ararken şuna dikkat edin: sahile yakın binalarda acil olan bazen sizin gideriniz değil, sokaktaki hattın dolmasıdır. Telefonda önce sokak rögarını sorup gereksiz yere masraf yapmanızı önlüyoruz; sorun bina hattınızdaysa ekip hemen yola çıkıyor.",
  "yakin": "Gölcük'e en yakın tıkanıklık açma servisini arıyorsanız: ofisimiz komşu ilçe Başiskele'de, Gölcük'e sahil yolu üzerinden bağlı. Halıdere'den Değirmendere'ye, Merkez'den Hisareyn'e kadar ekiplerimiz ortalama 30 dakikada adreste. Trafik ve iş yoğunluğuna göre süre değişebilir; arayınca tahmini süreyi söylüyoruz.",
  "yerel": {
   "tikali-gider-acma": "Gölcük'te 1999 sonrası yapılan binalarda daire içi tesisat genelde sağlam; sorun daha çok binanın denize yakın düşük kotlu çıkışında. Mutfak ve lavabo giderinden gelen tortu eğimi az olan bina çıkışında yavaşlayıp birikiyor ve tıkanıklık zemin kat giderlerinde kendini gösteriyor. Daireyi açıp geçmiyor, bina çıkışına da bakıyoruz.",
   "tuvalet-tikanikligi-acma": "Gölcük'te zemin ve bodrum kattaki tuvaletlerden gelen çağrılarda dikkat ettiğimiz şey şu: tuvalet tıkalı mı, yoksa bina hattı dolduğu için su geri mi geliyor? İkincisinde klozeti ne kadar açarsanız açın su yine gelir. Önce bunu ayırıyor, sonra doğru noktaya müdahale ediyoruz.",
   "rogar-temizleme": "Gölcük'ün sahil şeridinde rögar yıkaması diğer ilçelere göre daha sık gereken bir iş. Eğim az olunca rögar dibine kum ve çamur çöküyor, hat ağırlaşıyor. Rögarı basınçlı suyla yıkıyor, ardından hattın akışını test ediyoruz. Sokak tarafı doluysa bunu size söylüyor, İSU'ya bildirmenizi öneriyoruz.",
   "kamerali-goruntuleme": "Gölcük'te kamerayı en çok bodrum ve zemin kat çıkışlarında kullanıyoruz. Düşük kotlu hatlarda su hiç tam boşalmadığı için içerisi göz kararı anlaşılmıyor; kamera, tortunun nerede biriktiğini ve borunun çöküp çökmediğini net gösteriyor. Kırma kararı gerekiyorsa bunu görüntüye bakarak birlikte veriyoruz."
  }},
 "derince": {
  "ulasim": "Derince'ye ofisimizden körfezin doğu ucunu dolanıp İzmit'i geçerek geliyoruz. Arayınca sahil tarafında mı yoksa Tahtalı, Geredeli, Toylar gibi kuzeydeki mahallelerde mi olduğunuzu söyleyin; kırsal mahallelerde WhatsApp'tan konum paylaşmanız adresi bulmamızı çok kolaylaştırıyor.",
  "gece": "Derince'de gece gelen çağrıların önemli kısmı sahil kesimindeki apartmanlardan; özellikle zemin katı dükkân olan binalarda gece biriken tıkanıklık sabah dükkân açılmadan çözülmek isteniyor. 7/24 açığız; gece de hafta sonu da arayabilirsiniz.",
  "belediye": "Derince Belediyesi evinizdeki ya da iş yerinizdeki gider tıkanıklığını açmaz; sokaktaki ana kanalizasyon hattı İSU'nun sorumluluğundadır. Kuzeydeki kırsal mahallelerde ise önce şunu bilmek gerekiyor: eviniz şehir kanalizasyonuna mı bağlı, yoksa fosseptiğe mi? Fosseptik dolduysa bu bir vidanjör işidir; hattın kendisi tıkalıysa bizi arayın.",
  "fiyat": "Derince'de fiyatı belirleyen şey çoğu zaman tıkanıklığın binanın neresinde olduğu. Zemin katı dükkân olan apartmanlarda dükkân ve konut giderleri aynı kolona bağlı olabiliyor; tıkanıklık bu ortak hatta ise iş tek bir lavabodan büyük. Usta yerinde görüp fiyatı işe başlamadan söylüyor; sorun giderilmeden ücret almıyoruz.",
  "acil": "Derince'de acil tıkanıklık açma servisine en çok zemin katı dükkân olan binalardan ihtiyaç duyuluyor; dükkân sabah açılmadan sorunun çözülmesi gerekiyor. Gece de arayabilirsiniz, iş yerinin açılış saatine göre planlıyoruz.",
  "yakin": "Derince'ye en yakın tıkanıklık açma servisini arıyorsanız bilin ki ofisimiz Başiskele'de, körfezin karşı kıyısında. Çenedağ, Sırrıpaşa, Yenikent ya da kuzeydeki mahalleler fark etmez; ekiplerimiz ortalama 30 dakikada adreste. Liman ve sanayi trafiğinin yoğun olduğu saatlerde arayınca gerçekçi bir süre söylüyoruz.",
  "yerel": {
   "tikali-gider-acma": "Derince'nin sahil kesimindeki apartmanlarda tıkalı gider şikâyeti genellikle en alt kattan başlıyor. Üst kat dairelerin gideri zemindeki dükkân ya da iş yeri gideriyle aynı kolonda birleşince yağ ve tortu en altta toplanıyor. Önce sorunun kendi dairenizde mi ortak kolonda mı olduğunu ayırıyoruz.",
   "tuvalet-tikanikligi-acma": "Derince'de iş yeri tuvaletlerinden gelen çağrılar konutlara göre daha sık. Kâğıt havlu ve hijyenik ped, yoğun kullanılan iş yeri tuvaletlerinde klozet dirseğinde hızla birikiyor. Klozeti sökmeden makineyle açıyor, tekrarlıyorsa kamerayla hattın devamına bakıyoruz.",
   "rogar-temizleme": "Derince'de rögar çağrısında ilk sorduğumuz soru şu: eviniz kanalizasyona mı bağlı fosseptiğe mi? Kuzeydeki kırsal mahallelerde bazı evler hâlâ fosseptiğe bağlı olabiliyor. Kanalizasyona bağlı rögarı açıp yıkıyoruz; fosseptik dolmuşsa bunu size dürüstçe söylüyor, vidanjör çağırmanızı öneriyoruz.",
   "kamerali-goruntuleme": "Derince'de kameralı görüntüleme en çok ortak kolon tartışmalarında işe yarıyor: tıkanıklık hangi dairenin hattında, hangi noktada? Kamerayı sürünce bunu tahminle değil görüntüyle söylüyoruz; apartman yönetimiyle konuşurken elinizde somut bir görüntü oluyor."
  }},
 "korfez": {
  "ulasim": "Körfez'e ofisimizden körfezin doğu ucunu dolanıp İzmit ve Derince'yi geçerek kuzey sahil hattı üzerinden geliyoruz. Hereke ile Yarımca arasındaki mesafe uzun olduğu için arayınca hangi tarafta olduğunuzu mutlaka söyleyin. WhatsApp'tan konum atarsanız ekip doğru adrese en kısa yoldan gelir.",
  "gece": "Körfez'de vardiyalı çalışan çok müşterimiz var; gider sorunu da çoğu zaman vardiya dönüşü, gece geç saatte fark ediliyor. 7/24 açığız. Gece aradığınızda önce telefonda suyu nasıl durduracağınızı söylüyor, sonra yola çıkıyoruz.",
  "belediye": "Körfez Belediyesi dairenizdeki ya da apartmanınızdaki tıkanıklığı açmaz; sokaktaki ana kanalizasyon hattı İSU'nun sorumluluğundadır. Çok daireli eski apartmanlarda birkaç daire aynı anda etkileniyorsa sorun büyük ihtimalle bina kolonundadır; bu bina içi bir iştir. Sokaktaki rögar taşıyorsa İSU'yu ALO 185'ten arayın.",
  "fiyat": "Körfez'de fiyatı en çok etkileyen şey çok daireli apartmanlardaki kolon tıkanıklıkları. Mutfak yağı yıllar içinde dar kalan kolonu daraltınca iş tek bir dairenin lavabosu olmaktan çıkıyor. Ne kadar iş olduğunu yerinde görüp fiyatı işe başlamadan söylüyor, ödemeyi sorun giderildikten sonra alıyoruz.",
  "acil": "Körfez'de acil tıkanıklık açma servisi çağrıları çoğu zaman vardiya dönüşü, gece geç saatte geliyor. Hereke'de de Yarımca'da da servis numaramız 7/24 açık; aradığınızda size gerçekçi bir varış süresi söylüyoruz.",
  "yakin": "Körfez'e en yakın tıkanıklık açma servisini arıyorsanız dürüst olalım: ofisimiz Körfez'in içinde değil, Başiskele'de. Ama Hereke'den Yarımca'ya, Tütünçiftlik'ten Kirazlıyalı'ya ekiplerimiz ortalama 30 dakikada adreste. Mesafe uzun olduğu için arayınca size gerçekçi bir varış süresi söylüyoruz.",
  "yerel": {
   "tikali-gider-acma": "Körfez'deki çok daireli eski apartmanlarda kolon çapları bugünkü kullanım için dar kalıyor. Her dairenin mutfak yağı aynı kolona aktığı için kolon zamanla daralıyor ve bir gün birkaç dairede birden gider yavaşlıyor. Bu durumda sadece sizin lavabonuzu açmak çözüm değil; kolonu temizleme ağzından açıyoruz.",
   "tuvalet-tikanikligi-acma": "Körfez'de alt kat dairelerden gelen tuvalet şikâyetlerinde çoğu zaman suç alt katta değil: üst katlardan gelen atık kolonun döndüğü noktada takılıyor ve su en alttaki klozetten yükseliyor. Bu yüzden alt kattaki klozeti açarken kolonu da kontrol ediyoruz.",
   "rogar-temizleme": "Körfez'de ana yola yakın binaların rögarına yol tozu ve kum taşınıyor; rögar dibinde biriken bu tortu hattı ağırlaştırıyor. Rögarı basınçlı suyla yıkadıktan sonra hattın devamını kamerayla kontrol ediyoruz; kum hattın içine de dolmuşsa yıkamayı oraya kadar uzatıyoruz.",
   "kamerali-goruntuleme": "Körfez'de kamerayı en çok kolon tıkanıklığının hangi kat aralığında olduğunu bulmak için kullanıyoruz. Çok katlı binada tahminle çalışmak hem zaman hem gereksiz söküm demek. Kamera tıkanıklığın yerini gösterince en yakın temizleme noktasından girip işi kısa yoldan bitiriyoruz."
  }},
 "kartepe": {
  "ulasim": "Kartepe Başiskele'nin doğusundaki komşumuz; ofisimizden kısa bir yolla geliyoruz. Köseköy ve Uzuntarla'daki sitelerde site adını ve blok numarasını, Maşukiye ve Arslanbey tarafındaki villalarda ise konumu WhatsApp'tan paylaşmanız işimizi çok kolaylaştırıyor. Kapalı sitelerde güvenliğe adımızı önceden bildirirsek giriş hızlanıyor.",
  "gece": "Kartepe'de gece ve hafta sonu çağrıları çoğunlukla hafta sonu evlerinden geliyor: cuma akşamı eve gelinir, giderler uzun süre kullanılmadığı için koku ya da tıkanıklık o gece fark edilir. 7/24 açığız; kış koşullarında yüksekteki adresler için yolu telefonda soruyor, ona göre çıkıyoruz.",
  "belediye": "Kartepe Belediyesi villanızdaki ya da sitenizdeki gider tıkanıklığına ekip göndermez; sokaktaki ana kanalizasyon hattı İSU'nun sorumluluğundadır. Villalarda bahçe hattı ve rögar parselin içinde kaldığı için mülk sahibinin sorumluluğundadır. Sokaktaki ana hat taşıyorsa İSU'yu ALO 185'ten arayın.",
  "fiyat": "Kartepe'de fiyatı en çok bahçe hattının uzunluğu ve kış koşulları etkiliyor. Villalarda gider evden çıkıp bahçede uzun bir yol aldığı için tıkanıklığın yerini bulmak bazen kamera istiyor; donma ya da kök girmişse iş uzuyor. Usta yerinde görüp fiyatı işe başlamadan söylüyor, ödemeyi iş bitince alıyoruz.",
  "acil": "Kartepe'de acil tıkanıklık açma servisine en çok hafta sonu evlerinde ihtiyaç duyuluyor: cuma akşamı eve gelinir, gider o gece tıkanır. Kış koşullarında yüksekteki adresler için yolu telefonda soruyor, ona göre yola çıkıyoruz.",
  "yakin": "Kartepe'ye en yakın tıkanıklık açma servisini arıyorsanız: ofisimiz komşu ilçe Başiskele'de. Köseköy'den Maşukiye'ye, Uzuntarla'dan Arslanbey'e ekiplerimiz ortalama 30 dakikada adreste. Kışın yükseklerdeki adreslerde yol durumuna göre süre uzayabilir; arayınca size gerçekçi bir süre söylüyoruz.",
  "yerel": {
   "tikali-gider-acma": "Kartepe'de hafta sonu ve yazlık evlerde lavabo, duş ve mutfak gideri uzun süre kullanılmayınca sifondaki su kuruyor; hem koku geliyor hem de içeride kalan birikinti sertleşiyor. İlk kullanımda gider tıkanınca kimyasal dökmeyin, sertleşmiş birikintiyi makineyle söküp hattı yıkıyoruz.",
   "tuvalet-tikanikligi-acma": "Kartepe'deki villalarda tuvalet tıkanıklığı bazen tuvalette değil, bahçedeki hatta oluyor: hat uzun, eğim yer yer az ve kışın soğukta akış yavaşlıyor. Klozeti açıp su yine geç gidiyorsa sorun dışarıdadır; bahçe rögarından girip hattı açıyoruz.",
   "rogar-temizleme": "Kartepe'nin villa ve müstakil evlerinde rögar tıkanıklığının iki ana sebebi var: kışın donma ve ağaç kökü. Ağaçlık bahçelerde kökler hattın ek yerlerinden girip rögarı sürekli dolduruyor. Rögarı yıkıyor, kökü kesici uçla temizliyor, hattın devamını kamerayla kontrol ediyoruz.",
   "kamerali-goruntuleme": "Kartepe'de kamera en çok uzun bahçe hatlarında işe yarıyor. Hat onlarca metre olunca tıkanıklığın yerini tahminle bulmak bahçeyi gereksiz kazmak demek. Kamerayı sürüp tıkanıklığın, kökün ya da çökmenin tam yerini işaretliyoruz; kazmak gerekiyorsa yalnızca orayı kazıyorsunuz."
  }},
 "karamursel": {
  "ulasim": "Karamürsel'e ofisimizden körfezin güney kıyısındaki sahil yolunu takip edip Gölcük'ü geçerek geliyoruz. Yazlık sitelerden arıyorsanız site adını ve blok numarasını, Ereğli ya da Kızderbent tarafındaysanız konumu WhatsApp'tan paylaşın. Site yönetiminin numarasını da verirseniz ortak rögarın yerini baştan öğreniyoruz.",
  "gece": "Karamürsel'de yaz aylarında gece çağrıları belirgin şekilde artıyor; sitelerde nüfus birden çoğalınca kışın az kullanılan hatlar ilk yoğun haftalarda tıkanabiliyor. 7/24 açığız; sezon içinde gece de hafta sonu da arayabilirsiniz.",
  "belediye": "Karamürsel Belediyesi yazlık dairenizdeki ya da sitenizdeki gider tıkanıklığını açmaz; sokaktaki ana kanalizasyon hattı İSU'nun sorumluluğundadır. Sitelerde birçok bloğun bağlı olduğu ortak rögar ve bahçe hatları sitenin kendi sorumluluğundadır; bu hatlar için site yönetimiyle birlikte çalışıyoruz. Site dışındaki ana hat taşıyorsa İSU'yu ALO 185'ten arayın.",
  "fiyat": "Karamürsel'de fiyatı en çok etkileyen şey sorunun tek dairede mi yoksa sitenin ortak hattında mı olduğu. Yaz yoğunluğunda ortak rögar dolduğunda sorun bütün blokta görülüyor ve iş tek bir lavabodan büyük oluyor. Yerinde görüp fiyatı işe başlamadan söylüyor, sorun giderilmeden ücret almıyoruz.",
  "acil": "Karamürsel'de acil tıkanıklık açma servisine yazın, sitelerde nüfus birden arttığında ihtiyaç artıyor. Ortak rögar ya da blok hattı taşıyorsa bekledikçe bütün bloğu etkiliyor; servis numaramız sezon boyunca gece gündüz açık.",
  "yakin": "Karamürsel'e en yakın tıkanıklık açma servisini arıyorsanız dürüst olalım: ofisimiz Başiskele'de, Karamürsel'e sahil yolu üzerinden bağlı. Merkezden Ereğli'ye, sahil şeridindeki sitelere ekiplerimiz ortalama 30 dakikada ulaşıyor; yaz trafiğinde süre uzayabilir, arayınca size gerçekçi bir süre söylüyoruz.",
  "yerel": {
   "tikali-gider-acma": "Karamürsel'deki yazlık sitelerde sezon başı klasik bir tablo var: kışın kapalı kalan dairelerde giderler aylarca kullanılmamış, sonra bir hafta sonu herkes aynı anda gelmiş. Kuruyup sertleşen birikinti ilk yoğun kullanımda lavabo ve mutfak giderini tıkıyor. Sertleşen tortuyu makineyle söküp hattı yıkıyoruz.",
   "tuvalet-tikanikligi-acma": "Karamürsel'de yaz aylarında tuvalet tıkanıklığı çoğu zaman misafir kalabalığıyla geliyor: ıslak mendil, ped ve fazla kâğıt aynı hafta sonunda klozete atılınca dirsek tıkanıyor. Klozeti sökmeden açıyoruz; aynı blokta birkaç daire etkileniyorsa ortak hatta da bakıyoruz.",
   "rogar-temizleme": "Karamürsel'deki sitelerde ortak rögar, sezon yoğunluğunda kapasitesinin üstünde çalışıyor. Ortak rögar dolunca taşma tek bir dairede değil bütün blokta görülüyor. Site yönetimiyle birlikte rögarı açıyor, basınçlı suyla yıkıyor; sezon öncesi yıkama için de randevu veriyoruz.",
   "kamerali-goruntuleme": "Karamürsel'de kameralı görüntülemeyi en çok sitelerin ortak hatlarında kullanıyoruz: sorun hangi bloğun hattında, ortak rögardan önce mi sonra mı? Kamera bunu netleştirince site yönetimi neyin, nerede yapılacağını görüntüyle görerek karar veriyor."
  }},
}

# ── Hizmet makaleleri (ilçe ve hub sayfalarında ortak iskelet) ─────────────
# {ad}{loc}{dat}{gen}{abl}{kisa} yer tutucuları build.yer() ile doldurulur. Hub'da {ad}="Kocaeli".
HIZMET_METIN = {
 "tikali-gider-acma": {
  "neden_giris": "Lavabo, mutfak ya da banyo gideri bir günde tıkanmaz; çoğu zaman haftalardır yavaşlayan bir gider bir gün tamamen kapanır. Sebebini bilirseniz hem doğru müdahale yapılır hem de aynı sorun tekrar etmez.",
  "nedenler": [
   ("Mutfak yağı", "Sıcakken akan yağ borunun soğuk bölümünde donup çepere yapışır. Üstüne gelen deterjan ve yemek artığıyla birlikte boru içi her gün biraz daha daralır."),
   ("Saç ve sabun", "Banyo ve duş giderinde saç, sabun kalıntısıyla birleşip keçeleşir ve süzgecin hemen altındaki dirseği kapatır."),
   ("Diş macunu ve kireç", "Lavabo giderinde diş macunu ve kireç ince bir tabaka hâlinde birikir; zamanla gider yavaşlar ve kokmaya başlar."),
   ("Kum ve toz", "Balkon ve yer süzgeçlerine yağmurla gelen kum ve toz giderin dibine çöker ve akışı keser."),
   ("Ortak kolon", "Apartmanda birkaç dairede aynı anda gider yavaşlıyorsa sorun sizin dairenizde değil bina kolonundadır."),
  ],
  "yontem": "Tıkalı gideri kırmadan, gider ağzından ya da temizleme kapağından makineyle açıyoruz. Spiral uç birikintiyi söküyor, gerekirse basınçlı suyla çeperi temizliyoruz. Aynı gider kısa sürede yine tıkanıyorsa kamerayla hattın içine bakıp kalıcı sebebi buluyoruz.",
  "belediye": "{ad}{loc} lavabo, mutfak ya da banyo gideriniz tıkandığında belediyeyi ya da İSU'yu aramanız sorunu çözmez; dairenizin içindeki ve binanızın kolonundaki tesisat mülk sahibinin sorumluluğundadır. İSU yalnızca sokaktaki ana kanalizasyon hattına bakar. Sokaktaki rögar taşıyorsa ALO 185'i arayın; tıkanıklık sizin gideriniz ya da bina kolonunuzdaysa bizi arayın.",
 },
 "tuvalet-tikanikligi-acma": {
  "neden_giris": "Tuvalet tıkanıklığı en can sıkıcı tıkanıklıktır, çünkü beklemeye gelmez. İyi haber şu: sebebi çoğu zaman bellidir ve klozeti sökmeden çözülür.",
  "nedenler": [
   ("Islak mendil", "Tuvalet kâğıdı gibi suda dağılmaz; dirseklerde ve kolonun döndüğü noktada toplanıp tıkaç oluşturur. Paketinde \"tuvalete atılabilir\" yazsa bile."),
   ("Hijyenik ped ve kâğıt havlu", "Suyu emip şişer ve klozet dirseğinde sıkışır."),
   ("Düşen cisim", "Diş fırçası, oyuncak, telefon… Klozete düşen sert bir cisim dirsekte durur, arkasından gelen her şeyi tutar."),
   ("Dar ya da eski bağlantı", "Alaturkadan klozete dönüştürülen tuvaletlerde altta kalan dar ve derin dirsek kolay tıkanır."),
   ("Kolon tıkanıklığı", "Sifon çekince su yükseliyor ve alt katlarda da benzer şikâyet varsa sorun klozette değil bina kolonundadır."),
  ],
  "yontem": "Tuvalet tıkanıklığını çoğu durumda klozeti yerinden sökmeden, klozetin içinden makineyle açıyoruz. Asma klozette ya da sert bir cisim sıkıştığında sökmek gerekebilir; sökersek contasını yenileyip sızdırmazlığı kontrol ederek yerine takıyoruz. Tekrarlıyorsa kamerayla hattın devamına bakıyoruz.",
  "belediye": "{ad}{loc} tuvaletiniz tıkandığında belediye ya da İSU evinize ekip göndermez; klozet ve bina içindeki hat mülk sahibinin sorumluluğundadır. İSU'yu (ALO 185) yalnızca sokaktaki ana kanalizasyon hattı taşıyorsa aramanız gerekir. Sokak rögarı boşsa ve sizin tuvaletiniz taşıyorsa bu iş bize düşer.",
 },
 "rogar-temizleme": {
  "neden_giris": "Rögar bir gecede dolmaz; dibinde biriken her katman hattı biraz daha ağırlaştırır. Taşmaya başladıysa çoğu zaman aylardır biriken bir sorun vardır.",
  "nedenler": [
   ("Ağaç kökü", "Bahçe hattındaki ek yerlerinden içeri giren kökler boru içinde ağ gibi büyür ve rögarı sürekli doldurur."),
   ("Çamur ve kum", "Eğimi az olan hatlarda su yavaş akar, taşıdığı kum ve çamur rögar dibine çöker."),
   ("Yağ birikimi", "Mutfaklardan gelen yağ rögarda soğuyup yüzeyde kalın bir tabaka oluşturur."),
   ("Yağmur suyu bağlantısı", "Yağmur suyu borusu pis su rögarına bağlıysa sağanakta rögar kapasitesini aşıp taşar."),
   ("Çöken ya da kırılan boru", "Eski hatlarda boru çökmüşse su yolu daralır; bunu ancak kamera gösterir."),
  ],
  "yontem": "Taşan rögarı önce açıp suyun akmasını sağlıyoruz, sonra rögarı ve hattı yüksek basınçlı suyla yıkıyoruz. Kök varsa kesici uçla temizliyoruz. Yıkamadan sonra akışı test ediyor, gerekiyorsa kamerayla çökme ya da kırık olup olmadığına bakıyoruz.",
  "belediye": "{ad}{loc} rögar taşıyorsa önce rögarın kime ait olduğuna bakın. Genel kural parsel bacasıdır: binanızın bahçesindeki rögar ve sokağa kadar olan bağlantı hattı mülk sahibinin, sokaktaki ana kanalizasyon hattı İSU'nun sorumluluğundadır. Sokaktaki rögar da doluysa İSU'yu ALO 185'ten arayın; sokak boş, sizin rögarınız doluysa bizi arayın.",
 },
 "kamerali-goruntuleme": {
  "neden_giris": "Kameralı görüntülemeyi bir lüks gibi görmeyin; aslında en çok para ve kırma masrafı kurtaran iştir. Hangi durumlarda gerektiğini aşağıda anlattık.",
  "nedenler": [
   ("Tekrarlayan tıkanıklık", "Aynı gider kısa aralıklarla tekrar tıkanıyorsa içeride açmakla geçmeyen bir sebep vardır: kök, çökme, ters eğim."),
   ("Kırma kararı öncesi", "Biri \"burayı kırmak lazım\" diyorsa önce görüntü isteyin; çoğu tıkanıklık kırmadan açılır."),
   ("Düşen cisim", "Klozete ya da gidere düşen bir cismin yerini kamera gösterir, çıkarmak kolaylaşır."),
   ("Sebebi bilinmeyen koku ve nem", "Duvarda ya da zeminde açıklanamayan nem ve koku varsa kamera hattaki çatlağı gösterebilir."),
   ("Ev alırken ya da tadilat öncesi", "Tadilattan önce gider hatlarının durumunu görmek, sonradan fayans kırmaktan çok daha ucuzdur."),
  ],
  "yontem": "Makaralı kamerayı gider ağzından, sifon yerinden ya da rögardan hattın içine sürüyoruz. Ekranda tıkanıklığın kaç metre ileride olduğunu, sebebini ve borunun durumunu birlikte izliyoruz. İsterseniz görüntüyü telefonunuza gönderiyoruz.",
  "belediye": "{ad}{loc} kameralı görüntüleme belediyenin ya da İSU'nun verdiği bir hizmet değildir; İSU yalnızca sokaktaki ana hatta kendi ekipleriyle çalışır. Bina içindeki ve parselinizdeki hattın kamerayla görüntülenmesi için bizi arayabilirsiniz.",
 },
}

# ── Anasayfa ve Hakkımızda ──────────────────────────────────────────────────
# Kullanıcının 2026-10-05'te verdiği tanıtım metninden (birebir korunup genişletildi).
TANITIM = ("Kocaeli Tıkalı Gider Açma Servisi olarak yılların tecrübesiyle Başiskele, Derince, Gölcük, İzmit ve Karamürsel "
           "başta olmak üzere Kocaeli'nin 7 ilçesinde profesyonel tıkalı gider açma hizmeti veriyoruz. Tıkalı gider, tuvalet "
           "tıkanıklığı, rögar temizleme ve kameralı gider görüntüleme işlemlerini kırmadan, son teknoloji cihazlarımızla "
           "gerçekleştiriyoruz.")
ODEME = ("Sorun tamamen giderilmeden ücret talep etmiyor, işlem tamamlandıktan sonra ödeme alıyoruz. Fiyatı ise usta yerinde "
         "gördükten sonra, işe başlamadan söylüyoruz; onayınız olmadan işe başlamıyoruz.")
KAPANIS = ("Gece gündüz demeden hızlı ve güvenilir hizmet için hemen bizi arayın, tıkanıklık büyümeden profesyonel çözüm alın! "
           "Kılıçarslan Mah. Hürriyet Cad. No:1, Başiskele/Kocaeli adresindeki ofisimizi ziyaret edebilirsiniz. "
           "Doğru tercih: Kocaeli Tıkalı Gider Açma!")

HAKKIMIZDA = [
 ("Biz kimiz?", [TANITIM,
   "İşimiz tek bir konu üzerine: tıkanıklık. Su tesisatı, kombi ya da elektrik işi yapmıyoruz; bütün ekipmanımız ve tecrübemiz gider, tuvalet ve rögar tıkanıklığı ile kameralı görüntüleme üzerine. Bir işte uzmanlaşınca o işi hem daha hızlı hem daha temiz yapıyorsunuz."]),
 ("Nasıl çalışıyoruz?", [
   "Arıyorsunuz ya da WhatsApp'tan yazıyorsunuz; mümkünse sorunun kısa bir videosunu atıyorsunuz. Videoya bakıp hangi makineyle geleceğimize karar veriyoruz. Adresinize ortalama 30 dakikada ulaşıyoruz.",
   "Usta önce sorunun yerini buluyor: gider mi, tuvalet mi, bina kolonu mu, rögar mı? Gerekiyorsa kamerayı hattın içine sürüp tıkanıklığı ekranda birlikte görüyoruz. Fiyatı işe başlamadan söylüyor, onayınızı aldıktan sonra kırmadan açıyoruz."]),
 ("Ücreti ne zaman alıyoruz?", [ODEME,
   "Bunu bir slogan olarak değil, çalışma şeklimiz olarak söylüyoruz: iş bittikten sonra akışı sizinle birlikte test ediyoruz; suyun gittiğini kendi gözünüzle görmeden ödeme istemiyoruz."]),
 ("Hangi bölgelere hizmet veriyoruz?", [
   "Merkezimiz Başiskele'de. Başiskele, İzmit, Gölcük, Derince, Karamürsel, Kartepe ve Körfez'e 7 gün 24 saat servis veriyoruz. Her ilçenin sayfasında, o ilçedeki binalarda en sık karşılaştığımız durumları da anlattık."]),
 ("Ofisimizi ziyaret edin", [KAPANIS]),
]

# ── Tıkanıklık Rehberi (kullanıcı 2026-10-05: "müşterileri bilgilendiren bir site") ──
# Soru varyasyonları NİYETE göre 3 yazıda toplandı; ⛔ her varyasyon için ayrı sayfa AÇMA (kannibalizasyon + ölçeklendirilmiş içerik).
#   lavabo-tikanirsa-ne-yapmali : "lavabo tıkanırsa ne yapmalıyım / ne yapmak lazım", "tıkalı gideri kendim açabilir miyim", "lavabo açmanın en kolay yolu"
#   tuvalet-tikanirsa-ne-yapmali: "tuvalet tıkanırsa ne yapmalıyım / ne yapmak lazım", "alaturka tuvalet tıkanıklığı nasıl gider"
#   gider-acma-aparati          : "gider açma aparatı nereden satın alınır"
# Bölüm öğeleri: düz metin = paragraf · ("h3", başlık, metin) · ("liste", [..]) · ("adim", [..]) · ("ipucu"/"dikkat", metin) · ("tablo", başlıklar, satırlar)
REHBER = [
 {"slug": "lavabo-tikanirsa-ne-yapmali", "ikon": "damla", "gorsel": ("tikali-gider-acma-servisi", "Lavabo giderinden çıkarılan saç ve tortu birikintisi"),
  "h1": "Lavabo Tıkanırsa Ne Yapmalı? Evde Açmanın Yolları",
  "title": "Lavabo Tıkanırsa Ne Yapmalı? Kendiniz Açmanın Yolları | Rehber",
  "aciklama": "Lavabo tıkanırsa ne yapmak lazım, tıkalı gideri kendiniz açabilir misiniz, lavabo açmanın en kolay yolu nedir? Ustadan dürüst cevaplar.",
  "ozet": "Lavabonuz tıkandı ve hemen usta çağırmak istemiyorsunuz; çok da haklısınız :) Basit tıkanıklıkların çoğunu evde kendiniz açabilirsiniz. Bu yazıda ilk 5 dakikada ne yapmanız gerektiğini, en kolay yöntemden başlayarak neleri deneyebileceğinizi ve hangi noktada artık usta çağırmanız gerektiğini dürüstçe anlattık.",
  "hizmet": "tikali-gider-acma",
  "bolum": [
   ("Lavabo tıkanırsa ne yapmak lazım? İlk 5 dakika", [
     ("adim", ["Musluğu kapatın ve tıkalı lavaboya su dökmeye devam etmeyin; dolan su taşarsa sorun büyür.",
               "Lavabodaki suyu bir kapla boşaltın; boş lavaboda ne yaptığınızı görmek kolaylaşır.",
               "Süzgeci ya da tıpayı çıkarıp altındaki saçı ve sabun birikintisini temizleyin. Tıkanıklıkların şaşırtıcı bir kısmı tam burada.",
               "Mutfak evyesiyse bulaşık makinesini ve çamaşır makinesini çalıştırmayın; onların suyu da aynı gidere gelir."]),
     "Bu dört adım çoğu zaman sorunu çözmese bile durumu kontrol altına alır. Sonrası için aşağıdaki yöntemleri kolaydan zora doğru sıraladık."]),
   ("Tıkalı gideri kendim açabilir miyim?", [
     "Evet, çoğu basit tıkanıklığı açabilirsiniz. Sorun yalnızca sizin lavabonuzdaysa ve tıkanıklık süzgecin ya da sifonun hemen altındaysa, bir pompa ya da basit bir spiralle sonuç almanız mümkün.",
     "Ama dürüst olalım: tıkanıklık lavabonun ilerisindeyse, yani duvarın içindeki boruda ya da bina kolonundaysa evdeki aletler oraya ulaşmaz. Bu durumda ne kadar uğraşırsanız uğraşın su yine yavaş gider; zorlamak da eski bağlantıları kaçırtabilir.",
     ("ipucu", "Banyodaki başka bir gider de yavaşladıysa ya da üst kattan su indiğinde lavabonuz fokurduyorsa sorun büyük ihtimalle sizin lavabonuzda değil, ortak hattadır. Bu durumda kendiniz uğraşmayın.")]),
   ("Lavabo açmanın en kolay yolu nedir?", [
     "Aşağıdaki yöntemleri sırayla deneyin; birinde sonuç alırsanız devamına geçmenize gerek yok.",
     ("h3", "1. Süzgeci ve tıpayı temizlemek", "Lavabo tıpasını çıkarın ya da çevirerek yukarı alın. Altına takılan saç ve sabun yumağını eldivenle temizleyin. Banyo lavabolarında en sık işe yarayan yöntem budur."),
     ("h3", "2. Pompa (vantuz) kullanmak", "Lavabonun taşma deliğini ıslak bir bezle sıkıca kapatın; yoksa bastığınız hava oradan kaçar. Lavaboya pompanın lastiğini örtecek kadar su bırakın, pompayı gidere tam oturtup 15-20 kez kuvvetlice basıp çekin."),
     ("h3", "3. Sıcak su (yalnızca yağ tıkanıklığında)", "Mutfak evyesinde tıkanıklık yağdan ise çok sıcak musluk suyu yağı yumuşatabilir. Kaynar su dökmeyin; plastik borularda ve bağlantılarda deformasyona yol açabilir."),
     ("h3", "4. Sifonu sökmek", "Lavabonun altındaki kıvrımlı parça sifondur. Altına bir kova koyup elle çevrilen somunları gevşetin, sifonu çıkarıp içini temizleyin. Takarken contaların yerine oturduğundan emin olun; yoksa sızdırır."),
     ("h3", "5. Spiral (yay) ile açmak", "Sifon temizse tıkanıklık ilerdedir. Hırdavatçılarda satılan el spiralini gider ağzından ya da sifon yerinden yavaşça ilerletip çevirin; takıldığı yerde ileri-geri hareketle birikintiyi dağıtın."),
     ("dikkat", "Spirali zorlamayın. Takılıp ilerlemiyorsa boru bir dirsekte dönüyor ya da tıkanıklık sert bir cisim olabilir; zorlamak boruyu çizebilir ya da bağlantıyı yerinden oynatabilir.")]),
   ("Karbonat ve sirke işe yarar mı?", [
     "İnternette en çok önerilen yöntem bu, o yüzden açık konuşalım: karbonat ve sirkenin köpürmesi gözle görülür ama boruyu mekanik olarak açmaz. Hafif bir kokuyu ya da süzgece yakın ince bir sabun tabakasını gidermeye yardımcı olabilir; yağla, saç yumağıyla ya da bina kolonundaki bir tıkanıklıkla baş edemez.",
     "Denemek isterseniz zararı yok; ama 15-20 dakika sonra su hâlâ gitmiyorsa daha fazla dökmeyin, yukarıdaki mekanik yöntemlere geçin."]),
   ("Tuz ruhu, kostik, çamaşır suyu: neden dökmemelisiniz?", [
     "Tıkalı lavaboya kimyasal dökmek en sık yapılan ve en riskli hata. Tuz ruhu ile çamaşır suyu karışırsa zehirli gaz çıkar; kapalı bir banyoda bu ciddi bir tehlikedir. Kostik ve güçlü asitler eski metal borulara ve contalara zarar verebilir.",
     "Bir de şu var: tıkanıklık açılmazsa kimyasal giderin içinde bekler. Sonra pompa ya da makineyle müdahale edildiğinde geri sıçrayıp yanığa yol açabilir.",
     ("dikkat", "Kimyasal döktüyseniz pompa kullanmayın ve ustaya mutlaka söyleyin.")]),
   ("Mutfak evyesi tıkanırsa ne yapmalı?", [
     "Mutfak tıkanıklığının neredeyse tek sebebi yağdır. Yağ sıcakken akar, borunun soğuk bölümünde donar ve çepere yapışır. Evyede pompa ve sıcak su ilk denenecek yöntemdir; çift gözlü evyede pompalarken diğer gözün giderini kapatmayı unutmayın.",
     "Bulaşık makinesi çalışınca evye doluyorsa tıkanıklık makinenin bağlandığı noktanın ilerisindedir; bu durumda sifonu sökmek genellikle yetmez."]),
   ("Ne zaman usta çağırmalısınız?", [
     ("liste", ["Birden fazla gider aynı anda yavaşladıysa", "Alt kattaki komşunun giderinden su geliyorsa",
                "Sifonu söktünüz, temizlediniz ama su yine gitmiyorsa", "Giderden sürekli fokurdama sesi ve koku geliyorsa",
                "Kimyasal döktünüz ve gider hâlâ tıkalıysa", "Aynı lavabo birkaç haftada bir yeniden tıkanıyorsa"]),
     "Bu durumlarda tıkanıklık evdeki aletlerin ulaşamayacağı bir yerdedir. [[hizmet:tikali-gider-acma|Tıkalı gider açma]] hizmetimizde gideri kırmadan makineyle açıyor, gerekirse [[hizmet:kamerali-goruntuleme|kamerayla]] hattın içine bakıyoruz. Sorun giderilmeden ücret almıyoruz."]),
   ("Lavabo tıkanmasın diye neler yapabilirsiniz?", [
     ("liste", ["Yemek yağını evyeye dökmeyin; soğuyunca kâğıt havluyla silip çöpe atın.", "Banyo lavabosuna saç tutucu süzgeç takın.",
                "Haftada bir giderden bir süre sıcak musluk suyu akıtın.", "Kahve telvesi ve yemek artığını gidere değil çöpe atın."])]),
  ],
  "sss": [("Lavabo tıkanırsa ne yapmalıyım?", "Önce su dökmeyi bırakın, süzgeci temizleyin, ardından taşma deliğini kapatıp pompayla deneyin. Olmazsa sifonu söküp temizleyin. Su hâlâ gitmiyorsa tıkanıklık ilerdedir ve usta gerekir."),
          ("Tıkalı gideri kendim açabilir miyim?", "Tıkanıklık süzgecin ya da sifonun hemen altındaysa evet. Duvar içindeki boruda ya da bina kolonundaysa evdeki aletler oraya ulaşmaz."),
          ("Lavabo açmanın en kolay yolu nedir?", "Süzgeci temizlemek ve taşma deliğini kapatarak pompa kullanmak. Bu ikisi işe yaramazsa sifonu sökmek bir sonraki adımdır."),
          ("Kaynar su lavabo açar mı?", "Kaynar su önermiyoruz; plastik borulara zarar verebilir. Yağ tıkanıklığında çok sıcak musluk suyu yeterlidir.")]},

 {"slug": "tuvalet-tikanirsa-ne-yapmali", "ikon": "klozet", "gorsel": ("tuvalet-tikanikligi", "Tıkanan tuvaletten taşan suyun banyo zeminine yayılması"),
  "h1": "Tuvalet Tıkanırsa Ne Yapmalı? Klozet ve Alaturka Tuvalet Rehberi",
  "title": "Tuvalet Tıkanırsa Ne Yapmalı? Klozet ve Alaturka Tuvalet | Rehber",
  "aciklama": "Tuvalet tıkanırsa ne yapmak lazım, klozet tıkanıklığını kendiniz açabilir misiniz, alaturka tuvalet tıkanıklığı nasıl gider? Adım adım rehber.",
  "ozet": "Tuvalet tıkanınca panik olmak çok normal; ama ilk birkaç dakikada doğru şeyi yaparsanız hem taşmayı önlersiniz hem de çoğu zaman sorunu kendiniz çözersiniz. Klozet ve alaturka tuvalet için ayrı ayrı anlattık.",
  "hizmet": "tuvalet-tikanikligi-acma",
  "bolum": [
   ("Tuvalet tıkanırsa ne yapmak lazım? İlk yapılacaklar", [
     ("adim", ["Sifonu bir daha çekmeyin. Su yükseliyorsa ikinci sifon taşmaya sebep olur.",
               "Rezervuarın altındaki ara musluğu saat yönünde çevirip kapatın; rezervuar sızdırıyorsa klozeti dolduramaz.",
               "Klozetin çevresine havlu serin; olası bir taşmada zemini ve alt katı korur.",
               "Klozette su çok yüksekse bir kapla bir kısmını kovaya alın; pompalarken taşma riski azalır."])]),
   ("Tuvalet tıkanıklığını kendim açabilir miyim?", [
     "Tuvalet kâğıdı fazla atıldıysa ya da yumuşak bir tıkanıklıksa evet, çoğu zaman bir klozet pompasıyla açılır. Islak mendil, ped, bez ya da düşen sert bir cisim varsa pompa genellikle cismi daha da ileri iter; bu durumda zorlamayın.",
     ("ipucu", "Banyodaki yer süzgecinden su geliyorsa ya da alt katlarda da benzer şikâyet varsa sorun klozette değil bina kolonundadır. Bunu evde açmanız mümkün değil.")]),
   ("Klozet tıkanıklığı nasıl açılır?", [
     ("h3", "Klozet pompası", "Lavabo pompası değil, alt kısmında uzantı (flanş) olan klozet pompası kullanın; klozetin gider ağzına tam oturur. Pompanın lastiğini örtecek kadar su olmalı. Yavaşça oturtup havayı çıkarın, sonra 15-20 kez kuvvetli basıp çekin."),
     ("h3", "Sıcak su ve sıvı sabun", "Yalnızca kâğıt tıkanıklığında işe yarar: klozete biraz sıvı bulaşık deterjanı ekleyin, üzerine çok sıcak (kaynar değil) musluk suyu dökün ve 15-20 dakika bekleyin. Kaynar su dökmeyin; seramik ani ısıdan çatlayabilir."),
     ("h3", "Klozet spirali", "Hırdavatçılarda klozet spirali satılır; ucu klozetin sırlı yüzeyini çizmesin diye kılıflıdır. Spirali klozetin ağzından nazikçe ilerletip çevirin."),
     ("dikkat", "Telefon, diş fırçası, oyuncak gibi sert bir cisim düştüyse pompa kullanmayın. Cisim ilerledikçe çıkarmak zorlaşır; bu durumda kamerayla yerini görüp çıkarıyoruz.")]),
   ("Alaturka tuvalet tıkanıklığı nasıl gider?", [
     "Alaturka tuvaletlerde dirsek klozete göre daha derin ve dardır; tıkanıklık genellikle bu dirseğin dibinde olur. İyi haber şu: alaturkada gider ağzı geniş olduğu için pompa ve spiral daha rahat çalışır.",
     ("h3", "Pompa ile", "Gider ağzını tam kapatan geniş bir pompa kullanın. Hazneye pompanın lastiğini örtecek kadar su doldurun ve kuvvetli, kısa hareketlerle pompalayın."),
     ("h3", "Kova ile su", "Hafif kâğıt tıkanıklığında bir kova ılık suyu yüksekten ve tek seferde gider ağzına dökmek basınç yaratıp tıkanıklığı ilerletebilir. Su yükseliyorsa ikinci kovayı dökmeyin."),
     ("h3", "Spiral ile", "Spirali gider ağzından dirseğe doğru ilerletin; alaturkanın dirseği derin olduğu için spiral birkaç kez takılabilir, zorlamadan çevirerek ilerleyin."),
     ("dikkat", "Alaturkadan klozete dönüştürülmüş tuvaletlerde altta eski, dar bir dirsek kalmış olabilir. Böyle bir tuvalet sık tıkanıyorsa evde açmak geçici çözümdür; hattı kamerayla görmek gerekir.")]),
   ("Tuvalete neler atılmamalı?", [
     ("liste", ["Islak mendil (paketinde \"tuvalete atılabilir\" yazsa bile)", "Hijyenik ped, tampon, bebek bezi", "Kâğıt havlu ve peçete",
                "Pamuk, kulak çubuğu, diş ipi", "Yemek artığı ve yağ", "Kedi kumu"]),
     "Bunların hiçbiri suda tuvalet kâğıdı gibi dağılmaz; dirseklerde ve kolonun döndüğü noktada birikip tıkaç oluşturur."]),
   ("Sifonu çekince su neden yükseliyor?", [
     "İki ihtimal var: ya klozetin kendi dirseği tıkalıdır ya da klozetten sonraki hat ya da bina kolonu doludur. Sadece sizin tuvaletinizde oluyorsa çoğunlukla klozettir. Banyodaki diğer giderler de fokurduyor, yer süzgecinden su geliyorsa sorun ileridedir."]),
   ("Ne zaman usta çağırmalısınız?", [
     ("liste", ["Pompa ile 2-3 denemede sonuç alamadıysanız", "Sert bir cisim düştüyse", "Yer süzgecinden ya da başka giderden su geliyorsa",
                "Alt katlarda da şikâyet varsa", "Tuvalet sık sık tıkanıyorsa"]),
     "[[hizmet:tuvalet-tikanikligi-acma|Tuvalet tıkanıklığı açma]] hizmetimizde çoğu durumda klozeti sökmeden açıyoruz; sökmek gerekirse contasını yenileyip yerine takıyoruz. Ödemeyi iş bitince alıyoruz."]),
  ],
  "sss": [("Tuvalet tıkanırsa ne yapmalıyım?", "Sifonu tekrar çekmeyin, rezervuarın ara musluğunu kapatın, klozetin çevresine havlu serin ve klozet pompasıyla deneyin. Sert bir cisim düştüyse pompa kullanmayın."),
          ("Alaturka tuvalet tıkanıklığı nasıl gider?", "Geniş bir pompa ya da spiral ile çoğu zaman açılır. Hafif kâğıt tıkanıklığında bir kova ılık suyu tek seferde dökmek işe yarayabilir; su yükseliyorsa devam etmeyin."),
          ("Tuvalete kaynar su dökülür mü?", "Hayır. Seramik ani ısıdan çatlayabilir; çok sıcak musluk suyu yeterlidir."),
          ("Islak mendil tuvaleti tıkar mı?", "Evet. Tuvalet kâğıdı gibi suda dağılmaz; tuvalet tıkanıklığının en sık sebeplerinden biridir.")]},

 {"slug": "gider-acma-aparati", "ikon": "anahtar", "gorsel": ("kocaeli-gider-acma", "Banyoda kullanılan elektrikli gider açma makinesi"),
  "h1": "Gider Açma Aparatı: Çeşitleri, Nereden Satın Alınır, Nasıl Kullanılır?",
  "title": "Gider Açma Aparatı Nereden Satın Alınır? Çeşitleri ve Kullanımı",
  "aciklama": "Gider açma aparatı nereden satın alınır, hangi aparat hangi tıkanıklıkta işe yarar, nasıl kullanılır? Pompa, spiral ve şerit aparatlar için rehber.",
  "ozet": "Evde bir gider açma aparatı bulundurmak mantıklı; küçük tıkanıklıkları usta çağırmadan çözersiniz. Hangi aparatın ne işe yaradığını, nereden alabileceğinizi ve nasıl kullanmanız gerektiğini anlattık. Bir not: biz aparat satmıyoruz :) Bu yazı tamamen bilgi amaçlı.",
  "hizmet": "tikali-gider-acma",
  "bolum": [
   ("Gider açma aparatı nedir?", [
     "Gider açma aparatı, tıkanan lavabo, duş, küvet ya da tuvalet giderini kimyasal kullanmadan, mekanik olarak açmaya yarayan el aletlerinin genel adıdır. Pompa, plastik şerit ve el spirali en yaygın olanlarıdır. Bizim kullandığımız elektrikli makineler ise bunların profesyonel ve çok daha güçlü versiyonlarıdır."]),
   ("Gider açma aparatı çeşitleri", [
     ("h3", "Pompa (vantuz)", "En temel aparat. Lavabo ve evye için düz ağızlı, klozet için alt kısmı uzantılı (flanşlı) modeller vardır. Yumuşak ve yakın tıkanıklıklarda işe yarar."),
     ("h3", "Plastik dişli şerit", "Üzerinde küçük dişler olan ince, esnek plastik şerittir. Gidere sokup çekince saç yumağını yakalayıp çıkarır. Banyo lavabosu ve duş gideri için çok pratiktir."),
     ("h3", "El spirali (yay)", "Metal yay biçiminde, ucu ve bir çevirme kolu olan aparattır. Gider ağzından ya da sifon yerinden ilerletilip çevrilerek daha derindeki tıkanıklığa ulaşır. Klozet için ucu kılıflı ayrı modeli vardır."),
     ("h3", "Basınçlı hava aparatı", "Gidere hava basıncı vererek tıkanıklığı iter. Dikkatli kullanılmalı; eski ve zayıf bağlantılarda sızıntıya yol açabilir."),
     ("h3", "Elektrikli gider açma makinesi", "Ustaların kullandığı motorlu makinelerdir; uzun hatlarda, kolonda ve rögarda çalışır. Ev kullanımı için gerekli değildir.")]),
   ("Gider açma aparatı nereden satın alınır?", [
     "Pompa ve plastik şerit gibi basit aparatları hırdavatçılarda, yapı marketlerde ve büyük marketlerin temizlik reyonlarında bulabilirsiniz. El spirali ve klozet spirali daha çok hırdavatçılarda ve yapı marketlerde satılır. İnternetteki pazar yerlerinde de hepsinin çeşitli boyları var.",
     ("ipucu", "Spiral alırken boyuna bakın: banyo lavabosu için kısa bir spiral yeterli; mutfak ve duş gideri için biraz daha uzun bir model işinizi görür. Çok uzun spiral ev kullanımında kontrolü zorlaştırır.")]),
   ("Hangi aparat hangi tıkanıklıkta işe yarar?", [
     ("tablo", ["Tıkanıklık", "Önerilen aparat"],
      [["Banyo lavabosu, duş gideri (saç)", "Plastik dişli şerit"], ["Lavabo ve mutfak evyesi", "Lavabo pompası, ardından el spirali"],
       ["Klozet (kâğıt)", "Flanşlı klozet pompası"], ["Klozet (daha derin)", "Ucu kılıflı klozet spirali"],
       ["Alaturka tuvalet", "Geniş ağızlı pompa ya da el spirali"], ["Bina kolonu, rögar, bahçe hattı", "Ev aparatı yetmez; usta gerekir"]])]),
   ("Gider açma aparatı nasıl kullanılır?", [
     ("adim", ["Eldiven takın ve gider çevresini havluyla koruyun.",
               "Önce süzgeci ya da tıpayı çıkarın; tıkanıklık bazen tam altındadır.",
               "Spiral kullanıyorsanız ucunu gidere sokup kolunu çevirerek yavaşça ilerletin.",
               "Takıldığı yerde ileri-geri ve döndürerek birikintiyi dağıtın ya da yakalayın.",
               "Spirali çevirerek geri çekin, ardından bir süre sıcak musluk suyu akıtıp akışı test edin."])]),
   ("Aparat kullanırken nelere dikkat etmeli?", [
     ("liste", ["Giderde kimyasal varsa aparat kullanmayın; geri sıçrayabilir.", "Spirali zorlamayın; takılıyorsa boru dönüyor ya da sert bir cisim var demektir.",
                "Klozette metal ucu çıplak spiral kullanmayın; sırlı yüzeyi çizer.", "Pompalarken lavabonun taşma deliğini kapatın."]),
     "Aparatla iki üç denemede sonuç alamıyorsanız tıkanıklık evdeki aletlerin ulaşamayacağı yerdedir. [[hizmet:tikali-gider-acma|Tıkalı gider açma]] ve [[hizmet:tuvalet-tikanikligi-acma|tuvalet tıkanıklığı açma]] için 7/24 arayabilirsiniz."]),
  ],
  "sss": [("Gider açma aparatı nereden satın alınır?", "Hırdavatçılardan, yapı marketlerden, büyük marketlerin temizlik reyonlarından ve internetteki pazar yerlerinden alınabilir."),
          ("En kullanışlı gider açma aparatı hangisi?", "Saç tıkanıklığı için plastik dişli şerit, lavabo ve evye için pompa, daha derin tıkanıklık için el spirali pratiktir."),
          ("Gider açma aparatı tuvalette kullanılır mı?", "Evet ama klozet için flanşlı pompa ya da ucu kılıflı klozet spirali kullanın; çıplak metal uç klozeti çizer."),
          ("Aparatla açılmıyorsa ne yapmalı?", "Zorlamayın. Tıkanıklık duvar içindeki boruda ya da bina kolonundadır; makineyle açılması gerekir.")]},
]

REHBER_GIRIS = ("Tıkanıklık olduğunda herkesin aklına aynı sorular geliyor: Kendim açabilir miyim? Ne yapmamalıyım? Ne zaman usta çağırmalıyım? "
                "Bu rehberde müşterilerimizin bize en sık sorduğu soruları, sahada gördüklerimize dayanarak dürüstçe cevapladık. "
                "Evde çözebileceğiniz durumu açıkça söylüyoruz; usta gerektiren durumu da :)")

# ── Gider açma ustası çağırırken dikkat edilecekler (kullanıcı 2026-10-05: "sahte, cihazı olmadan gider açacağını iddia eden
#    kişiler tesisatınıza zarar verebilir ve masrafınız büyüyebilir") — ⛔ kimseyi isimle hedef alma, genel uyarı dili.
USTA_DIKKAT_GIRIS = [
 "Tıkanıklık acil olunca insan ilk bulduğu numarayı arıyor; bunu çok iyi anlıyoruz. Ama sahada sık gördüğümüz bir durum var: cihazı olmadan gider açacağını iddia eden kişiler tesisatınıza zarar verebiliyor ve küçük bir tıkanıklığın masrafı büyüyebiliyor. Kimi çağırırsanız çağırın, aşağıdakilere dikkat edin.",
 "Gider açma işi basit görünür ama yanlış yapıldığında boruyu çatlatabilir, contayı kaçırtabilir ya da gereksiz yere fayans kırdırabilir. Cihazı olmadan, sadece kimyasalla ya da tahminle iş yapanlar tesisatınıza zarar verebilir ve masrafınız büyüyebilir. Usta çağırmadan önce şunlara dikkat etmenizi öneririz.",
 "Bize gelen çağrıların bir kısmı, daha önce başka birinin müdahale ettiği ve sorunun büyüdüğü işler. Cihazı olmadan gider açacağını iddia eden kişiler tesisatınıza zarar verebilir; o yüzden kimi çağıracağınızı seçerken birkaç soruyu baştan sormanız sizi büyük masraftan kurtarır.",
]
USTA_DIKKAT = [
 ("Fiyatı işe başlamadan sorun", "Usta durumu gördükten sonra fiyatı söylemeli ve onayınızı almadan işe başlamamalı. \"Bakarız, iş bitince konuşuruz\" diyen birine dikkat edin."),
 ("Hangi cihazla geleceğini sorun", "Gider açma makine işidir: spiral makinesi, gerektiğinde basınçlı yıkama ve kamera. Cihazı olmadan gider açacağını iddia eden kişiler tesisatınıza zarar verebilir ve masrafınız büyüyebilir."),
 ("Kırma önerisine hemen evet demeyin", "\"Burayı kırmak lazım\" deniyorsa önce kamera görüntüsü isteyin. Çoğu tıkanıklık kırmadan açılır; kırmak gerekiyorsa bile yalnızca sorunlu nokta kırılmalıdır."),
 ("Sadece kimyasalla gelenlere dikkat", "Kimyasal kalıcı çözüm değildir; eski borulara ve contalara zarar verebilir, tıkanıklık açılmazsa giderde bekleyip sonraki müdahaleyi tehlikeli hâle getirir."),
 ("Adresi ve telefonu belli birini seçin", "Sorun tekrar ederse ulaşabileceğiniz, adresi belli bir firmayla çalışın. Bizim ofisimiz Başiskele'de, Kılıçarslan Mah. Hürriyet Cad. No:1'de; isterseniz uğrayabilirsiniz."),
 ("Ödemeyi iş bitince yapın", "Suyun gittiğini kendi gözünüzle görmeden ödeme yapmayın. Biz de sorun tamamen giderilmeden ücret talep etmiyor, ödemeyi işlem tamamlandıktan sonra alıyoruz."),
]
