# -*- coding: utf-8 -*-
"""Görsel türevleri + favicon. Kaynak: _src/kaynak/ (kullanıcının yüklediği orijinaller). Çıktı: images/, kökte favicon.
Çalıştır: python3 _src/media.py   (build.py'den önce, yalnızca görsel değişince)

⚠️ Derince ve Gölcük banner'larının alt şeridinde BAŞKA alan adı yazıyor
   (derincetikaligideracma.com / golcuktikaligideracma.com) → o şerit kırpılıyor (KIRP)."""
import os
from PIL import Image, ImageDraw

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(KOK, "_src", "kaynak")
CIKTI = os.path.join(KOK, "images")

FOTO_GEN = (480, 960)       # saha fotoğrafları
BANNER_GEN = (640, 1024)    # yazılı banner'lar (küçük türevde yazı okunmuyor)
KIRP = {"derince-gider-acma-servisi.webp": 0.868, "golcuk-gider-acma-servisi.webp": 0.815}  # üstten tutulacak oran

def banner_mi(ad): return im_boyut(ad)[0] == 1024 and ad != "hero.webp"
def im_boyut(ad): return Image.open(os.path.join(KAYNAK, ad)).size

def turev():
    os.makedirs(CIKTI, exist_ok=True)
    for ad in sorted(os.listdir(KAYNAK)):
        if not ad.endswith(".webp"): continue
        im = Image.open(os.path.join(KAYNAK, ad)).convert("RGB")
        if ad in KIRP: im = im.crop((0, 0, im.width, round(im.height * KIRP[ad])))
        taban = ad[:-5]
        genler = BANNER_GEN if banner_mi(ad) else ((768, 1280) if ad == "hero.webp" else FOTO_GEN)
        for g in genler:
            k = im.copy()
            if k.width > g: k = k.resize((g, round(k.height * g / k.width)), Image.LANCZOS)
            k.save(os.path.join(CIKTI, f"{taban}-{g}.webp"), "WEBP", quality=78 if g < 1000 else 74, method=6)
        print(taban, genler)
    # og:image için JPEG (bazı paylaşım önizlemeleri WebP okumuyor)
    Image.open(os.path.join(KAYNAK, "hero.webp")).convert("RGB").resize((1200, 806), Image.LANCZOS).save(
        os.path.join(CIKTI, "og-kocaeli-tikali-gider-acma.jpg"), quality=82, optimize=True)

def favicon():
    # Lacivert yuvarlak kare + mavi damla. ⚠️ WebP favicon Google'da görünmez → ico + png.
    S = 512
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=112, fill=(8, 20, 40, 255))
    # damla: üstte sivri, altta daire
    d.ellipse((136, 196, 376, 436), fill=(34, 184, 255, 255))
    d.polygon([(256, 64), (148, 270), (364, 270)], fill=(34, 184, 255, 255))
    d.ellipse((196, 290, 252, 346), fill=(255, 255, 255, 200))
    im.resize((48, 48), Image.LANCZOS).save(os.path.join(KOK, "favicon.ico"), sizes=[(48, 48), (32, 32), (16, 16)])
    for b in (48, 96, 180, 192, 512):
        im.resize((b, b), Image.LANCZOS).save(os.path.join(CIKTI, f"favicon-{b}.png"), optimize=True)
    print("favicon tamam")

if __name__ == "__main__":
    turev(); favicon()
