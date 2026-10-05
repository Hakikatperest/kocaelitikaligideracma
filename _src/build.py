# -*- coding: utf-8 -*-
"""
kocaelitikaligideracma.com statik site üreticisi.
  python3 _src/media.py   (yalnızca görsel değişince)
  python3 _src/build.py && python3 _src/denetim.py
⛔ Üretilen HTML'i elle düzenleme; veri _src/data.py'de, şablon burada.

Yapı (kullanıcı kararı 2026-10-05): 7 ilçe × 4 hizmet
  /                                anasayfa (Kocaeli geneli)
  /<hizmet>/                       4 hizmet sayfası
  /<ilce>-gider-acma/              7 ilçe sayfası (ilçe hub'ı, 4 hizmete dağıtır)
  /<ilce>-<hizmet>/                28 ilçe × hizmet sayfası
  /hizmet-bolgeleri/ /iletisim/ /gizlilik-politikasi/ /404.html
"""
import os, json, hashlib, html, shutil
from urllib.parse import quote
from PIL import Image
import data as D

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = D.SITE
ALAN = S["alan"]
ILCE = {i["slug"]: i for i in D.ILCELER}
HIZ = {h["slug"]: h for h in D.HIZMETLER}
ONEK = ""   # sayfa derinliğine göre göreli yol öneki

# ── yardımcılar ─────────────────────────────────────────────────────────────
def e(t): return html.escape(str(t), quote=True)
def ic(yol=""): return (ONEK + yol) if (ONEK + yol) else "./"
def kucuk(s): return s.replace("I", "ı").replace("İ", "i").lower()
def ek(i, hal="loc"): return i["ad"] + D.ILCE_EK[i["slug"]][{"loc": 0, "dat": 1, "gen": 2, "abl": 3}[hal]]
def tohum(*p): return int(hashlib.md5("|".join(p).encode()).hexdigest()[:8], 16)
def sec(liste, *p): return liste[tohum(*p) % len(liste)]
def karistir(liste, *p):
    t = tohum(*p); l = list(liste); son = []
    while l:
        t = (t * 1103515245 + 12345) & 0x7FFFFFFF
        son.append(l.pop(t % len(l)))
    return son
def surum(g):
    with open(os.path.join(KOK, g), "rb") as f: return g + "?v=" + hashlib.md5(f.read()).hexdigest()[:8]
def ve_liste(l): return ", ".join(l[:-1]) + " ve " + l[-1] if len(l) > 1 else l[0]

ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"
def tr_sira(i): return [ALFABE.index(c) if c in ALFABE else 99 for c in kucuk(i["ad"])]
ILCE_SIRALI = sorted(D.ILCELER, key=tr_sira)

def ilce_yolu(i, h=None): return f"{i['slug']}-{h['slug']}/" if h else f"{i['slug']}-gider-acma/"
def hiz_yolu(h): return f"{h['slug']}/"

def yer(metin, i, h=None):
    loc, dat, gen, abl = D.ILCE_EK[i["slug"]]
    return metin.format(ad=i["ad"], loc=loc, dat=dat, gen=gen, abl=abl,
                        kisa=kucuk(h["kisa"]) if h else "", ozet=h["ozet"] if h else "")

# ── ikonlar (satır içi SVG) ─────────────────────────────────────────────────
IK = {
 "tel": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/>',
 "wa": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/>',
 "saat": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 18a8 8 0 1 1 0-16 8 8 0 0 1 0 16zm.5-13H11v6l5.2 3.2.8-1.3-4.5-2.7z"/>',
 "konum": '<path d="M12 2a7 7 0 0 0-7 7c0 5.3 7 13 7 13s7-7.7 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/>',
 "kalkan": '<path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5l-8-3zm-1.2 14.2-3.5-3.5 1.4-1.4 2.1 2.1 4.9-4.9 1.4 1.4-6.3 6.3z"/>',
 "hiz": '<path d="M13 2 3 14h7l-1 8 10-12h-7l1-8z"/>',
 "damla": '<path d="M12 2.7S5 10.4 5 15a7 7 0 0 0 14 0c0-4.6-7-12.3-7-12.3z"/>',
 "klozet": '<path d="M6 2h7a1 1 0 0 1 1 1v6h5a1 1 0 0 1 1 1c0 3.9-2.5 7.2-6 8.4V21a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1v-3.2A9 9 0 0 1 4 11V10a1 1 0 0 1 1-1V3a1 1 0 0 1 1-1zm1 2v5h5V4H7zm-1 7c.4 3 2.6 5.3 5.5 5.9l.5.1V20h0v-3l.5-.1A7 7 0 0 0 17.9 11H6z"/>',
 "rogar": '<path d="M12 3C6.5 3 2 5.2 2 8v8c0 2.8 4.5 5 10 5s10-2.2 10-5V8c0-2.8-4.5-5-10-5zm0 2c4.6 0 8 1.6 8 3s-3.4 3-8 3-8-1.6-8-3 3.4-3 8-3zm-5 2.3v1.4h2V7.3H7zm4-.5v1.4h2V6.8h-2zm4 .5v1.4h2V7.3h-2zM4 11.1C5.8 12.3 8.7 13 12 13s6.2-.7 8-1.9V16c0 1.4-3.4 3-8 3s-8-1.6-8-3v-4.9z"/>',
 "kamera": '<path d="M4 6h11a2 2 0 0 1 2 2v1.5l4-2.5v10l-4-2.5V16a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2zm5.5 2.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zm0 2a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3z"/>',
 "tik": '<path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/>',
 "ok": '<path d="M12 4l-1.4 1.4 5.6 5.6H4v2h12.2l-5.6 5.6L12 20l8-8z"/>',
 "menu": '<path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/>',
 "uyari": '<path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/>',
 "lira": '<path d="M9 3h2v4.1l4-1.6.7 1.9L11 9.2v1.6l4-1.6.7 1.9L11 12.9V19a6 6 0 0 0 6-6h2a8 8 0 0 1-8 8H9v-7.3l-2.3.9-.7-1.9 3-1.2V10.9l-2.3.9-.7-1.9 3-1.2V3z"/>',
}
def svg(ad, sinif="ik"):
    return f'<svg class="{sinif}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{IK[ad]}</svg>'

# ── görsel ──────────────────────────────────────────────────────────────────
def gorsel(taban, alt, sinif="", oncelik=False, boy="(min-width:980px) 520px, 100vw"):
    genler = sorted(int(f.rsplit("-", 1)[1][:-5]) for f in os.listdir(os.path.join(KOK, "images"))
                    if f.startswith(taban + "-") and f.endswith(".webp") and f.rsplit("-", 1)[1][:-5].isdigit()
                    and f.rsplit("-", 1)[0] == taban)
    parca = []; olcu = None
    for g in genler:
        yol = f"images/{taban}-{g}.webp"
        w, h = Image.open(os.path.join(KOK, yol)).size
        parca.append(f"{ic(yol)} {w}w"); olcu = (w, h)
    yukle = 'fetchpriority="high"' if oncelik else 'loading="lazy" decoding="async"'
    return (f'<img class="{sinif}" src="{ic(f"images/{taban}-{genler[-1]}.webp")}" srcset="{", ".join(parca)}" '
            f'sizes="{boy}" width="{olcu[0]}" height="{olcu[1]}" alt="{e(alt)}" {yukle}>')

def galeri(oge, baslik):
    return (f'<section class="blok"><h2>{e(baslik)}</h2><div class="galeri">' +
            "".join(f'<figure>{gorsel(t, a, boy="(min-width:980px) 280px, 50vw")}<figcaption>{e(a)}</figcaption></figure>'
                    for t, a in oge) + '</div></section>')

# ── düğmeler ────────────────────────────────────────────────────────────────
def tel_btn(metin=None, sinif="dg dg-ara"):
    metin = metin or f"Hemen Ara: {S['tel_goster']}"
    return f'<a class="{sinif}" href="tel:{S["tel_link"]}">{svg("tel")}<span>{e(metin)}</span></a>'

def wa_btn(mesaj, metin="WhatsApp'tan Yaz", sinif="dg dg-wa"):
    return (f'<a class="{sinif}" href="https://wa.me/{S["wa"]}?text={quote(mesaj)}" target="_blank" '
            f'rel="noopener">{svg("wa")}<span>{e(metin)}</span></a>')

def wa_mesaj(h=None, i=None):
    if h and i: return f"Merhaba, {i['ad']} için {kucuk(h['kisa'])} hizmeti almak istiyorum."
    if h: return f"Merhaba, {kucuk(h['kisa'])} hizmeti almak istiyorum."
    if i: return f"Merhaba, {i['ad']} için gider açma hizmeti almak istiyorum."
    return "Merhaba, tıkalı gider açma hizmeti almak istiyorum."

# ── iskelet ─────────────────────────────────────────────────────────────────
def ads_head():
    a = D.ADS
    if not a["etiket"]: return ""
    ayar = json.dumps({"etiket": a["etiket"], "tel": a["tel"], "wa": a["wa"]})
    return (f'<script async src="https://www.googletagmanager.com/gtag/js?id={a["etiket"]}"></script>\n'
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
            f"gtag('js',new Date());gtag('config','{a['etiket']}');window.W4_ADS={ayar};</script>\n")

def head(baslik, aciklama, yol, sema=None, robots="index,follow", og="images/og-kocaeli-tikali-gider-acma.jpg"):
    kanonik = ALAN + "/" + yol
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n' for s in (sema or []))
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{ads_head()}<title>{e(baslik)}</title>
<meta name="description" content="{e(aciklama)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{kanonik}">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{e(S['marka'])}">
<meta property="og:title" content="{e(baslik)}">
<meta property="og:description" content="{e(aciklama)}">
<meta property="og:url" content="{kanonik}">
<meta property="og:image" content="{ALAN}/{og}">
<meta name="theme-color" content="#060B14">
<link rel="icon" href="{ic('favicon.ico')}" sizes="48x48">
<link rel="icon" type="image/png" sizes="192x192" href="{ic('images/favicon-192.png')}">
<link rel="apple-touch-icon" href="{ic('images/favicon-180.png')}">
<link rel="preload" href="{ic('assets/fonts/pjs-var-tr.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{ic(surum('assets/css/site.css'))}">
{ld}</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>
"""

def logo():
    return (f'<a class="logo" href="{ic()}" aria-label="{e(S["marka"])} anasayfa">'
            f'<img src="{ic("images/favicon-96.png")}" width="42" height="42" alt="">'
            f'<span class="logo-ad"><b>KOCAELİ</b><small>TIKALI GİDER AÇMA</small></span></a>')

def ust(aktif=""):
    hiz = "".join(f'<a{" class=aktif" if aktif == h["slug"] else ""} href="{ic(hiz_yolu(h))}">{svg(h["ikon"])}{e(h["ad"])}</a>'
                  for h in D.HIZMETLER)
    ilc = "".join(f'<a href="{ic(ilce_yolu(i))}">{svg("konum")}{e(i["ad"])}</a>' for i in ILCE_SIRALI)
    return f"""<header class="ust">
 <div class="kap ust-ic">
  {logo()}
  <nav class="menu" id="menu" aria-label="Ana menü">
   <div class="menu-grup"><span class="menu-baslik">Hizmetler</span><div class="menu-alt">{hiz}</div></div>
   <div class="menu-grup"><span class="menu-baslik">İlçeler</span><div class="menu-alt">{ilc}</div></div>
   <a href="{ic('hizmet-bolgeleri/')}"{' class="aktif"' if aktif=='bolge' else ''}>Hizmet Bölgeleri</a>
   <a href="{ic('iletisim/')}"{' class="aktif"' if aktif=='iletisim' else ''}>İletişim</a>
  </nav>
  <div class="ust-sag">
   <a class="ust-tel" href="tel:{S['tel_link']}">{svg('saat')}<span><small>7/24 Hizmet</small><b>{S['tel_goster']}</b></span></a>
   <button class="menu-ac" type="button" aria-controls="menu" aria-expanded="false" aria-label="Menüyü aç">{svg('menu')}</button>
  </div>
 </div>
</header>
<main id="icerik">
"""

def kirinti(parcalar):
    li, ld = [], []
    for n, (ad, yol) in enumerate(parcalar, 1):
        if yol is None:
            li.append(f'<li aria-current="page">{e(ad)}</li>')
            ld.append({"@type": "ListItem", "position": n, "name": ad})
        else:
            li.append(f'<li><a href="{ic(yol)}">{e(ad)}</a></li>')
            ld.append({"@type": "ListItem", "position": n, "name": ad, "item": ALAN + "/" + yol})
    return (f'<nav class="kirinti" aria-label="Sayfa yolu"><ol>{"".join(li)}</ol></nav>',
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld})

def w4_imza():
    return ('<div class="w4"><div class="w4-bag"><span class="w4-etiket">Web Tasarım:</span>'
            '<a class="w4-ad" href="https://www.web4medya.com/" target="_blank" rel="noopener">'
            'Web<span class="w4-d">4</span>Medya</a></div></div>')

def alt():
    hiz = "".join(f'<li><a href="{ic(hiz_yolu(h))}">{e(h["ad"])}</a></li>' for h in D.HIZMETLER)
    ilc = "".join(f'<li><a href="{ic(ilce_yolu(i))}">{e(i["ad"])} gider açma</a></li>' for i in ILCE_SIRALI)
    return f"""</main>
<footer class="alt">
 <div class="kap alt-izgara">
  <div class="alt-marka">
   {logo()}
   <p>İzmit, Başiskele, Gölcük, Derince, Körfez, Kartepe ve Karamürsel'de tıkalı gider açma, tuvalet tıkanıklığı açma, rögar temizleme ve kameralı gider görüntüleme. 7 gün 24 saat.</p>
   <p class="alt-sat">{svg('tel')}<a href="tel:{S['tel_link']}">{S['tel_goster']}</a></p>
   <p class="alt-sat">{svg('konum')}<a href="{S['harita']}" target="_blank" rel="noopener">{e(S['adres'])}</a></p>
   <p class="alt-sat">{svg('saat')}<span>7 gün 24 saat</span></p>
  </div>
  <div><h2 class="alt-b">Hizmetler</h2><ul class="alt-liste">{hiz}</ul></div>
  <div><h2 class="alt-b">İlçeler</h2><ul class="alt-liste">{ilc}<li><a href="{ic('hizmet-bolgeleri/')}">Tüm hizmet bölgeleri</a></li></ul></div>
 </div>
 <div class="kap alt-son">
  <p>© 2026 {e(S['marka'])} · <a href="{ic('gizlilik-politikasi/')}">Gizlilik Politikası</a> · <a href="{ic('iletisim/')}">İletişim</a></p>
 </div>
 {w4_imza()}
</footer>
<div class="dock" id="dock">
 {tel_btn('Hemen Ara', 'dg dg-ara')}
 {wa_btn(wa_mesaj(), 'WhatsApp')}
</div>
<script src="{ic(surum('assets/js/app.js'))}" defer></script>
</body>
</html>
"""

# ── şema ────────────────────────────────────────────────────────────────────
def isletme():
    return {"@type": "Plumber", "@id": ALAN + "/#isletme", "name": S["marka"], "url": ALAN + "/",
            "telephone": S["tel_link"], "image": ALAN + "/images/og-kocaeli-tikali-gider-acma.jpg",
            "logo": ALAN + "/images/favicon-512.png",
            "address": {"@type": "PostalAddress", **S["adres_sema"]},
            "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
                "opens": "00:00", "closes": "23:59"},
            "areaServed": [{"@type": "City", "name": f"{i['ad']}, Kocaeli"} for i in D.ILCELER]}

def sema_hizmet(ad, tur, i=None, yol=""):
    return {"@context": "https://schema.org", "@type": "Service", "name": ad, "serviceType": tur,
            "provider": {"@type": "Plumber", "@id": ALAN + "/#isletme", "name": S["marka"], "telephone": S["tel_link"]},
            "areaServed": {"@type": "City", "name": f"{i['ad']}, Kocaeli"} if i else {"@type": "AdministrativeArea", "name": "Kocaeli"},
            "url": ALAN + "/" + yol}

def sema_sss(sorular):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in sorular]}

# ── ortak bloklar ───────────────────────────────────────────────────────────
def guven():
    oge = [("saat", "7/24 hizmet", "Gece, hafta sonu ve bayramda da arayabilirsiniz."),
           ("hiz", "Ortalama 30 dakika", "Kocaeli'de adrese ortalama 30 dakikada ulaşıyoruz."),
           ("kamera", "Kırmadan, kameralı", "Tıkanıklığın yerini kamerayla görüp kırmadan açıyoruz."),
           ("lira", "Fiyat işten önce", "Usta yerinde baktıktan sonra, işe başlamadan fiyatı söylüyor.")]
    return '<ul class="guven">' + "".join(
        f'<li><span class="guven-ik">{svg(i)}</span><div><b>{e(b)}</b><span>{e(m)}</span></div></li>' for i, b, m in oge) + "</ul>"

def sss_html(sorular, baslik="Sık Sorulan Sorular"):
    oge = "".join(f'<details class="sss-oge"><summary>{e(s)}</summary><p>{e(c)}</p></details>' for s, c in sorular)
    return f'<section class="blok" id="sss"><h2>{e(baslik)}</h2><div class="sss">{oge}</div></section>'

def cta(baslik, metin, h=None, i=None):
    return f"""<section class="cta"><div class="kap cta-ic">
 <div><h2>{e(baslik)}</h2><p>{e(metin)}</p></div>
 <div class="cta-dg">{tel_btn()}{wa_btn(wa_mesaj(h, i))}</div>
</div></section>"""

SAHNE = ('<div class="sahne" aria-hidden="true"><div class="zemin-izgara"></div>'
         '<canvas class="kabarcik"></canvas><span class="isik isik-1"></span><span class="isik isik-2"></span></div>')

def hero(etiket, h1, p, gorsel_html, kir="", h=None, i=None, sinif="hero-ic"):
    return f"""<section class="hero {sinif}">{SAHNE}<div class="kap hero-izgara">
 <div class="hero-metin">
  {kir}
  <p class="ust-etiket"><span class="nokta"></span>{e(etiket)}</p>
  <h1>{h1}</h1>
  <p class="hero-p">{e(p)}</p>
  <div class="hero-dg">{tel_btn()}{wa_btn(wa_mesaj(h, i))}</div>
 </div>
 <div class="hero-derin"><figure class="hero-gorsel" data-egim>{gorsel_html}</figure><span class="hero-golge"></span></div>
</div></section>"""

def kart_hizmet(h, i=None):
    yol = ilce_yolu(i, h) if i else hiz_yolu(h)
    ad = h["h1"].format(ad=i["ad"]) if i else h["ad"]
    return (f'<a class="hkart" data-egim href="{ic(yol)}"><span class="hkart-g">{gorsel(h["galeri"][0][0], "", boy="(min-width:980px) 280px, 100vw")}</span>'
            f'<span class="hkart-ic"><span class="hkart-ik">{svg(h["ikon"])}</span>'
            f'<b>{e(ad)}</b><span>{e(h["ozet"])}</span><em>Ayrıntılar {svg("ok")}</em></span></a>')

def ilce_kart(i):
    return (f'<a class="ikart" data-egim href="{ic(ilce_yolu(i))}">{svg("konum")}<b>{e(i["ad"])}</b>'
            f'<span>{e(", ".join(i["mahalle"][:3]))}…</span></a>')

# ── ilçe × hizmet sayfası ───────────────────────────────────────────────────
GIRIS = [
 "{ad}{loc} {kisa} için 7/24 hizmet veriyoruz. {ozet} Ekiplerimiz adrese ortalama 30 dakikada ulaşıyor.",
 "{ozet} {ad}{loc} gece ya da gündüz fark etmeden arayabilirsiniz; ekiplerimiz ortalama 30 dakikada yanınızda.",
 "{ad} ve çevresinde {kisa} işleri için 7/24 ulaşabileceğiniz bir ekibiz. {ozet} Fiyatı işe başlamadan söylüyoruz.",
]
BOLGE_H2 = [
 "{ad}{loc} {kisa}: binaları ve hatları tanıyoruz",
 "{ad}{loc} {kisa} işlerinde neye dikkat ediyoruz?",
 "{ad}{abl} gelen çağrılarda en sık ne görüyoruz?",
]
ISLER_H2 = {
 "tikali-gider-acma":        "{ad}{loc} açtığımız giderler",
 "tuvalet-tikanikligi-acma": "{ad} tuvalet ve klozet tıkanıklığı: yaptığımız işler",
 "rogar-temizleme":          "{ad}{loc} rögar açma ve yıkama işleri",
 "kamerali-goruntuleme":     "{ad}{loc} kameralı görüntülemeyle neler yapıyoruz?",
}
MAHALLE = [
 "[MAH] başta olmak üzere {ad}{gen} tüm mahallelerine {kisa} için geliyoruz. Aramada mahalle ve sokak adını söylemeniz ekibi doğru yönlendirmemizi kolaylaştırıyor.",
 "{ad}{loc} [MAH] mahallelerinden çağrı alıyoruz; listede olmayan mahalleler için de aynı şekilde geliyoruz.",
 "Hizmet verdiğimiz {ad} mahallelerinden bazıları: [MAH]. Adres tarifini telefonda netleştirip ekibi en kısa güzergâhtan gönderiyoruz.",
]
SSS_H2 = ["{ad} {kisa} hakkında sık sorulanlar", "{ad}{loc} {kisa}: sorular ve cevaplar", "Sık sorulan sorular"]

def mahalle_cumle(i, h=None, *p):
    return yer(sec(MAHALLE, i["slug"], *p), i, h).replace("[MAH]", ve_liste(i["mahalle"][:6]))

def baglanti_agi(i, h):
    a1 = "".join(f'<li><a href="{ic(ilce_yolu(i, x))}">{e(x["h1"].format(ad=i["ad"]))}</a></li>'
                 for x in D.HIZMETLER if x["slug"] != h["slug"])
    a1 += f'<li><a href="{ic(ilce_yolu(i))}">{e(i["ad"])} gider açma: tüm hizmetler</a></li>'
    a2 = "".join(f'<li><a href="{ic(ilce_yolu(ILCE[k], h))}">{e(h["h1"].format(ad=ILCE[k]["ad"]))}</a></li>' for k in i["komsu"])
    diger = [x for x in ILCE_SIRALI if x["slug"] != i["slug"] and x["slug"] not in i["komsu"]]
    a3 = " · ".join(f'<a href="{ic(ilce_yolu(k, h))}">{e(k["ad"])}</a>' for k in diger)
    return f"""<section class="blok ag">
 <div class="ag-kol"><h2>{e(ek(i))} diğer hizmetlerimiz</h2><ul class="ag-liste">{a1}</ul></div>
 <div class="ag-kol"><h2>Yakın ilçelerde {e(kucuk(h['kisa']))}</h2><ul class="ag-liste">{a2}</ul>
  <p class="ag-not">Diğer ilçeler: {a3} · <a href="{ic(hiz_yolu(h))}">{e(h['ad'])}</a></p></div>
</section>"""

def ilce_hizmet_sayfasi(i, h):
    yol = ilce_yolu(i, h); s = i["slug"]; hs = h["slug"]
    H1 = h["h1"].format(ad=i["ad"])
    giris = yer(sec(GIRIS, s, hs, "giris"), i, h)
    bolge_p = [i[a] for a in h["alan"]] + [yer(D.KOPRU[hs], i, h), i["saha"]]
    belirti = karistir(h["belirti"], s, hs, "b")[:5]
    isler = karistir(h["isler"], s, hs, "i")[:4]
    oneri = karistir(h["oneri"], s, hs, "o")[:3]
    genel = [i[a] for a in ("yapi", "gider", "rogar") if a not in h["alan"]]
    gal = karistir(h["galeri"], s, hs, "g")
    sss_tum = [(yer(q, i, h), c) for q, c in h["sss"]]
    sss = [sss_tum[0]] + karistir(sss_tum[1:], s, hs, "s")[:3]
    kir_html, kir_ld = kirinti([("Anasayfa", ""), (f"{i['ad']} Gider Açma", ilce_yolu(i)), (h["ad"], None)])
    baslik = h["title"].format(ad=i["ad"])
    aciklama = f"{i['ad']} {kucuk(h['kisa'])}: {h['ozet']} 7/24, ortalama 30 dakikada adreste. {S['tel_goster']}"
    sema = [sema_hizmet(H1, h["ad"], i, yol), sema_sss(sss), kir_ld]
    return head(baslik, aciklama, yol, sema) + ust(hs) + hero(
        f"{i['ad']}, Kocaeli · 7/24", e(H1), giris, gorsel(gal[0][0], gal[0][1], oncelik=True), kir_html, h, i) + f"""
<div class="kap">{guven()}</div>
<div class="kap govde">
 <section class="blok">
  <h2>{e(yer(sec(BOLGE_H2, s, hs, 'h2'), i, h))}</h2>
  {''.join(f'<p>{e(x)}</p>' for x in bolge_p)}
 </section>
 <section class="blok">
  <h2>{e(yer('Hangi durumlarda {kisa} için aramalısınız?', i, h))}</h2>
  <ul class="tik-liste">{''.join(f'<li>{svg("tik")}<span>{e(b)}</span></li>' for b in belirti)}</ul>
 </section>
 <section class="blok">
  <h2>{e(yer(ISLER_H2[hs], i, h))}</h2>
  <div class="is-izgara">{''.join(f'<div class="is"><h3>{e(a)}</h3><p>{e(m)}</p></div>' for a, m in isler)}</div>
 </section>
 {galeri(gal[1:3], "Sahadan fotoğraflar")}
 <section class="blok kutu-vurgu">
  <h2>Usta gelene kadar ne yapabilirsiniz?</h2>
  <ol class="adim-liste">{''.join(f'<li>{e(o)}</li>' for o in oneri)}</ol>
 </section>
 <section class="blok">
  <h2>{e(yer('{ad} hakkında bilmenizde fayda olanlar', i, h))}</h2>
  {''.join(f'<p>{e(x)}</p>' for x in genel)}
  <p>{e(mahalle_cumle(i, h, hs, 'm'))}</p>
 </section>
 {sss_html(sss, yer(sec(SSS_H2, s, hs, 'sss'), i, h))}
 {baglanti_agi(i, h)}
</div>
{cta(f"{i['ad']} için usta mı lazım?", "7/24 arayabilir ya da WhatsApp'tan fotoğraf, video gönderebilirsiniz.", h, i)}
""" + alt()

# ── ilçe sayfası (hub) ──────────────────────────────────────────────────────
def ilce_sayfasi(i):
    yol = ilce_yolu(i); s = i["slug"]
    H1 = f"{i['ad']} Gider Açma Servisi"
    sss = [
     (f"{ek(i)} hangi gider açma hizmetlerini veriyorsunuz?",
      f"{ek(i)} tıkalı gider açma (lavabo, mutfak, banyo), tuvalet tıkanıklığı açma, rögar temizleme ve kameralı gider görüntüleme hizmeti veriyoruz."),
     (f"{ek(i, 'dat')} ne kadar sürede geliyorsunuz?",
      "Ekiplerimiz Kocaeli'de adrese ortalama 30 dakikada ulaşıyor. Trafik ve o anki iş yoğunluğuna göre süre değişebilir; arama sırasında tahmini süreyi söylüyoruz."),
     ("Gece ve hafta sonu çalışıyor musunuz?", "Evet. 7 gün 24 saat hizmet veriyoruz."),
     ("Fiyatı ne zaman öğrenirim?", "Usta yerinde baktıktan sonra, işe başlamadan önce fiyatı söylüyor; onayınız olmadan işe başlamıyoruz."),
    ]
    kir_html, kir_ld = kirinti([("Anasayfa", ""), ("Hizmet Bölgeleri", "hizmet-bolgeleri/"), (f"{i['ad']} Gider Açma", None)])
    baslik = f"{i['ad']} Gider Açma Servisi | Tıkanıklık, Tuvalet, Rögar · 7/24"
    aciklama = (f"{i['ad']} gider açma: tıkalı gider, tuvalet tıkanıklığı, rögar temizleme ve kameralı görüntüleme. "
                f"7/24, ortalama 30 dakikada adreste. {S['tel_goster']}")
    komsu = "".join(f'<li><a href="{ic(ilce_yolu(ILCE[k]))}">{e(ILCE[k]["ad"])} gider açma</a></li>' for k in i["komsu"])
    adres = ""
    if s == "basiskele":
        adres = (f'<p class="not">{svg("konum")}<span>Adresimiz Başiskele\'de: {e(S["adres"])}. '
                 f'<a href="{S["harita"]}" target="_blank" rel="noopener">Haritada aç</a></span></p>')
    banner_alt = f"{i['ad']} gider açma servisi, {S['tel_goster']}"
    sema = [sema_hizmet(H1, "Gider açma", i, yol), sema_sss(sss), kir_ld]
    return head(baslik, aciklama, yol, sema) + ust() + hero(
        f"{i['ad']}, Kocaeli · 7/24", e(H1),
        f"{ek(i)} tıkalı gider, tuvalet tıkanıklığı ve rögar sorunları için 7 gün 24 saat ulaşabileceğiniz ekibiz. Tıkanıklığın yerini gerektiğinde kamerayla görüp kırmadan açıyoruz; ekiplerimiz adrese ortalama 30 dakikada ulaşıyor.",
        gorsel(i["banner"], banner_alt, oncelik=True), kir_html, None, i) + f"""
<div class="kap">{guven()}</div>
<div class="kap govde">
 <section class="blok"><h2>{e(ek(i))} hizmetlerimiz</h2>
  <p class="blok-giris">Her hizmetin {e(i['ad'])} sayfasında, ilçedeki binalarda en sık karşılaştığımız durumları da anlattık.</p>
  <div class="hkart-izgara">{''.join(kart_hizmet(h, i) for h in D.HIZMETLER)}</div></section>
 <section class="blok"><h2>{e(ek(i))} gider ve rögar hatları</h2>
  {''.join(f'<p>{e(i[a])}</p>' for a in ('yapi', 'gider', 'rogar', 'saha'))}
  {adres}
 </section>
 <section class="blok"><h2>Hizmet verdiğimiz {e(i['ad'])} mahalleleri</h2>
  <ul class="mah-liste">{''.join(f'<li>{e(m)}</li>' for m in i['mahalle'])}</ul>
  <p>{e(mahalle_cumle(i, None, 'hub'))}</p></section>
 {sss_html(sss, f"{i['ad']} gider açma: sık sorulanlar")}
 <section class="blok"><h2>Yakın ilçeler</h2><ul class="ag-liste">{komsu}</ul></section>
</div>
{cta(f"{i['ad']} için gider açma ustası mı lazım?", "7/24 arayabilir ya da WhatsApp'tan yazabilirsiniz.", None, i)}
""" + alt()

# ── hizmet sayfası ──────────────────────────────────────────────────────────
def hizmet_sayfasi(h):
    yol = hiz_yolu(h)
    sss = [(q.format(ad="Kocaeli", loc="'de"), c) for q, c in h["sss"]]
    kir_html, kir_ld = kirinti([("Anasayfa", ""), (h["ad"], None)])
    aciklama = f"{h['ad']}: {h['ozet']} Kocaeli'de 7 ilçede 7/24 hizmet. {S['tel_goster']}"
    ilce = "".join(f'<li><a href="{ic(ilce_yolu(i, h))}">{e(h["h1"].format(ad=i["ad"]))}</a></li>' for i in ILCE_SIRALI)
    diger = "".join(kart_hizmet(x) for x in D.HIZMETLER if x["slug"] != h["slug"])
    sema = [sema_hizmet(h["hub_h1"], h["ad"], None, yol), sema_sss(sss), kir_ld]
    return head(h["hub_title"], aciklama, yol, sema) + ust(h["slug"]) + hero(
        "Kocaeli · 7 ilçe · 7/24", e(h["hub_h1"]),
        h["ozet"] + " Kocaeli'de 7/24 hizmet veriyoruz; ekiplerimiz adrese ortalama 30 dakikada ulaşıyor.",
        gorsel(h["galeri"][0][0], h["galeri"][0][1], oncelik=True), kir_html, h) + f"""
<div class="kap">{guven()}</div>
<div class="kap govde">
 <section class="blok"><h2>Neler yapıyoruz?</h2>
  <div class="is-izgara">{''.join(f'<div class="is"><h3>{e(a)}</h3><p>{e(m)}</p></div>' for a, m in h['isler'])}</div></section>
 <section class="blok"><h2>Hangi durumlarda aramalısınız?</h2>
  <ul class="tik-liste">{''.join(f'<li>{svg("tik")}<span>{e(b)}</span></li>' for b in h['belirti'])}</ul></section>
 {galeri(h['galeri'], "Sahadan fotoğraflar")}
 <section class="blok kutu-vurgu"><h2>Usta gelene kadar ne yapabilirsiniz?</h2>
  <ol class="adim-liste">{''.join(f'<li>{e(o)}</li>' for o in h['oneri'])}</ol></section>
 <section class="blok"><h2>İlçeye göre {e(kucuk(h['kisa']))}</h2><ul class="ilce-izgara">{ilce}</ul></section>
 {sss_html(sss)}
 <section class="blok"><h2>Diğer hizmetlerimiz</h2><div class="hkart-izgara hkart-3">{diger}</div></section>
</div>
{cta(f"{h['ad']} için hemen ulaşın", "7/24 arayabilir ya da WhatsApp'tan yazabilirsiniz.", h)}
""" + alt()

# ── anasayfa ────────────────────────────────────────────────────────────────
ANA_SSS = [
 ("Hangi ilçelere hizmet veriyorsunuz?", "Kocaeli'de " + ve_liste([i["ad"] for i in D.ILCELER]) + " ilçelerine geliyoruz."),
 ("Gece ya da hafta sonu ulaşabilir miyim?", "Evet. 7 gün 24 saat hizmet veriyoruz; telefonla arayabilir ya da WhatsApp'tan yazabilirsiniz."),
 ("Usta ne kadar sürede gelir?", "Ekiplerimiz adrese ortalama 30 dakikada ulaşıyor. Trafik ve iş yoğunluğuna göre süre değişebilir; arama sırasında size tahmini süreyi söylüyoruz."),
 ("Gider açarken kırma yapılıyor mu?", "Hayır, tıkanıklığı gider ağzından makineyle açıyoruz. Gerektiğinde hattın içini kamerayla görüyoruz; kırma ancak boru kırılmış ya da çökmüşse gündeme gelir ve bunu önce görüntüyle size gösteriyoruz."),
 ("Fiyatı ne zaman öğrenirim?", "Fotoğraf ya da videoyla yaklaşık bilgi verebiliyoruz. Kesin fiyatı usta yerinde baktıktan sonra, işe başlamadan önce söylüyor."),
]

def anasayfa():
    kartlar = "".join(kart_hizmet(h) for h in D.HIZMETLER)
    ilceler = "".join(ilce_kart(i) for i in ILCE_SIRALI)
    sema = [{"@context": "https://schema.org", **isletme()}, sema_sss(ANA_SSS)]
    kam = HIZ["kamerali-goruntuleme"]
    saha = [("rogar-yikama", "Rögar borusuna basınçlı su püskürten yıkama başlığı"),
            ("kamerali-tikaniklik-goruntuleme", "Duş giderine sürülen makaralı kameranın ekran ünitesi"),
            ("kirmadan-tikaniklik-acma", "Yer giderinin kapağı açılarak kırmadan tıkanıklık açma"),
            ("kocaeli-tikali-gider-acma-servisi", "Gider açma ekipmanının taşındığı servis aracı")]
    return head("Kocaeli Tıkalı Gider Açma | Tuvalet, Rögar, Kameralı · 7/24",
                "Kocaeli'de tıkalı gider açma, tuvalet tıkanıklığı açma, rögar temizleme ve kameralı görüntüleme. "
                f"7/24 hizmet, ortalama 30 dakikada adreste, kırmadan. {S['tel_goster']}", "", sema) + ust() + f"""
<section class="hero hero-ana">
 <div class="hero-fon" data-paralaks>{gorsel('hero', '', oncelik=True, boy='100vw')}</div>
 {SAHNE}
 <div class="kap hero-ana-ic">
  <div class="hero-metin">
   <p class="ust-etiket"><span class="nokta"></span>Kocaeli · 7 ilçe · 7/24</p>
   <h1>Kocaeli Tıkalı Gider Açma <span class="vurgu">ortalama 30 dakikada</span> kapınızda</h1>
   <p class="hero-p">Lavabo, mutfak ve banyo gideri, tuvalet tıkanıklığı ve taşan rögar için 7 gün 24 saat ulaşabileceğiniz ekibiz. Tıkanıklığın yerini gerektiğinde kamerayla görüp kırmadan açıyoruz; fiyatı işe başlamadan söylüyoruz.</p>
   <div class="hero-dg">{tel_btn()}{wa_btn(wa_mesaj())}</div>
  </div>
  <a class="kam-panel" data-egim href="{ic(hiz_yolu(kam))}">
   <span class="kam-b">{svg('kamera')} Kamera ile gider tespiti</span>
   <span class="kam-p">Hattın içini kamerayla görüyor, tıkanıklığın yerini ve sebebini kırmadan buluyoruz.</span>
   <span class="kam-l"><span>{svg('tik')}Tıkanıklığın yeri ve sebebi</span><span>{svg('tik')}Kırmadan karar</span><span>{svg('tik')}Görüntüyü sizinle paylaşma</span></span>
   <em>Nasıl çalışır? {svg('ok')}</em>
  </a>
 </div>
</section>
<div class="kap">{guven()}</div>
<div class="kap govde">
 <section class="blok"><p class="bolum-ust">Hizmetlerimiz</p><h2>Gider açma hizmetleri</h2>
  <p class="blok-giris">Her hizmetin ilçenize özel sayfasında, o bölgedeki binalarda en sık karşılaştığımız durumları da anlattık.</p>
  <div class="hkart-izgara">{kartlar}</div></section>
 <section class="blok" id="bolgeler"><p class="bolum-ust">Hizmet bölgeleri</p><h2>Hizmet verdiğimiz ilçeler</h2>
  <p class="blok-giris">İlçenizi seçin; o ilçedeki dört hizmetin sayfasına oradan ulaşabilirsiniz. Merkezimiz Başiskele'de.</p>
  <div class="ikart-izgara">{ilceler}</div></section>
 <section class="blok"><p class="bolum-ust">Süreç</p><h2>Nasıl çalışıyoruz?</h2>
  <div class="surec-kap"><div class="boru" aria-hidden="true"><span class="boru-su"></span></div>
  <ol class="surec">
   <li><b>Arayın ya da yazın</b><span>Sorunu anlatın; mümkünse WhatsApp'tan fotoğraf ya da kısa video gönderin.</span></li>
   <li><b>Ekip yola çıksın</b><span>Adresinize en yakın ekibi yönlendiriyoruz; ortalama 30 dakikada adresteyiz.</span></li>
   <li><b>Yerinde tespit ve fiyat</b><span>Usta tıkanıklığın yerini gerekirse kamerayla görüyor, fiyatı işe başlamadan söylüyor.</span></li>
   <li><b>Kırmadan açma ve kontrol</b><span>Gideri makineyle açıyor, akışı birlikte test ediyor, ortamı temiz bırakıyoruz.</span></li>
  </ol></div></section>
 {galeri(saha, "Sahadan fotoğraflar")}
 {sss_html(ANA_SSS)}
</div>
{cta("Gideriniz mi tıkandı?", "7/24 arayabilir ya da WhatsApp'tan yazabilirsiniz. Ortalama 30 dakikada adresinizdeyiz.")}
""" + alt()

# ── diğer sayfalar ──────────────────────────────────────────────────────────
def basit(baslik, aciklama, yol, h1, govde, aktif="", robots="index,follow"):
    kir_html, kir_ld = kirinti([("Anasayfa", ""), (h1, None)])
    return head(baslik, aciklama, yol, [kir_ld], robots) + ust(aktif) + f"""
<section class="hero hero-dar"><div class="kap"><div class="hero-metin">{kir_html}<h1>{e(h1)}</h1></div></div></section>
<div class="kap govde">{govde}</div>
""" + alt()

def bolgeler():
    satir = []
    for i in ILCE_SIRALI:
        l = "".join(f'<li><a href="{ic(ilce_yolu(i, h))}">{e(h["h1"].format(ad=i["ad"]))}</a></li>' for h in D.HIZMETLER)
        satir.append(f'<section class="bolge"><h2><a href="{ic(ilce_yolu(i))}">{e(i["ad"])} gider açma</a></h2><ul>{l}</ul></section>')
    govde = (f'<p class="blok-giris">Kocaeli\'de {len(D.ILCELER)} ilçeye 7/24 servis veriyoruz. Merkezimiz Başiskele\'de; '
             f'ekiplerimiz adrese ortalama 30 dakikada ulaşıyor.</p><div class="bolge-izgara">{"".join(satir)}</div>')
    return basit("Hizmet Bölgeleri | Kocaeli Tıkalı Gider Açma · 7 İlçe",
                 "Kocaeli Tıkalı Gider Açma'nın hizmet verdiği ilçeler: İzmit, Başiskele, Gölcük, Derince, Körfez, Kartepe, Karamürsel.",
                 "hizmet-bolgeleri/", "Hizmet Bölgeleri", govde, "bolge")

def iletisim():
    govde = f"""<section class="blok iletisim">
 <div class="ilt-kart">{svg('tel')}<div><h2>Telefon</h2><p><a href="tel:{S['tel_link']}">{S['tel_goster']}</a></p></div></div>
 <div class="ilt-kart">{svg('wa')}<div><h2>WhatsApp</h2><p>Fotoğraf ya da video göndererek sorunu anlatabilirsiniz.</p>{wa_btn(wa_mesaj())}</div></div>
 <div class="ilt-kart">{svg('konum')}<div><h2>Adres</h2><p>{e(S['adres'])}</p><p><a href="{S['harita']}" target="_blank" rel="noopener">Haritada aç</a></p></div></div>
 <div class="ilt-kart">{svg('saat')}<div><h2>Çalışma saatleri</h2><p>7 gün 24 saat</p><p><a href="{ic('hizmet-bolgeleri/')}">Hizmet bölgeleri</a></p></div></div>
</section>"""
    return basit(f"İletişim | Kocaeli Tıkalı Gider Açma · {S['tel_goster']}",
                 f"Kocaeli Tıkalı Gider Açma iletişim: {S['tel_goster']}, WhatsApp, 7/24. Adres: {S['adres']}.",
                 "iletisim/", "İletişim", govde, "iletisim")

def gizlilik():
    p = lambda *x: "".join(f"<p>{e(t)}</p>" for t in x)
    olcum = ("Reklamlarımızın sonuç verip vermediğini ölçmek için Google Ads dönüşüm etiketi kullanılır. Bu etiket, siteye hangi reklamdan "
             "geldiğinizi ve arama ya da WhatsApp düğmesine tıklayıp tıklamadığınızı Google'a bildirir. Tarayıcı ayarlarınızdan çerezleri "
             "silebilir ya da engelleyebilirsiniz.") if D.ADS["etiket"] else \
            "Bu sitede analitik ya da reklam ölçüm çerezi kullanılmaz."
    govde = f"""<section class="blok metin">
<h2>Kişisel veriler</h2>{p("Bu site üzerinden form doldurulmaz ve kişisel veri toplanmaz. Bizi telefonla aradığınızda ya da WhatsApp'tan yazdığınızda paylaştığınız ad, telefon numarası ve adres bilgisi yalnızca talep ettiğiniz hizmeti vermek amacıyla kullanılır ve üçüncü kişilerle paylaşılmaz.")}
<h2>Çerezler ve ölçüm</h2>{p(olcum)}
<h2>Haklarınız</h2>{p("6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamındaki haklarınızla ilgili talepleriniz için " + S["tel_goster"] + " numarasından ya da " + S["adres"] + " adresinden bize ulaşabilirsiniz.")}
</section>"""
    return basit("Gizlilik Politikası | Kocaeli Tıkalı Gider Açma", "Kocaeli Tıkalı Gider Açma gizlilik politikası ve çerez bilgilendirmesi.",
                 "gizlilik-politikasi/", "Gizlilik Politikası", govde)

def hata404():
    govde = ('<section class="blok"><p>Aradığınız sayfa bulunamadı. <a href="/">Anasayfaya</a> ya da '
             '<a href="/hizmet-bolgeleri/">hizmet bölgelerine</a> göz atabilirsiniz.</p></section>')
    return basit("Sayfa bulunamadı | Kocaeli Tıkalı Gider Açma", "Aradığınız sayfa bulunamadı.", "404.html",
                 "Sayfa bulunamadı", govde, robots="noindex,follow")

# ── yazma ───────────────────────────────────────────────────────────────────
def yaz(yol, icerik):
    hedef = os.path.join(KOK, yol, "index.html") if yol.endswith("/") or yol == "" else os.path.join(KOK, yol)
    os.makedirs(os.path.dirname(hedef), exist_ok=True)
    with open(hedef, "w", encoding="utf-8") as f: f.write(icerik)

def sayfa(yol, uretici, *arg):
    global ONEK
    ONEK = "../" * yol.count("/")
    yaz(yol, uretici(*arg))
    return yol

def temizle():
    """Önceki üretimden kalan sayfa klasörlerini sil (yalnızca index.html içerenler)."""
    for ad in os.listdir(KOK):
        tam = os.path.join(KOK, ad)
        if os.path.isdir(tam) and ad not in {"assets", "images", "_src", ".git"} and os.path.isfile(os.path.join(tam, "index.html")):
            shutil.rmtree(tam)

def main():
    global ONEK
    temizle()
    yollar = [sayfa("", anasayfa)]
    for h in D.HIZMETLER: yollar.append(sayfa(hiz_yolu(h), hizmet_sayfasi, h))
    for i in D.ILCELER:
        yollar.append(sayfa(ilce_yolu(i), ilce_sayfasi, i))
        for h in D.HIZMETLER: yollar.append(sayfa(ilce_yolu(i, h), ilce_hizmet_sayfasi, i, h))
    yollar += [sayfa("hizmet-bolgeleri/", bolgeler), sayfa("iletisim/", iletisim), sayfa("gizlilik-politikasi/", gizlilik)]
    ONEK = "/"
    yaz("404.html", hata404())
    sm = "".join(f"<url><loc>{ALAN}/{y}</loc></url>" for y in yollar if y != "gizlilik-politikasi/")
    yaz("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    yaz("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {ALAN}/sitemap.xml\n")
    yaz("CNAME", S["cname"] + "\n")
    print(f"{len(yollar)} sayfa üretildi")

if __name__ == "__main__":
    main()
