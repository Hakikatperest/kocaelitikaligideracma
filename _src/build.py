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
import os, re, json, hashlib, html, shutil, datetime
from urllib.parse import quote
from PIL import Image
import data as D
import icerik as IC

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = D.SITE
ALAN = S["alan"]
ILCE = {i["slug"]: i for i in D.ILCELER}
HIZ = {h["slug"]: h for h in D.HIZMETLER}
ONEK = ""   # sayfa derinliğine göre göreli yol öneki
HERO_KOYU = S.get("hero_tema", "koyu") == "koyu"
HK = "koyu" if HERO_KOYU else "hero-acik"   # hero tema sınıfı
BUGUN = datetime.date.today().isoformat()

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
 "kapat": '<path d="M19 6.4 17.6 5 12 10.6 6.4 5 5 6.4 10.6 12 5 17.6 6.4 19 12 13.4 17.6 19 19 17.6 13.4 12z"/>',
 "uyari": '<path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/>',
 "anahtar": '<path d="M22.7 19 13.6 9.9c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/>',
 "evye": '<path d="M2 11h20v1.5A6.5 6.5 0 0 1 15.5 19h-7A6.5 6.5 0 0 1 2 12.5V11zm9-8h5a2 2 0 0 1 2 2v2h-2V5h-5v5h-2V5a2 2 0 0 1 2-2z"/>',
 "dus": '<path d="M5 3h7a7 7 0 0 1 7 7v1H4V9a3 3 0 0 0-1.5-2.6L3.5 4.7A5 5 0 0 1 6 9V5H5V3zm2 10h2v2H7v-2zm4 0h2v2h-2v-2zm4 0h2v2h-2v-2zM7 17h2v2H7v-2zm4 0h2v2h-2v-2zm4 0h2v2h-2v-2zm-4 4h2v1h-2z"/>',
 "bilgi": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/>',
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
    avif = ", ".join(x.replace(".webp ", ".avif ") for x in parca)
    return (f'<picture><source type="image/avif" srcset="{avif}" sizes="{boy}">'
            f'<img class="{sinif}" src="{ic(f"images/{taban}-{genler[-1]}.webp")}" srcset="{", ".join(parca)}" '
            f'sizes="{boy}" width="{olcu[0]}" height="{olcu[1]}" alt="{e(alt)}" {yukle}></picture>')

def galeri(oge, baslik):
    return (f'<section class="blok"><h2>{e(baslik)}</h2><div class="galeri">' +
            "".join(f'<figure>{gorsel(t, a, boy="(min-width:980px) 280px, 50vw")}<figcaption>{e(a)}</figcaption></figure>'
                    for t, a in oge) + '</div></section>')

# ── düğmeler ────────────────────────────────────────────────────────────────
def tel_btn(metin=None, sinif="dg dg-ara", ust="7/24 Hemen Ara"):
    """metin yoksa iki satır: küçük üst etiket + büyük numara (hero ve CTA). metin verilirse tek satır (footer)."""
    yazi = (f'<span class="dg-yazi"><small>{e(ust)}</small><b>{S["tel_goster"]}</b></span>' if metin is None
            else f'<span class="dg-yazi"><b>{e(metin)}</b></span>')
    return (f'<a class="{sinif}" href="tel:{S["tel_link"]}" aria-label="Telefonla ara: {S["tel_goster"]}">'
            f'<span class="dg-ik">{svg("tel")}</span>{yazi}</a>')

def wa_btn(mesaj, metin=None, sinif="dg dg-wa", ust="WhatsApp'tan"):
    yazi = (f'<span class="dg-yazi"><small>{e(ust)}</small><b>Hemen Yazın</b></span>' if metin is None
            else f'<span class="dg-yazi"><b>{e(metin)}</b></span>')
    return (f'<a class="{sinif}" href="https://wa.me/{S["wa"]}?text={quote(mesaj)}" target="_blank" '
            f'rel="noopener" aria-label="WhatsApp ile yazın"><span class="dg-ik">{svg("wa")}</span>{yazi}</a>')

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
<meta name="theme-color" content="{"#060B14" if HERO_KOYU else "#FFFFFF"}">
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
    return f"""<header class="ust{" koyu" if HERO_KOYU else ""}">
 <div class="kap ust-ic">
  {logo()}
  <nav class="menu" id="menu" aria-label="Ana menü">
   <div class="menu-grup"><span class="menu-baslik">Hizmetler</span><div class="menu-alt">{hiz}</div></div>
   <div class="menu-grup"><span class="menu-baslik">İlçeler</span><div class="menu-alt">{ilc}</div></div>
   <a href="{ic('rehber/')}"{' class="aktif"' if aktif=='rehber' else ''}>Rehber</a>
   <a href="{ic('hizmet-bolgeleri/')}"{' class="aktif"' if aktif=='bolge' else ''}>Hizmet Bölgeleri</a>
   <a href="{ic('hakkimizda/')}"{' class="aktif"' if aktif=='hakkimizda' else ''}>Hakkımızda</a>
   <a href="{ic('iletisim/')}"{' class="aktif"' if aktif=='iletisim' else ''}>İletişim</a>
  </nav>
  <div class="ust-sag">
   <a class="ust-tel" href="tel:{S['tel_link']}">{svg('saat')}<span><small class="durum"><span class="canli"></span>Şu an açığız · 7/24</small><b>{S['tel_goster']}</b></span></a>
   <button class="menu-ac" type="button" aria-controls="menu" aria-expanded="false" aria-label="Menüyü aç">{svg('menu', 'ik ik-ac')}{svg('kapat', 'ik ik-kapat')}</button>
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
    reh = "".join(f'<li><a href="{ic(r["slug"] + "/")}">{e(r["h1"].split("?")[0])}?</a></li>' for r in IC.REHBER)
    return f"""</main>
<footer class="alt koyu">
 <div class="kap alt-izgara">
  <div class="alt-marka">
   {logo()}
   <p>Yılların tecrübesiyle İzmit, Başiskele, Gölcük, Derince, Körfez, Kartepe ve Karamürsel'de tıkalı gider açma, tuvalet tıkanıklığı açma, rögar temizleme ve kameralı gider görüntüleme. Kırmadan çalışıyor, ödemeyi iş bitince alıyoruz. 7 gün 24 saat.</p>
   <p class="alt-sat">{svg('tel')}<a href="tel:{S['tel_link']}">{S['tel_goster']}</a></p>
   <p class="alt-sat">{svg('wa')}<a href="https://wa.me/{S['wa']}?text={quote(wa_mesaj())}" target="_blank" rel="noopener">WhatsApp'tan yazın</a></p>
   <p class="alt-sat">{svg('konum')}<a href="{S['harita']}" target="_blank" rel="noopener">{e(S['adres'])}</a></p>
   <p class="alt-sat">{svg('saat')}<span>7 gün 24 saat</span></p>
  </div>
  <div><h2 class="alt-b">Hizmetler</h2><ul class="alt-liste">{hiz}</ul>
   <h2 class="alt-b alt-b2">Rehber</h2><ul class="alt-liste">{reh}<li><a href="{ic('hakkimizda/')}">Hakkımızda</a></li></ul></div>
  <div><h2 class="alt-b">İlçeler</h2><ul class="alt-liste">{ilc}<li><a href="{ic('hizmet-bolgeleri/')}">Tüm hizmet bölgeleri</a></li></ul></div>
 </div>
 <div class="kap alt-son">
  <p>© 2026 {e(S['marka'])} · <a href="{ic('gizlilik-politikasi/')}">Gizlilik Politikası</a> · <a href="{ic('iletisim/')}">İletişim</a></p>
 </div>
 {w4_imza()}
</footer>
<div class="hizli" id="dock" aria-label="Hızlı iletişim">
 <a class="hz hz-ara" href="tel:{S['tel_link']}" aria-label="Hemen ara: {S['tel_goster']}"><span class="hz-isik"></span><span class="hz-ik">{svg('tel')}</span><span class="hz-yazi"><small><span class="canli"></span>7/24 açık</small><b>Hemen Ara</b></span></a>
 <a class="hz hz-wa" href="https://wa.me/{S['wa']}?text={quote(wa_mesaj())}" target="_blank" rel="noopener" aria-label="WhatsApp'tan yazın"><span class="hz-ik">{svg('wa')}</span><span class="hz-yazi"><b>WhatsApp'tan Yaz</b></span></a>
</div>
<script src="{ic(surum('assets/js/app.js'))}" defer></script>
</body>
</html>
"""

# ── şema ────────────────────────────────────────────────────────────────────
def isletme():
    return {"@type": "Plumber", "@id": ALAN + "/#isletme", "name": S["marka"], "url": ALAN + "/",
            "telephone": S["tel_link"], "image": ALAN + "/images/og-kocaeli-tikali-gider-acma.jpg",
            "logo": ALAN + "/images/favicon-512.png", "description": IC.TANITIM + " " + IC.ODEME,
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
           ("lira", "Ödeme iş bitince", "Sorun giderilmeden ücret almıyoruz; fiyatı işe başlamadan söylüyoruz.")]
    return '<ul class="guven">' + "".join(
        f'<li><span class="guven-ik">{svg(i)}</span><div><b>{e(b)}</b><span>{e(m)}</span></div></li>' for i, b, m in oge) + "</ul>"

def sss_html(sorular, baslik="Sık Sorulan Sorular"):
    oge = "".join(f'<details class="sss-oge"><summary>{e(s)}</summary><p>{e(c)}</p></details>' for s, c in sorular)
    return f'<section class="blok" id="sss"><h2>{e(baslik)}</h2><div class="sss">{oge}</div></section>'

SORUNLAR = [("tikali-gider-acma", "Tıkalı gider (lavabo, mutfak, banyo)"), ("tuvalet-tikanikligi-acma", "Tuvalet tıkanıklığı"),
            ("rogar-temizleme", "Rögar taşıyor / rögar temizliği"), ("kamerali-goruntuleme", "Kameralı görüntüleme"), ("diger", "Diğer")]

def teklif_formu(h=None, i=None):
    ilce = "".join(f'<option{" selected" if i and x["slug"] == i["slug"] else ""}>{e(x["ad"])}</option>' for x in ILCE_SIRALI)
    sorun = "".join(f'<option{" selected" if h and k == h["slug"] else ""}>{e(a)}</option>' for k, a in SORUNLAR)
    return f"""<form class="teklif" action="https://wa.me/{S['wa']}" method="get" target="_blank" data-teklif>
  <p class="teklif-b">{svg('wa')} Hızlı fiyat bilgisi al</p>
  <p class="teklif-k">Seçimlerinizi yapın; bilgiler WhatsApp mesajı olarak hazırlansın, siz gönderin. Sitede hiçbir bilgi saklanmaz.</p>
  <div class="teklif-iki">
   <label>İlçe<select name="ilce"><option value="">Seçin</option>{ilce}</select></label>
   <label class="teklif-genis">Sorun<select name="sorun">{sorun}</select></label>
  </div>
  <label>Mahalle ve kısa not<textarea name="text" rows="3" placeholder="Örnek: Yeniköy Mah., 3. kat, mutfak evyesi doluyor"></textarea></label>
  <button class="dg dg-wa" type="submit"><span class="dg-ik">{svg('wa')}</span><span class="dg-yazi"><small>Bilgileriniz hazır</small><b>WhatsApp'ta gönder</b></span></button>
 </form>"""

def cta(baslik, metin, h=None, i=None):
    return f"""<section class="cta koyu" id="teklif"><div class="kap cta-ic">
 <div class="cta-sol">
  <p class="durum-rozet"><span class="canli"></span>Şu an hizmet veriyoruz · <span class="durum-saat">7/24</span></p>
  <h2>{e(baslik)}</h2><p>{e(metin)}</p>
  <a class="cta-tel" href="tel:{S['tel_link']}"><span class="cta-tel-ik">{svg('tel')}</span><span><small>7/24 arayın</small><b>{S['tel_goster']}</b></span></a>
  <ul class="cta-liste"><li>{svg('tik')}Ortalama 30 dakikada adreste</li><li>{svg('tik')}Fiyat işe başlamadan söylenir</li><li>{svg('tik')}Kırmadan, gerekirse kameralı</li></ul>
 </div>
 {teklif_formu(h, i)}
</div></section>"""

# ── anasayfa ve hizmet sayfası bölümleri
SORUN_KART = [("klozet", "Tuvalet tıkandı", "Su yükseliyor, sifon çekince gitmiyor", "tuvalet-tikanikligi-acma"),
              ("evye", "Mutfak evyesi doluyor", "Yağ birikimi, bulaşık makinesi suyu geri geliyor", "tikali-gider-acma"),
              ("damla", "Lavabo yavaş akıyor", "Saç, sabun ve diş macunu birikimi", "tikali-gider-acma"),
              ("dus", "Duş gideri tıkalı", "Duş teknesinde ya da küvette su birikiyor", "tikali-gider-acma"),
              ("rogar", "Rögar taşıyor", "Bahçe ya da bina rögarı doldu, koku var", "rogar-temizleme"),
              ("kamera", "Sürekli tekrar ediyor", "Açtırdınız ama kısa sürede yine tıkandı", "kamerali-goruntuleme")]

def sorun_secici():
    k = "".join(f'<a class="skart" data-egim href="{ic(hiz_yolu(HIZ[h]))}"><span class="skart-ik">{svg(ik)}</span>'
                f'<b>{e(b)}</b><span>{e(m)}</span>{svg("ok", "ik skart-ok")}</a>' for ik, b, m, h in SORUN_KART)
    return f"""<section class="blok"><p class="bolum-ust">Hızlı yönlendirme</p><h2>Sorununuz hangisi?</h2>
  <p class="blok-giris">Yaşadığınız duruma en yakın olanı seçin; o işi nasıl yaptığımızı anlattığımız sayfaya gidin.</p>
  <div class="skart-izgara">{k}</div></section>"""

def kamera_demo():
    kam = HIZ["kamerali-goruntuleme"]
    return f"""<section class="blok kamera-blok koyu"><div class="kamera-izgara">
 <div class="kamera-metin"><p class="bolum-ust">Kameralı görüntüleme</p>
  <h2>Tıkanıklığı tahmin etmiyoruz, görüyoruz</h2>
  <p>Makaralı kamerayı gider ağzından hattın içine sürüyoruz. Ekranda tıkanıklığın kaç metre ileride olduğunu, sebebinin yağ mı, kök mü, düşen bir cisim mi olduğunu ve borunun sağlam olup olmadığını birlikte görüyoruz.</p>
  <ul class="tik-liste tik-tek"><li>{svg('tik')}<span>Kırma kararı görüntüye bakılarak verilir; çoğu tıkanıklık kırmadan açılır.</span></li>
   <li>{svg('tik')}<span>Açtıktan sonra hattı yeniden görüntüleyip temizliği doğruluyoruz.</span></li>
   <li>{svg('tik')}<span>İsterseniz görüntüyü telefonunuza gönderiyoruz.</span></li></ul>
  <p><a class="metin-bag" href="{ic(hiz_yolu(kam))}">Kameralı görüntüleme hizmeti {svg('ok')}</a></p>
 </div>
 <div class="kam-demo" aria-hidden="true">
  <div class="kam-ekran">
   <div class="tunel"><span></span><span></span><span></span><span></span><span></span><span></span></div>
   <div class="tikac"></div><div class="nisan"></div>
   <div class="kam-hud"><span class="rec">KAYIT</span><span>Mesafe <b class="m-sayac">0,0</b> m</span></div>
   <div class="tespit">{svg('uyari')} Tıkanıklık tespit edildi</div>
  </div>
  <div class="kam-boru"><div class="kam-ic"><div class="kam-kablo"></div><div class="kam-bas"><span class="kam-isik"></span></div><div class="kam-tikac"></div></div></div>
  <p class="kam-not">Temsilî animasyon</p>
 </div>
</div></section>"""

HARITA_BOLGE = {  # şematik — ölçekli DEĞİL. (path, etiket x, y)
 "korfez":     ("M20 62 L232 50 L250 188 L40 212 Z", 135, 128),
 "derince":    ("M232 50 L402 40 L412 178 L250 188 Z", 325, 112),
 "izmit":      ("M402 40 L602 52 L622 198 L578 214 L412 178 Z", 508, 118),
 "kartepe":    ("M602 52 L780 84 L768 330 L646 302 L622 198 Z", 700, 190),
 "basiskele":  ("M432 252 L578 224 L622 206 L646 302 L602 392 L452 382 Z", 540, 312),
 "golcuk":     ("M252 258 L432 252 L452 382 L272 392 Z", 356, 322),
 "karamursel": ("M30 252 L252 258 L272 392 L42 382 Z", 150, 322),
}
def kocaeli_harita():
    g = []
    for i in D.ILCELER:
        d, x, y = HARITA_BOLGE[i["slug"]]
        merkez = i["slug"] == "basiskele"
        g.append(f'<a href="{ic(ilce_yolu(i))}" class="hb" data-ilce="{i["slug"]}" aria-label="{e(i["ad"])} gider açma">'
                 f'<path class="hb-alan" d="{d}"/><circle class="hb-nabiz{" hb-merkez" if merkez else ""}" cx="{x}" cy="{y-22}" r="7"/>'
                 f'<circle class="hb-pin" cx="{x}" cy="{y-22}" r="5"/>'
                 f'<text x="{x}" y="{y+4}" class="hb-ad">{e(i["ad"])}</text>'
                 + (f'<text x="{x}" y="{y+22}" class="hb-alt">Merkezimiz</text>' if merkez else "") + '</a>')
    return f"""<div class="harita-kap koyu"><svg class="kharita" viewBox="0 0 800 420" role="img" aria-label="Hizmet verdiğimiz Kocaeli ilçeleri, şematik harita">
  <defs><linearGradient id="su" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B3A66"/><stop offset="1" stop-color="#1679B8"/></linearGradient></defs>
  <path class="korfez-su" d="M0 214 L250 190 L412 180 L578 216 L622 204 L600 222 L578 226 L432 252 L252 258 L0 252 Z" fill="url(#su)"/>
  <path class="dalga" d="M30 236 C120 226 200 238 300 228 S480 222 560 222"/>
  <text x="300" y="246" class="korfez-ad">İzmit Körfezi</text>
  {''.join(g)}
 </svg><p class="harita-not">Şematik gösterimdir, ölçekli değildir. İlçeye tıklayın.</p></div>"""

def uzmanlik():
    neden = [("Yağ", "Mutfak yağı sıcakken akar, borunun soğuk bölümünde donup çepere yapışır; zamanla boru çapını daraltır."),
             ("Saç ve sabun", "Banyo ve duş giderinde saç, sabun kalıntısıyla birleşip keçeleşir ve süzgecin altındaki dirseği kapatır."),
             ("Islak mendil ve ped", "Tuvalet kâğıdı gibi suda dağılmaz; dirseklerde ve kolonun döndüğü noktada toplanıp tıkaç oluşturur."),
             ("Kireç ve tortu", "Eski borularda iç yüzey pürüzlenir; tutunan kireç ve tortu diğer birikintiler için zemin hazırlar."),
             ("Ağaç kökü", "Bahçe hattında ek yerlerinden içeri giren kökler boru içinde ağ gibi büyür, rögarı sürekli doldurur."),
             ("Eğim ve hat yapısı", "Eğimi yetersiz ya da çok dirsekli hatlarda su yavaş akar; taşıdığı tortu yolda kalır.")]
    kimya = [("Kalıcı çözüm değil", "Yüzeydeki saç ve sabunu kısmen eritir ama çepere yapışmış yağı, kireci ya da sıkışmış bir cismi sökmez; tıkanıklık kısa sürede geri gelir."),
             ("Boru ve contaya zarar verebilir", "Güçlü asit ve bazlar eski metal borularda ve plastik bağlantılarda aşınmaya yol açabilir."),
             ("Karıştırmak tehlikeli", "Tuz ruhu ile çamaşır suyu ya da farklı açıcılar karışınca zehirli gaz çıkabilir; kapalı banyoda bu ciddi bir risktir."),
             ("Ustanın işini zorlaştırır", "Giderde bekleyen kimyasal, makineyle açarken geri sıçrayabilir. Kimyasal kullandıysanız ustaya mutlaka söyleyin.")]
    return f"""<section class="blok"><p class="bolum-ust">Bilmekte fayda var</p><h2>Gider neden tıkanır?</h2>
  <div class="is-izgara is-3">{''.join(f'<div class="is"><h3>{e(a)}</h3><p>{e(m)}</p></div>' for a, m in neden)}</div></section>
 <section class="blok kutu-uyari"><h2>{svg('uyari')} Kimyasal gider açıcıyı neden önermiyoruz?</h2>
  <div class="is-izgara">{''.join(f'<div class="is is-sade"><h3>{e(a)}</h3><p>{e(m)}</p></div>' for a, m in kimya)}</div></section>"""

def fiyat_faktor(baslik="Gider açma fiyatları ne kadar?"):
    f = [("konum", "Tıkanıklığın yeri", "Lavabo sifonundaki tıkanıklık ile bina kolonu ya da bahçe hattındaki tıkanıklık aynı iş değildir."),
         ("bilgi", "Tıkanıklığın sebebi", "Saç ve sabun birikintisi kısa sürede açılırken yağ, kireç ya da kök daha fazla işlem ister."),
         ("anahtar", "Erişim", "Temizleme kapağının olup olmaması, klozetin sökülmesi gerekip gerekmediği, rögarın derinliği."),
         ("kamera", "Kamera ve ek işlem", "Tekrarlayan tıkanıklıkta kameralı görüntüleme ya da basınçlı suyla yıkama gerekebilir.")]
    return f"""<section class="blok fiyat-blok"><p class="bolum-ust">Şeffaf fiyat</p><h2>{e(baslik)}</h2>
  <p class="blok-giris">Her tıkanıklık farklı olduğu için telefonda kesin fiyat vermiyoruz; fotoğraf ya da videoyla yaklaşık bilgi verebiliyoruz. Kesin fiyatı usta yerinde gördükten sonra, <b>işe başlamadan</b> söylüyor; onayınız olmadan işe başlamıyoruz. Sorun tamamen giderilmeden ücret talep etmiyor, ödemeyi iş bitince alıyoruz.</p>
  <div class="fiyat-izgara">{''.join(f'<div class="fkart"><span class="guven-ik">{svg(ik)}</span><h3>{e(a)}</h3><p>{e(m)}</p></div>' for ik, a, m in f)}</div>
  <p><a class="dg dg-hayalet" href="#teklif"><span class="dg-ik">{svg('wa')}</span><span class="dg-yazi"><b>Fotoğraf gönderip yaklaşık fiyat öğrenin</b></span></a></p></section>"""

def konum_blok():
    q = quote("Kılıçarslan Mah. Hürriyet Cad. No:1 Başiskele Kocaeli")
    return f"""<section class="blok konum-blok"><div class="konum-izgara">
 <div><p class="bolum-ust">Konum</p><h2>Merkezimiz Başiskele'de</h2>
  <p class="alt-sat">{svg('konum')}<span>{e(S['adres'])}</span></p>
  <p class="alt-sat">{svg('saat')}<span>7 gün 24 saat · <span class="durum-rozet durum-ic"><span class="canli"></span>şu an açık</span></span></p>
  <p class="alt-sat">{svg('tel')}<a href="tel:{S['tel_link']}">{S['tel_goster']}</a></p>
  <p>Ekiplerimiz Başiskele'den İzmit, Gölcük, Derince, Körfez, Kartepe ve Karamürsel'e ortalama 30 dakikada ulaşıyor.</p>
  <p><a class="metin-bag" href="{S['harita']}" target="_blank" rel="noopener">Google Haritalar'da yol tarifi al {svg('ok')}</a></p></div>
 <div class="harita-cerceve" data-harita="https://maps.google.com/maps?q={q}&amp;z=15&amp;output=embed">
  <button type="button" class="harita-ac">{svg('konum')}<span>Haritayı göster</span><small>Tıklayınca Google Haritalar yüklenir</small></button>
 </div>
</div></section>"""

def yorumlar():
    """⛔ Yalnız GERÇEK yorum (data.YORUMLAR). Boşken bölüm basılmaz; aggregateRating şeması KONMAZ."""
    if not D.YORUMLAR: return ""
    k = "".join(f'<figure class="ykart"><div class="yildiz" aria-label="{p} yıldız">{"★" * p}{"☆" * (5 - p)}</div>'
                f'<blockquote>{e(m)}</blockquote><figcaption><b>{e(ad)}</b> · {e(ilce)}<small>{e(kaynak)}</small></figcaption></figure>'
                for ad, ilce, p, m, kaynak in D.YORUMLAR)
    return f'<section class="blok"><p class="bolum-ust">Müşteri yorumları</p><h2>Müşterilerimiz ne diyor?</h2><div class="ykart-izgara">{k}</div></section>'


SAHNE = ('<div class="sahne" aria-hidden="true"><div class="zemin-izgara"></div>'
         '<canvas class="kabarcik"></canvas><span class="isik isik-1"></span><span class="isik isik-2"></span></div>')

def hero(etiket, h1, p, gorsel_html, kir="", h=None, i=None, sinif="hero-ic"):
    return f"""<section class="hero {HK} {sinif}">{SAHNE}<div class="kap hero-izgara">
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
            f'<h3 class="hkart-b">{e(ad)}</h3><span>{e(h["ozet"])}</span><em>Ayrıntılar {svg("ok")}</em></span></a>')

def ilce_kart(i):
    return (f'<a class="ikart" data-egim data-ilce="{i["slug"]}" href="{ic(ilce_yolu(i))}">{svg("konum")}<b>{e(i["ad"])}</b>'
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

# ── SEO makale mimarisi (2026-10-05) ───────────────────────────────────────
# Kullanıcı: "her iç sayfa ve anasayfa kendi konusu üzerine SEO açısından güçlü H1/H2/H3 başlıklardan oluşsun,
# benim dilimle makaleler, örümcek ağı gibi birbirine bağlı". Örnek H2'ler (Gölcük): "…servisine nasıl ulaşırsınız?",
# "…belediye gider açma hizmeti veriyor mu?", "Gider açma fiyatları ne kadar?", "… 7/24 Tıkanıklık Açma Servisi",
# "…'e en yakın tıkanıklık açma servisi". Makaleler _src/icerik.py'de.
# ⛔ Buton tekrarı yok: gövdede tel/WhatsApp DÜZ BAĞLANTI (hero + #teklif + mobil yüzen butonlar yeterli).

def bagla(metin, i=None):
    """Metni kaçışlar, [[yol|yazı]] işaretlerini site içi bağlantıya çevirir."""
    def r(m):
        yol, yazi = m.group(1), m.group(2)
        if yol.startswith("hizmet:"):
            h = HIZ[yol[7:]]; hedef = ilce_yolu(i, h) if i else hiz_yolu(h)
        elif yol.startswith("ilce:"):
            hedef = ilce_yolu(ILCE[yol[5:]])
        else:
            hedef = yol
        return f'<a href="{ic(hedef)}">{yazi}</a>'
    return re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r, e(metin))

def P(metin, i=None): return f"<p>{bagla(metin, i)}</p>"
def ipucu(etiket, metin, i=None, sinif="ipucu"):
    return f'<p class="{sinif}"><b>{e(etiket)}</b> {bagla(metin, i)}</p>'
def tel_a(): return f'<a href="tel:{S["tel_link"]}">{S["tel_goster"]}</a>'
def wa_a(mesaj, yazi="WhatsApp'tan yazabilirsiniz"):
    return f'<a href="https://wa.me/{S["wa"]}?text={quote(mesaj)}" target="_blank" rel="noopener">{e(yazi)}</a>'

def h3_izgara(oge, sinif="is-izgara"):
    return f'<div class="{sinif}">' + "".join(f'<div class="is"><h3>{e(a)}</h3><p>{e(m)}</p></div>' for a, m in oge) + "</div>"

def sorumluluk_tablo():
    satir = [("Evinizdeki lavabo, mutfak, duş ve tuvalet gideri", "Mülk sahibi", "Özel servis (biz)"),
             ("Bina kolonu, bahçe rögarı, parsel bacasına kadar olan hat", "Mülk sahibi / bina yönetimi", "Özel servis (biz)"),
             ("Sokaktaki ana kanalizasyon hattı ve sokak rögarı", "İSU", "ALO 185 (7/24)")]
    return ('<div class="tablo-kap"><table class="tablo"><thead><tr><th>Tıkanıklığın yeri</th><th>Kimin sorumluluğunda?</th>'
            '<th>Kimi aramalısınız?</th></tr></thead><tbody>' +
            "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in satir) + "</tbody></table></div>")

def servis_no(baslik="7/24 acil servis numarası"):
    return (f'<a class="servis-no" href="tel:{S["tel_link"]}"><span class="servis-no-ik">{svg("tel")}</span>'
            f'<span><small>{e(baslik)}</small><b>{S["tel_goster"]}</b><em>Gece, hafta sonu ve bayram dahil</em></span></a>')

ACIL_HAVUZ = [
 "Acil durumda ilk dakikalar önemli: taşan bir tuvalet ya da dolan bir rögar beklerken büyür. {ad}{loc} acil {kisa} için aradığınızda telefonu bir usta açar, önce suyu nasıl durduracağınızı anlatır, sonra en yakın ekip yola çıkar.",
 "{ad}{loc} acil {kisa} gerektiğinde sabahı beklemeyin. Gece yarısı, hafta sonu ya da bayram fark etmez; servis numaramızı aradığınızda ekip ortalama 30 dakikada adresinizde.",
 "{ad}{loc} acil bir tıkanıklıkta en çok kaybedilen şey zaman. Servis numaramız 7 gün 24 saat açık; aradığınızda adresinizi alıp ekibi hemen yönlendiriyoruz.",
]

def usta_dikkat(i=None):
    tohum_ad = i["slug"] if i else "_genel"
    baslik = f"{ek(i)} gider açma ustası çağırırken dikkat etmeniz gerekenler" if i else "Gider açma ustası çağırırken dikkat etmeniz gerekenler"
    oge = karistir(IC.USTA_DIKKAT, tohum_ad, "ud") if i else IC.USTA_DIKKAT
    return (f'<section class="blok kutu-uyari"><h2>{svg("uyari")} {e(baslik)}</h2>{P(sec(IC.USTA_DIKKAT_GIRIS, tohum_ad, "udg"))}'
            f'{h3_izgara(oge, "is-izgara is-3")}</section>')

ODEME_KISA = "Sorun tamamen giderilmeden ücret talep etmiyoruz; ödemeyi işlem tamamlandıktan sonra alıyoruz."

# hizmete göre fiyat etkenleri (H3)
FIYAT_ETKEN = {
 "tikali-gider-acma": [("Tıkanıklığın yeri", "Lavabo sifonundaki tıkanıklık ile bina kolonundaki tıkanıklık aynı emek değildir."),
                       ("Birikintinin türü", "Saç ve sabun kısa sürede açılır; yağ ve kireç basınçlı su ile yıkama isteyebilir."),
                       ("Erişim", "Temizleme kapağı yoksa ya da sifon gömme ise işe başka bir noktadan girmek gerekir.")],
 "tuvalet-tikanikligi-acma": [("Klozetin tipi", "Yere monte klozet ile asma klozet aynı değildir; asma klozette söküm gerekebilir."),
                       ("Tıkanıklığın yeri", "Klozet dirseğindeki tıkanıklık ile bina kolonundaki tıkanıklık farklı iştir."),
                       ("Sıkışan cisim", "Sert bir cisim sıkıştıysa kamera ve çıkarma işlemi gerekebilir.")],
 "rogar-temizleme": [("Rögarın derinliği", "Derin ve geniş rögarlar daha uzun yıkama ister."),
                       ("Hattın uzunluğu", "Rögar ile sokak arasındaki hat uzadıkça iş uzar."),
                       ("Kök ve çamur", "Kök kesme ve yoğun çamur yıkaması ek işlem demektir.")],
 "kamerali-goruntuleme": [("Hattın uzunluğu", "Ev içi kısa hat ile onlarca metrelik bahçe hattı aynı değildir."),
                       ("Giriş noktası", "Gider ağzından mı, rögardan mı, temizleme kapağından mı girileceği süreyi etkiler."),
                       ("Açma ile birlikte mi?", "Görüntülemenin ardından tıkanıklığı açmak da gerekiyorsa iki iş birlikte değerlendirilir.")],
}
ULAS_IPUCU = {
 "tikali-gider-acma": "Giderin üstüne su dökmeye devam etmeyin; kısa bir video çekip WhatsApp'tan atın, hangi makineyle geleceğimizi oradan anlıyoruz.",
 "tuvalet-tikanikligi-acma": "Su yükseliyorsa sifonu bir daha çekmeyin, rezervuarın altındaki ara musluğu kapatın; sonra bizi arayın.",
 "rogar-temizleme": "Rögar kapağını açtıysanız çevresini işaretleyin, içine eğilmeyin; kapalı rögarda zehirli gaz birikebilir.",
 "kamerali-goruntuleme": "Tıkanıklığın en son ne zaman ve hangi giderde olduğunu not edin; kamerayı nereden süreceğimize birlikte karar veriyoruz.",
}
GECE_HAVUZ = [
 "{ad}{loc} {kisa} için 7 gün 24 saat açığız. Gece yarısı, hafta sonu ya da bayram fark etmez; aradığınızda telefonu bir usta açar ve önce suyu nasıl durduracağınızı anlatır, sonra ekip yola çıkar.",
 "Tıkanıklık mesai saati bilmez :) {ad}{loc} {kisa} için gece de hafta sonu da arayabilirsiniz. Gece çağrısında da gündüzkü ekipmanla, kamerası ve makinesiyle geliyoruz.",
 "{ad}{loc} gece ya da hafta sonu {kisa} gerekiyorsa sabahı beklemeyin; beklemek çoğu zaman taşmayı büyütür. 7/24 açığız ve ekiplerimiz adrese ortalama 30 dakikada ulaşıyor.",
]

def ilce_hizmet_sayfasi(i, h):
    yol = ilce_yolu(i, h); s = i["slug"]; hs = h["slug"]
    IM, HM = IC.ILCE_METIN[s], IC.HIZMET_METIN[hs]
    H1 = h["h1"].format(ad=i["ad"])
    kisa = kucuk(h["kisa"])
    Y = lambda t: yer(t, i, h)
    giris = Y(sec(GIRIS, s, hs, "giris"))
    nedenler = karistir(HM["nedenler"], s, hs, "n")[:2]
    etken = karistir(FIYAT_ETKEN[hs], s, hs, "f")[:2]
    isler = karistir(h["isler"], s, hs, "i")[:4]
    belirti = karistir(h["belirti"], s, hs, "b")[:5]
    oneri = karistir(h["oneri"], s, hs, "o")[:3]
    gal = karistir(h["galeri"], s, hs, "g")
    yakin_ilk = IM["yakin"].split(". ")[0] + "."
    sss_tum = [(Y(q), c) for q, c in h["sss"]] + [("Ücreti ne zaman ödüyorum?", ODEME_KISA + " Fiyatı ise usta yerinde gördükten sonra, işe başlamadan söylüyor.")]
    sss = [sss_tum[0]] + karistir(sss_tum[1:], s, hs, "s")[:3]
    kir_html, kir_ld = kirinti([("Anasayfa", ""), (f"{i['ad']} Gider Açma", ilce_yolu(i)), (h["ad"], None)])
    baslik = h["title"].format(ad=i["ad"])
    aciklama = f"{i['ad']} {kisa}: {h['ozet']} 7/24, ortalama 30 dakikada adreste, ödeme iş bitince. {S['tel_goster']}"
    sema = [sema_hizmet(H1, h["ad"], i, yol), sema_sss(sss), kir_ld]
    diger = [x for x in D.HIZMETLER if x["slug"] != hs]
    kopru_hiz = HIZ["kamerali-goruntuleme"] if hs != "kamerali-goruntuleme" else HIZ["tikali-gider-acma"]
    komsu = [ILCE[k] for k in i["komsu"]]
    govde = f"""
 <section class="blok">
  <h2>{e(Y('{ad}{loc} {kisa} servisine nasıl ulaşırsınız?'))}</h2>
  <p>{e(IM['ulasim'].split('. ')[0])}. Bize {tel_a()} numarasından 7/24 ulaşabilir ya da {wa_a(wa_mesaj(h, i))}. Adresimizi ve yol tarifini <a href="{ic('iletisim/')}">iletişim sayfamızda</a> bulabilirsiniz.</p>
  {ipucu('Tavsiyemiz:', ULAS_IPUCU[hs])}
 </section>
 <section class="blok">
  <h2>{e(Y(sec(['{ad}{loc} {kisa} neden gerekir?', '{ad}{loc} bu tıkanıklık neden olur?', '{ad}{loc} {kisa} çağrılarında en sık ne görüyoruz?'], s, hs, 'nh')))}</h2>
  {P(IM['yerel'][hs])}
  {P(i['gider'] if hs != 'rogar-temizleme' else i['rogar'])}
  {h3_izgara(nedenler)}
  <p>Aynı sorun kısa sürede tekrar ediyorsa açmakla geçmeyen bir sebep vardır; bunu <a href="{ic(ilce_yolu(i, kopru_hiz))}">{e(kopru_hiz['h1'].format(ad=i['ad']))}</a> ile buluyoruz.</p>
 </section>
 <section class="blok">
  <h2>{e(Y(sec(['{ad}{loc} {kisa} nasıl yapılır? Kırmadan çözüm', 'Kırmadan {kisa}: {ad}{loc} nasıl çalışıyoruz?'], s, hs, 'yh')))}</h2>
  {P(HM['yontem'])}
  {P(Y(D.KOPRU[hs]))}
  {h3_izgara(isler)}
 </section>
 {galeri(gal[1:3], Y('{ad} {kisa}: sahadan fotoğraflar'))}
 <section class="blok">
  <h2>{e(Y('{ad} {kisa} fiyatları ne kadar?'))}</h2>
  <p>Her tıkanıklık farklı olduğu için telefonda kesin fiyat vermiyoruz; video ya da fotoğrafla yaklaşık bilgi verebiliyoruz. Kesin fiyatı usta yerinde gördükten sonra, <b>işe başlamadan</b> söylüyor. {e(ODEME_KISA)}</p>
  {P(IM['fiyat'])}
  {h3_izgara(etken)}
  <p>İlçe genelinde fiyatı etkileyen durumları <a href="{ic(ilce_yolu(i))}">{e(i['ad'])} gider açma</a> sayfamızda da anlattık.</p>
 </section>
 <section class="blok">
  <h2>{e(Y('{ad}{loc} {kisa} için belediyeyi aramalı mısınız?'))}</h2>
  {P(Y(HM['belediye']).split('. ')[0] + '.')}
  {P(IM['belediye'])}
  <p>Hangi tıkanıklıkta kimin sorumlu olduğunu <a href="{ic(hiz_yolu(h))}">{e(h['hub_h1'])}</a> sayfamızda tablo hâlinde gösterdik.</p>
 </section>
 <section class="blok">
  <h2>{e(Y('{ad} 7/24 acil {kisa} servisi'))}</h2>
  {P(IM['acil'])}
  {P(Y(sec(ACIL_HAVUZ, s, hs, 'acil')))}
  {servis_no(Y('{ad} acil {kisa} servis numarası'))}
 </section>
 <section class="blok">
  <h2>{e(Y("{ad}{dat} en yakın {kisa} servisi hangisi?"))}</h2>
  <p>{e(yakin_ilk)} Komşu ilçelerde de aynı hizmeti veriyoruz: {', '.join(f'<a href="{ic(ilce_yolu(k, h))}">{e(h["h1"].format(ad=k["ad"]))}</a>' for k in komsu)}.</p>
 </section>
 <section class="blok">
  <h2>{e(Y('Hangi durumlarda {kisa} için aramalısınız?'))}</h2>
  <ul class="tik-liste">{''.join(f'<li>{svg("tik")}<span>{e(b)}</span></li>' for b in belirti)}</ul>
 </section>
 <section class="blok kutu-vurgu">
  <h2>Usta gelene kadar ne yapmalısınız?</h2>
  <ol class="adim-liste">{''.join(f'<li>{e(o)}</li>' for o in oneri)}</ol>
 </section>
 <section class="blok">
  <h2>{e(Y('{ad}{loc} {kisa} hizmeti verdiğimiz mahalleler'))}</h2>
  <p>{e(mahalle_cumle(i, h, hs, 'm'))}</p>
 </section>
 {sss_html(sss, Y(sec(SSS_H2, s, hs, 'sss')))}
 {baglanti_agi(i, h)}"""
    return head(baslik, aciklama, yol, sema) + ust(hs) + hero(
        f"{i['ad']}, Kocaeli · 7/24", e(H1), giris, gorsel(gal[0][0], gal[0][1], oncelik=True), kir_html, h, i) + \
        f'\n<div class="kap">{guven()}</div>\n<div class="kap govde">{govde}\n</div>\n' + \
        cta(f"{i['ad']} için usta mı lazım?", "7/24 arayabilir ya da WhatsApp'tan fotoğraf, video gönderebilirsiniz.", h, i) + alt()

def ilce_sayfasi(i):
    yol = ilce_yolu(i); s = i["slug"]; IM = IC.ILCE_METIN[s]
    H1 = f"{i['ad']} Gider Açma Servisi"
    sss = [
     (f"{ek(i)} hangi gider açma hizmetlerini veriyorsunuz?",
      f"{ek(i)} tıkalı gider açma (lavabo, mutfak, banyo), tuvalet tıkanıklığı açma, rögar temizleme ve kameralı gider görüntüleme hizmeti veriyoruz."),
     (f"{ek(i, 'dat')} ne kadar sürede geliyorsunuz?",
      "Ekiplerimiz Kocaeli'de adrese ortalama 30 dakikada ulaşıyor. Trafik ve o anki iş yoğunluğuna göre süre değişebilir; arama sırasında tahmini süreyi söylüyoruz."),
     (f"{ek(i)} belediye gider açıyor mu?",
      "Hayır. Ev ve bina içindeki tesisat mülk sahibinin sorumluluğundadır; sokaktaki ana kanalizasyon hattı ise İSU'nun. Sokak hattı taşıyorsa ALO 185'i, eviniz ya da binanız tıkalıysa bizi arayın."),
     ("Ücreti ne zaman ödüyorum?", ODEME_KISA + " Fiyatı usta yerinde gördükten sonra, işe başlamadan söylüyor."),
     ("Gece ve hafta sonu çalışıyor musunuz?", "Evet. 7 gün 24 saat hizmet veriyoruz."),
    ]
    kir_html, kir_ld = kirinti([("Anasayfa", ""), ("Hizmet Bölgeleri", "hizmet-bolgeleri/"), (f"{i['ad']} Gider Açma", None)])
    baslik = f"{i['ad']} Gider Açma Servisi | Tıkanıklık, Tuvalet, Rögar · 7/24"
    aciklama = (f"{i['ad']} gider açma servisi: tıkalı gider, tuvalet tıkanıklığı, rögar temizleme, kameralı görüntüleme. "
                f"7/24, ortalama 30 dakikada adreste, ödeme iş bitince. {S['tel_goster']}")
    hizmetler = "".join(
        f'<div class="hsatir"><span class="hsatir-ik">{svg(h["ikon"])}</span><div><h3><a href="{ic(ilce_yolu(i, h))}">{e(h["h1"].format(ad=i["ad"]))}</a></h3>'
        f'<p>{e(IM["yerel"][h["slug"]].split(". ")[0])}. <a href="{ic(ilce_yolu(i, h))}">Devamını okuyun {svg("ok")}</a></p></div></div>'
        for h in D.HIZMETLER)
    komsu = "".join(f'<li><a href="{ic(ilce_yolu(ILCE[k]))}">{e(ILCE[k]["ad"])} gider açma servisi</a></li>' for k in i["komsu"])
    adres = ""
    if s == "basiskele":
        adres = (f'<p class="not">{svg("konum")}<span>Ofisimiz Başiskele\'de: {e(S["adres"])}. '
                 f'<a href="{S["harita"]}" target="_blank" rel="noopener">Haritada aç</a></span></p>')
    sema = [sema_hizmet(H1, "Gider açma", i, yol), sema_sss(sss), kir_ld]
    govde = f"""
 <section class="blok">
  <h2>{e(i['ad'])} Gider Açma Servisine nasıl ulaşırsınız?</h2>
  {P(IM['ulasim'])}
  <p>Telefon: {tel_a()} · WhatsApp: {wa_a(wa_mesaj(None, i), 'mesaj gönderin')} · Ofis: {e(S['adres'])}</p>
  {adres}
 </section>
 <section class="blok">
  <h2>{e(i['ad'])} 7/24 Acil Tıkanıklık Açma Servisi</h2>
  {P(IM['gece'])}
  {P(IM['acil'])}
  {servis_no(f"{i['ad']} 7/24 acil tıkanıklık açma servis numarası")}
 </section>
 <section class="blok">
  <h2>{e(ek(i))} hangi gider açma hizmetlerini veriyoruz?</h2>
  <div class="hliste">{hizmetler}</div>
 </section>
 <section class="blok">
  <h2>{e(ek(i))} belediye gider açma hizmeti veriyor mu?</h2>
  {P(IM['belediye'])}
  {sorumluluk_tablo()}
 </section>
 <section class="blok">
  <h2>{e(i['ad'])} gider açma fiyatları ne kadar?</h2>
  {P(IM['fiyat'])}
  {ipucu('Önemli:', ODEME_KISA)}
 </section>
 {usta_dikkat(i)}
 <section class="blok">
  <h2>{e(ek(i, 'dat'))} en yakın tıkanıklık açma servisi hangisi?</h2>
  {P(IM['yakin'])}
 </section>
 <section class="blok">
  <h2>{e(ek(i))} giderler neden sık tıkanıyor?</h2>
  {''.join(P(i[a]) for a in ('yapi', 'gider', 'rogar', 'saha'))}
 </section>
 <section class="blok">
  <h2>{e(ek(i))} hizmet verdiğimiz mahalleler</h2>
  <ul class="mah-liste">{''.join(f'<li>{e(m)}</li>' for m in i['mahalle'])}</ul>
  <p>{e(mahalle_cumle(i, None, 'hub'))}</p>
 </section>
 {sss_html(sss, f"{i['ad']} gider açma: sık sorulan sorular")}
 <section class="blok"><h2>{e(i['ad'])} çevresindeki ilçeler</h2><ul class="ag-liste">{komsu}<li><a href="{ic('hizmet-bolgeleri/')}">Tüm hizmet bölgeleri</a></li></ul></section>"""
    return head(baslik, aciklama, yol, sema) + ust() + hero(
        f"{i['ad']}, Kocaeli · 7/24", e(H1),
        f"{ek(i)} tıkalı gider, tuvalet tıkanıklığı ve rögar sorunları için 7 gün 24 saat ulaşabileceğiniz ekibiz. Kırmadan, gerektiğinde kamerayla çalışıyor; ödemeyi iş bitince alıyoruz.",
        gorsel(i["banner"], f"{i['ad']} gider açma servisi, {S['tel_goster']}", oncelik=True), kir_html, None, i) + \
        f'\n<div class="kap">{guven()}</div>\n<div class="kap govde">{govde}\n</div>\n' + \
        cta(f"{i['ad']} için gider açma ustası mı lazım?", "7/24 arayabilir ya da WhatsApp'tan yazabilirsiniz.", None, i) + alt()

def hizmet_sayfasi(h):
    yol = hiz_yolu(h); hs = h["slug"]; HM = IC.HIZMET_METIN[hs]
    kisa = kucuk(h["kisa"])
    KO = {"ad": "Kocaeli", "slug": "_kocaeli"}
    Y = lambda t: t.format(ad="Kocaeli", loc="'de", dat="'ye", gen="'nin", abl="'den", kisa=kisa, ozet=h["ozet"])
    sss = [(Y(q), c) for q, c in h["sss"]] + [("Ücreti ne zaman ödüyorum?", ODEME_KISA + " Fiyatı ise usta yerinde gördükten sonra, işe başlamadan söylüyor.")]
    kir_html, kir_ld = kirinti([("Anasayfa", ""), (h["ad"], None)])
    aciklama = f"{h['hub_h1']}: {h['ozet']} Kocaeli'nin 7 ilçesinde 7/24, ödeme iş bitince. {S['tel_goster']}"
    ilceler = "".join(
        f'<div class="hsatir"><span class="hsatir-ik">{svg("konum")}</span><div><h3><a href="{ic(ilce_yolu(i, h))}">{e(h["h1"].format(ad=i["ad"]))}</a></h3>'
        f'<p>{e(IC.ILCE_METIN[i["slug"]]["yerel"][hs].split(". ")[0])}. <a href="{ic(ilce_yolu(i, h))}">Devamını okuyun {svg("ok")}</a></p></div></div>'
        for i in ILCE_SIRALI)
    diger = "".join(kart_hizmet(x) for x in D.HIZMETLER if x["slug"] != hs)
    sema = [sema_hizmet(h["hub_h1"], h["ad"], None, yol), sema_sss(sss), kir_ld]
    bel_h2 = Y("{kisa} için belediyeyi ya da İSU'yu aramalı mısınız?").capitalize()
    govde = f"""
 <section class="blok">
  <h2>{e(Y('Kocaeli {kisa} servisine nasıl ulaşırsınız?'))}</h2>
  <p>Bize {tel_a()} numarasından 7/24 ulaşabilir ya da {wa_a(wa_mesaj(h))}. Ofisimiz Başiskele'de: {e(S['adres'])}. Ekiplerimiz Kocaeli'nin 7 ilçesine ortalama 30 dakikada ulaşıyor.</p>
  {ipucu('Tavsiyemiz:', ULAS_IPUCU[hs])}
 </section>
 <section class="blok">
  <h2>{e(Y(h['hub_neden']))}</h2>
  {P(HM['neden_giris'])}
  {h3_izgara(HM['nedenler'], 'is-izgara is-3')}
 </section>
 <section class="blok">
  <h2>{e(Y('Kırmadan {kisa} nasıl yapılır?'))}</h2>
  {P(HM['yontem'])}
  {h3_izgara(h['isler'])}
 </section>
 {galeri(h['galeri'], Y('{kisa}: sahadan fotoğraflar').capitalize())}
 {fiyat_faktor(Y('Kocaeli {kisa} fiyatları ne kadar?'))}
 {usta_dikkat() if hs == 'tikali-gider-acma' else ''}
 <section class="blok">
  <h2>{e(Y('Kocaeli 7/24 acil {kisa} servisi'))}</h2>
  <p>{e(Y('Kocaeli genelinde acil {kisa} için 7 gün 24 saat açığız. Gece, hafta sonu ya da bayram fark etmez; aradığınızda en yakın ekip yola çıkar ve adresinize ortalama 30 dakikada ulaşır.'))}</p>
  {servis_no(Y('Kocaeli acil {kisa} servis numarası'))}
 </section>
 <section class="blok">
  <h2>{e(bel_h2)}</h2>
  {P(Y(HM['belediye']))}
  {sorumluluk_tablo()}
 </section>
 <section class="blok">
  <h2>{e(Y('Hangi ilçelerde {kisa} hizmeti veriyoruz?'))}</h2>
  <div class="hliste">{ilceler}</div>
 </section>
 <section class="blok">
  <h2>Hangi durumlarda aramalısınız?</h2>
  <ul class="tik-liste">{''.join(f'<li>{svg("tik")}<span>{e(b)}</span></li>' for b in h['belirti'])}</ul>
 </section>
 <section class="blok kutu-vurgu"><h2>Usta gelene kadar ne yapmalısınız?</h2>
  <ol class="adim-liste">{''.join(f'<li>{e(o)}</li>' for o in h['oneri'])}</ol></section>
 {rehber_kutu([r for r in IC.REHBER if r['hizmet'] == hs] or IC.REHBER[-1:])}
 {sss_html(sss, Y('Kocaeli {kisa}: sık sorulan sorular'))}
 <section class="blok"><h2>Diğer hizmetlerimiz</h2><div class="hkart-izgara hkart-3">{diger}</div></section>"""
    return head(h["hub_title"], aciklama, yol, sema) + ust(hs) + hero(
        "Kocaeli · 7 ilçe · 7/24", e(h["hub_h1"]),
        h["ozet"] + " Kocaeli'de 7/24 hizmet veriyoruz; ekiplerimiz adrese ortalama 30 dakikada ulaşıyor, ödemeyi iş bitince alıyoruz.",
        gorsel(h["galeri"][0][0], h["galeri"][0][1], oncelik=True), kir_html, h) + \
        f'\n<div class="kap">{guven()}</div>\n<div class="kap govde">{govde}\n</div>\n' + \
        cta(f"{h['ad']} için hemen ulaşın", "7/24 arayabilir ya da WhatsApp'tan yazabilirsiniz.", h) + alt()

# ── anasayfa ────────────────────────────────────────────────────────────────
ANA_SSS = [
 ("Hangi ilçelere hizmet veriyorsunuz?", "Kocaeli'de " + ve_liste([i["ad"] for i in D.ILCELER]) + " ilçelerine geliyoruz."),
 ("Gece ya da hafta sonu ulaşabilir miyim?", "Evet. 7 gün 24 saat hizmet veriyoruz; telefonla arayabilir ya da WhatsApp'tan yazabilirsiniz."),
 ("Usta ne kadar sürede gelir?", "Ekiplerimiz adrese ortalama 30 dakikada ulaşıyor. Trafik ve iş yoğunluğuna göre süre değişebilir; arama sırasında size tahmini süreyi söylüyoruz."),
 ("Gider açarken kırma yapılıyor mu?", "Hayır, tıkanıklığı gider ağzından makineyle açıyoruz. Gerektiğinde hattın içini kamerayla görüyoruz; kırma ancak boru kırılmış ya da çökmüşse gündeme gelir ve bunu önce görüntüyle size gösteriyoruz."),
 ("Fiyatı ne zaman öğrenirim?", "Fotoğraf ya da videoyla yaklaşık bilgi verebiliyoruz. Kesin fiyatı usta yerinde baktıktan sonra, işe başlamadan önce söylüyor."),
 ("Ödemeyi ne zaman yapıyorum?", "Sorun tamamen giderilmeden ücret talep etmiyoruz; ödemeyi işlem tamamlandıktan sonra, akışı birlikte test ettikten sonra alıyoruz."),
 ("Belediye ya da İSU evimdeki gideri açar mı?", "Hayır. Ev ve bina içindeki tesisat mülk sahibinin sorumluluğundadır. İSU (ALO 185) yalnızca sokaktaki ana kanalizasyon hattına bakar."),
 ("Ofisinize gelebilir miyim?", "Evet. Ofisimiz Kılıçarslan Mah. Hürriyet Cad. No:1, Başiskele/Kocaeli adresinde."),
]

def ana_hero(kam):
    """Anasayfa hero'su. Koyu: tam ekran boru görseli + paralaks. Açık: görsel sağda 3D çerçevede, kamera kartı üstüne biner."""
    kart = f'''<a class="kam-panel koyu" data-egim href="{ic(hiz_yolu(kam))}">
   <span class="kam-b">{svg('kamera')} Kamera ile gider tespiti</span>
   <span class="kam-p">Hattın içini kamerayla görüyor, tıkanıklığın yerini ve sebebini kırmadan buluyoruz.</span>
   <span class="kam-l"><span>{svg('tik')}Tıkanıklığın yeri ve sebebi</span><span>{svg('tik')}Kırmadan karar</span><span>{svg('tik')}Görüntüyü sizinle paylaşma</span></span>
   <em>Nasıl çalışır? {svg('ok')}</em>
  </a>'''
    metin = f'''  <div class="hero-metin">
   <p class="ust-etiket"><span class="canli"></span>Şu an hizmet veriyoruz · Kocaeli · 7/24</p>
   <h1><span class="ad">Kocaeli Tıkalı Gider Açma</span> <span class="vurgu">ortalama 30 dakikada</span> kapınızda</h1>
   <p class="hero-p">Lavabo, mutfak ve banyo gideri, tuvalet tıkanıklığı ve taşan rögar için 7 gün 24 saat ulaşabileceğiniz ekibiz. Tıkanıklığın yerini gerektiğinde kamerayla görüp kırmadan açıyoruz; fiyatı işe başlamadan söylüyoruz.</p>
   <div class="hero-dg">{tel_btn()}{wa_btn(wa_mesaj())}</div>
  </div>'''
    if HERO_KOYU:
        return f'''<section class="hero koyu hero-ana">
 <div class="hero-fon" data-paralaks>{gorsel('hero', '', oncelik=True, boy='100vw')}</div>
 {SAHNE}
 <div class="kap hero-ana-ic">
{metin}
  <div class="hero-derin hero-mobil"><figure class="hero-gorsel">{gorsel('hero', 'Kocaeli tıkalı gider açma: boru hattında akan su', boy='100vw')}</figure><span class="hero-golge"></span></div>
  {kart}
 </div>
</section>'''
    return f'''<section class="hero hero-acik hero-ana-acik">{SAHNE}<div class="kap hero-izgara">
{metin}
 <div class="hero-derin hero-derin-ana"><figure class="hero-gorsel" data-egim>{gorsel('hero', 'Kocaeli tıkalı gider açma: hızlı ve kırmadan çözüm', oncelik=True, boy='(min-width:980px) 560px, 100vw')}</figure><span class="hero-golge"></span>
  {kart.replace('class="kam-panel koyu"', 'class="kam-panel koyu kam-ust"')}</div>
</div></section>'''

def rehber_kutu(liste, baslik="Kendiniz yapmadan önce okuyun"):
    k = "".join(f'<a class="rkart" href="{ic(r["slug"] + "/")}"><span class="skart-ik">{svg(r["ikon"])}</span>'
                f'<span><b>{e(r["h1"])}</b><small>{e(r["ozet"][:120].rsplit(" ", 1)[0])}…</small></span>{svg("ok", "ik skart-ok")}</a>'
                for r in liste)
    return f'<section class="blok"><p class="bolum-ust">Tıkanıklık rehberi</p><h2>{e(baslik)}</h2><div class="rkart-izgara">{k}</div></section>'

def anasayfa():
    kartlar = "".join(kart_hizmet(h) for h in D.HIZMETLER)
    ilceler = "".join(ilce_kart(i) for i in ILCE_SIRALI)
    sema = [{"@context": "https://schema.org", **isletme()}, sema_sss(ANA_SSS)]
    kam = HIZ["kamerali-goruntuleme"]
    saha = [("rogar-yikama", "Rögar borusuna basınçlı su püskürten yıkama başlığı"),
            ("kamerali-tikaniklik-goruntuleme", "Duş giderine sürülen makaralı kameranın ekran ünitesi"),
            ("kirmadan-tikaniklik-acma", "Yer giderinin kapağı açılarak kırmadan tıkanıklık açma"),
            ("kocaeli-tikali-gider-acma-servisi", "Gider açma ekipmanının taşındığı servis aracı")]
    neden_biz = [("Yılların tecrübesi", "Yalnızca tıkanıklık işi yapıyoruz; gider, tuvalet, rögar ve kameralı görüntüleme. Bir işte uzmanlaşınca o işi hem hızlı hem temiz yapıyorsunuz."),
                 ("Kırmadan, son teknoloji cihazlarla", "Spiral makinesi, basınçlı yıkama ve kamera araçta. Tıkanıklığı tahminle değil görüntüyle buluyor, kırmadan açıyoruz."),
                 ("Ödeme iş bitince", "Sorun tamamen giderilmeden ücret talep etmiyoruz. Fiyatı işe başlamadan söylüyor, ödemeyi işlem tamamlandıktan sonra alıyoruz."),
                 ("Ofisimiz Başiskele'de", "Adresi belli bir firmayız: Kılıçarslan Mah. Hürriyet Cad. No:1, Başiskele/Kocaeli. Yolunuz düşerse uğrayabilirsiniz.")]
    ilce_bag = ", ".join(f'<a href="{ic(ilce_yolu(i))}">{e(i["ad"])}</a>' for i in ILCE_SIRALI)
    return head("Kocaeli Tıkalı Gider Açma | 7/24 Acil Tıkanıklık Açma Servisi",
                "Kocaeli tıkalı gider açma: tuvalet tıkanıklığı, rögar temizleme, kameralı görüntüleme. 7/24 acil servis, "
                f"kırmadan, ödeme iş bitince. Servis numarası {S['tel_goster']}", "", sema) + ust() + f"""
{ana_hero(kam)}
<div class="kap">{guven()}</div>
<div class="kap govde">
 {sorun_secici()}
 <section class="blok">
  <p class="bolum-ust">İletişim</p><h2>Kocaeli Tıkalı Gider Açma Servisine nasıl ulaşırsınız?</h2>
  <p>Bize {tel_a()} numarasından 7 gün 24 saat ulaşabilir ya da {wa_a(wa_mesaj())}. Mümkünse sorunun kısa bir videosunu atın; videoya bakıp hangi makineyle geleceğimize karar veriyoruz. Ofisimiz Başiskele'de: {e(S['adres'])}. Ekiplerimiz {ilce_bag} ilçelerine ortalama 30 dakikada ulaşıyor.</p>
 </section>
 <section class="blok"><p class="bolum-ust">Hizmetlerimiz</p><h2>Kocaeli'de hangi gider açma hizmetlerini veriyoruz?</h2>
  <p class="blok-giris">Her hizmetin ilçenize özel sayfasında, o bölgedeki binalarda en sık karşılaştığımız durumları da anlattık.</p>
  <div class="hkart-izgara">{kartlar}</div></section>
 <section class="blok"><p class="bolum-ust">Hakkımızda</p><h2>Neden Kocaeli Tıkalı Gider Açma?</h2>
  {P(IC.TANITIM)}
  {h3_izgara(neden_biz)}
  <p><a class="metin-bag" href="{ic('hakkimizda/')}">Hakkımızda daha fazlası {svg('ok')}</a></p></section>
 <section class="blok">
  <p class="bolum-ust">Acil servis</p><h2>Kocaeli 7/24 Acil Tıkanıklık Açma Servisi</h2>
  <p>Gece yarısı taşan bir tuvalet, sabaha karşı dolan bir rögar, bayram sabahı kapanan bir mutfak gideri… Tıkanıklık mesai saati bilmiyor, biz de bilmiyoruz :) Kocaeli'nin 7 ilçesinde 7 gün 24 saat acil tıkanıklık açma servisi veriyoruz; aradığınızda önce suyu nasıl durduracağınızı anlatıyor, sonra en yakın ekibi yola çıkarıyoruz.</p>
  {servis_no("Kocaeli 7/24 acil tıkanıklık açma servis numarası")}
 </section>
 <section class="blok" id="bolgeler"><p class="bolum-ust">Hizmet bölgeleri</p><h2>Kocaeli'de hangi ilçelere hizmet veriyoruz?</h2>
  <p class="blok-giris">İlçenizi seçin; o ilçedeki dört hizmetin sayfasına oradan ulaşabilirsiniz. Merkezimiz Başiskele'de.</p>
  <div class="bolge-ana">{kocaeli_harita()}<div class="ikart-izgara ikart-2">{ilceler}</div></div></section>
 {kamera_demo()}
 <section class="blok"><p class="bolum-ust">Süreç</p><h2>Tıkanıklık açma süreci nasıl işliyor?</h2>
  <div class="surec-kap"><div class="boru" aria-hidden="true"><span class="boru-su"></span></div>
  <ol class="surec">
   <li><h3>Arayın</h3><span>Sorunu anlatın; mümkünse WhatsApp'tan fotoğraf ya da kısa video gönderin.</span></li>
   <li><h3>Adresinizi alalım</h3><span>Mahalle ve sokağı netleştirip size en yakın ekibi yönlendiriyoruz.</span></li>
   <li><h3>Ekibimiz gelsin</h3><span>Ortalama 30 dakikada adresteyiz; usta durumu görüp fiyatı işe başlamadan söylüyor.</span></li>
   <li><h3>Sorunu çözelim</h3><span>Kırmadan açıyor, akışı birlikte test ediyoruz; ödemeyi iş bitince alıyoruz.</span></li>
  </ol></div></section>
 <section class="blok">
  <p class="bolum-ust">Sorumluluk</p><h2>Kocaeli'de belediye gider açar mı?</h2>
  <p>Bu soruyu çok sık duyuyoruz. Kısa cevap: hayır. Belediye ya da İSU evinizdeki lavabo, tuvalet veya bina kolonunuzdaki tıkanıklığa ekip göndermez; bunlar mülk sahibinin sorumluluğundadır. İSU yalnızca sokaktaki ana kanalizasyon hattına bakar ve ona ALO 185 üzerinden 7/24 ulaşabilirsiniz. Ayrımı yapmanın en kolay yolu sokaktaki rögara bakmak: sokak rögarı da doluysa 185'i, sokak boş ama sizin gideriniz ya da bahçe rögarınız doluysa bizi arayın.</p>
  {sorumluluk_tablo()}
 </section>
 {uzmanlik()}
 {fiyat_faktor("Kocaeli'de gider açma fiyatları ne kadar?")}
 {usta_dikkat()}
 {rehber_kutu(IC.REHBER, "Tıkanıklık rehberi: evde ne yapabilirsiniz?")}
 {galeri(saha, "Sahadan fotoğraflar")}
 {yorumlar()}
 {konum_blok()}
 {sss_html(ANA_SSS)}
</div>
{cta("Gideriniz mi tıkandı?", "7/24 arayabilir ya da WhatsApp'tan yazabilirsiniz. Ortalama 30 dakikada adresinizdeyiz.")}
""" + alt()

def capa(metin):
    t = kucuk(metin)
    for a, b in zip("çğıöşüâ", "cgiosua"): t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]

def rehber_sayfasi(r):
    yol = r["slug"] + "/"
    h = HIZ[r["hizmet"]]
    govde = []
    for baslik, ogeler in r["bolum"]:
        parca = []
        for o in ogeler:
            if isinstance(o, str): parca.append(P(o))
            elif o[0] == "h3": parca.append(f"<h3>{e(o[1])}</h3>{P(o[2])}")
            elif o[0] == "liste": parca.append('<ul class="tik-liste tik-tek">' + "".join(f'<li>{svg("tik")}<span>{bagla(x)}</span></li>' for x in o[1]) + "</ul>")
            elif o[0] == "adim": parca.append('<ol class="adim-liste">' + "".join(f"<li>{bagla(x)}</li>" for x in o[1]) + "</ol>")
            elif o[0] == "ipucu": parca.append(ipucu("Tavsiyemiz:", o[1]))
            elif o[0] == "dikkat": parca.append(ipucu("Dikkat:", o[1], sinif="ipucu ipucu-dikkat"))
            elif o[0] == "tablo":
                parca.append('<div class="tablo-kap"><table class="tablo"><thead><tr>' + "".join(f"<th>{e(x)}</th>" for x in o[1]) +
                             "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{e(x)}</td>" for x in sat) + "</tr>" for sat in o[2]) + "</tbody></table></div>")
        govde.append(f'<section class="blok makale" id="{capa(baslik)}"><h2>{e(baslik)}</h2>{"".join(parca)}</section>')
    icindekiler = "".join(f'<li><a href="#{capa(b)}">{e(b)}</a></li>' for b, _ in r["bolum"])
    diger = [x for x in IC.REHBER if x["slug"] != r["slug"]]
    kir_html, kir_ld = kirinti([("Anasayfa", ""), ("Rehber", "rehber/"), (r["h1"].split("?")[0] + "?", None)])
    makale = {"@context": "https://schema.org", "@type": "Article", "headline": r["h1"], "description": r["aciklama"],
              "inLanguage": "tr", "datePublished": "2026-10-05", "dateModified": BUGUN,
              "author": {"@type": "Organization", "name": S["marka"], "url": ALAN + "/"},
              "publisher": {"@id": ALAN + "/#isletme"}, "mainEntityOfPage": ALAN + "/" + yol,
              "image": ALAN + f"/images/{r['gorsel'][0]}-960.webp"}
    sema = [makale, sema_sss(r["sss"]), kir_ld]
    return head(r["title"], r["aciklama"], yol, sema) + ust("rehber") + hero(
        "Tıkanıklık rehberi", e(r["h1"]), r["ozet"], gorsel(r["gorsel"][0], r["gorsel"][1], oncelik=True), kir_html, h) + f"""
<div class="kap govde makale-govde">
 <nav class="icindekiler" aria-label="Bu yazıda"><b>Bu yazıda neler var?</b><ol>{icindekiler}</ol></nav>
 {''.join(govde)}
 <section class="blok kutu-vurgu"><h2>Uğraşmak istemiyorsanız</h2>
  <p>Evde denediniz ve olmadı, ya da hiç uğraşmak istemiyorsunuz; çok normal :) <a href="{ic(hiz_yolu(h))}">{e(h['ad'])}</a> için 7/24 arayabilirsiniz. Kırmadan açıyor, ödemeyi iş bitince alıyoruz.</p>
  {servis_no("7/24 acil tıkanıklık açma servis numarası")}</section>
 {sss_html(r['sss'], "Sık sorulan sorular")}
 {rehber_kutu(diger, "Diğer rehber yazıları")}
</div>
{cta("Kendiniz açamadınız mı?", "7/24 arayabilir ya da WhatsApp'tan fotoğraf gönderebilirsiniz.", h)}
""" + alt()

def rehber_ana():
    k = "".join(f"""<section class="blok rehber-ozet"><h2><a href="{ic(r['slug'] + '/')}">{e(r['h1'])}</a></h2>{P(r['ozet'])}
  <ul class="ag-liste">{''.join(f'<li>{e(b)}</li>' for b, _ in r['bolum'][:4])}</ul>
  <p><a class="metin-bag" href="{ic(r['slug'] + '/')}">Yazının tamamını okuyun {svg('ok')}</a></p></section>""" for r in IC.REHBER)
    govde = f'<p class="blok-giris">{e(IC.REHBER_GIRIS)}</p>{k}{uzmanlik()}{usta_dikkat()}'
    return basit("Tıkanıklık Rehberi | Lavabo, Tuvalet, Gider Açma Soruları",
                 "Lavabo ve tuvalet tıkanırsa ne yapmalı, tıkalı gideri kendiniz açabilir misiniz, gider açma aparatı nereden alınır? Ustadan dürüst cevaplar.",
                 "rehber/", "Tıkanıklık Rehberi", govde, "rehber")

def hakkimizda():
    k = "".join(f'<section class="blok"><h2>{e(b)}</h2>{"".join(P(x) for x in ps)}</section>' for b, ps in IC.HAKKIMIZDA)
    govde = (f'<div class="hakkimizda-g">{gorsel("kocaeli-tikali-gider-acma-servisi", "Gider açma ekipmanının taşındığı servis aracımız", boy="(min-width:980px) 420px, 100vw")}</div>'
             + k + usta_dikkat() + konum_blok())
    return basit("Hakkımızda | Kocaeli Tıkalı Gider Açma · Başiskele",
                 "Kocaeli Tıkalı Gider Açma: yılların tecrübesiyle kırmadan tıkanıklık açma, ödeme iş bitince. Ofis: Kılıçarslan Mah. Hürriyet Cad. No:1, Başiskele.",
                 "hakkimizda/", "Hakkımızda", govde, "hakkimizda")

# ── diğer sayfalar ──────────────────────────────────────────────────────────
def basit(baslik, aciklama, yol, h1, govde, aktif="", robots="index,follow"):
    kir_html, kir_ld = kirinti([("Anasayfa", ""), (h1, None)])
    return head(baslik, aciklama, yol, [kir_ld], robots) + ust(aktif) + f"""
<section class="hero {HK} hero-dar"><div class="kap"><div class="hero-metin">{kir_html}<h1>{e(h1)}</h1></div></div></section>
<div class="kap govde">{govde}</div>
{cta("Gideriniz mi tıkandı?", "7/24 arayabilir ya da WhatsApp'tan yazabilirsiniz.")}
""" + alt()

def bolgeler():
    satir = []
    for i in ILCE_SIRALI:
        l = "".join(f'<li><a href="{ic(ilce_yolu(i, h))}">{e(h["h1"].format(ad=i["ad"]))}</a></li>' for h in D.HIZMETLER)
        satir.append(f'<section class="bolge"><h2><a href="{ic(ilce_yolu(i))}">{e(i["ad"])} gider açma</a></h2><ul>{l}</ul></section>')
    govde = (f'<p class="blok-giris">Kocaeli\'de {len(D.ILCELER)} ilçeye 7/24 servis veriyoruz. Merkezimiz Başiskele\'de; '
             f'ekiplerimiz adrese ortalama 30 dakikada ulaşıyor.</p>{kocaeli_harita()}<div class="bolge-izgara">{"".join(satir)}</div>')
    return basit("Hizmet Bölgeleri | Kocaeli Tıkalı Gider Açma · 7 İlçe",
                 "Kocaeli Tıkalı Gider Açma'nın hizmet verdiği ilçeler: İzmit, Başiskele, Gölcük, Derince, Körfez, Kartepe, Karamürsel.",
                 "hizmet-bolgeleri/", "Hizmet Bölgeleri", govde, "bolge")

def iletisim():
    govde = f"""<section class="blok iletisim">
 <div class="ilt-kart">{svg('tel')}<div><h2>Telefon</h2><p><a href="tel:{S['tel_link']}">{S['tel_goster']}</a></p></div></div>
 <div class="ilt-kart">{svg('wa')}<div><h2>WhatsApp</h2><p>Fotoğraf ya da video göndererek sorunu anlatabilirsiniz.</p>{wa_btn(wa_mesaj())}</div></div>
 <div class="ilt-kart">{svg('konum')}<div><h2>Adres</h2><p>{e(S['adres'])}</p><p><a href="{S['harita']}" target="_blank" rel="noopener">Haritada aç</a></p></div></div>
 <div class="ilt-kart">{svg('saat')}<div><h2>Çalışma saatleri</h2><p>7 gün 24 saat · <span class="durum-rozet durum-ic"><span class="canli"></span>şu an açık</span></p><p><a href="{ic('hizmet-bolgeleri/')}">Hizmet bölgeleri</a></p></div></div>
</section>
{konum_blok()}"""
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
    yollar.append(sayfa("rehber/", rehber_ana))
    for r in IC.REHBER: yollar.append(sayfa(r["slug"] + "/", rehber_sayfasi, r))
    yollar += [sayfa("hizmet-bolgeleri/", bolgeler), sayfa("hakkimizda/", hakkimizda), sayfa("iletisim/", iletisim),
               sayfa("gizlilik-politikasi/", gizlilik)]
    ONEK = "/"
    yaz("404.html", hata404())
    sm = "".join(f"<url><loc>{ALAN}/{y}</loc><lastmod>{BUGUN}</lastmod></url>" for y in yollar if y != "gizlilik-politikasi/")
    yaz("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    yaz("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {ALAN}/sitemap.xml\n")
    yaz("CNAME", S["cname"] + "\n")
    # IndexNow anahtarı (Bing/Yandex; Google kullanmaz) — kökteki dcba226538277f4dda1e62b717c061c0.txt build'den bağımsız durur, ⛔ silme
    print(f"{len(yollar)} sayfa üretildi")

if __name__ == "__main__":
    main()
