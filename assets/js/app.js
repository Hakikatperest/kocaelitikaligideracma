/* Kocaeli Tıkalı Gider Açma — app.js
   1) mobil menü  2) mobil hızlı iletişim (#dock) sayfa başında ve dibinde gizlenir (hero düğmeleri / imza)
   3) Google Ads dönüşümü: tel: ve wa.me tıklaması → window.W4_ADS.tel / .wa (send_to etiketi)
   4) 3D katmanı: kabarcık sahnesi (canvas, kütüphanesiz izdüşüm) · [data-egim] kart eğimi · hero paralaksı · .rv açılışı
   ⚠️ Açılışta IntersectionObserver KULLANMA (Tessa'da 20 öğe hiç açılmadı) — rAF + dikdörtgen kontrolü + 6 sn güvenlik ağı. */
(function () {
  var dg = document.querySelector('.menu-ac'), menu = document.getElementById('menu');
  if (dg && menu) {
    // Menü açıkken arka plan kaydırılmaz: html'e .menu-acik → CSS overflow:hidden + touchmove kilidi (eski iOS overflow'u yok sayar).
    // ⚠️ body'yi position:fixed yapma — sticky başlık sayfayla birlikte yukarı kayıp kaybolur.
    var ayarla = function (acik) {
      menu.classList.toggle('acik', acik);
      document.documentElement.classList.toggle('menu-acik', acik);
      dg.setAttribute('aria-expanded', acik ? 'true' : 'false');
      dg.setAttribute('aria-label', acik ? 'Menüyü kapat' : 'Menüyü aç');
    };
    dg.addEventListener('click', function () { ayarla(!menu.classList.contains('acik')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) ayarla(false); });
    // perdeye (menü ve başlık dışına) dokununca kapan
    document.addEventListener('click', function (e) {
      if (menu.classList.contains('acik') && !e.target.closest('.ust')) ayarla(false);
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('acik')) { ayarla(false); dg.focus(); } });
    window.addEventListener('resize', function () { if (window.innerWidth > 1080 && menu.classList.contains('acik')) ayarla(false); });
    // menü dışındaki dokunmatik kaydırmayı engelle; menünün kendi içi (uzunsa) kayabilir
    document.addEventListener('touchmove', function (e) {
      if (menu.classList.contains('acik') && !e.target.closest('#menu')) e.preventDefault();
    }, { passive: false });
  }

  var dock = document.getElementById('dock');
  if (dock) {
    var bekle = false;
    var kontrol = function () {
      bekle = false;
      var kalan = document.documentElement.scrollHeight - (window.scrollY + window.innerHeight);
      dock.classList.toggle('gizli', kalan < 140 || window.scrollY < 380);  // sayfa başında hero düğmeleri zaten görünüyor
    };
    window.addEventListener('scroll', function () { if (!bekle) { bekle = true; requestAnimationFrame(kontrol); } }, { passive: true });
    kontrol();
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    var ads = window.W4_ADS;
    if (!a || !ads || typeof window.gtag !== 'function') return;
    var href = a.getAttribute('href') || '';
    var tur = href.indexOf('tel:+905358151804') === 0 ? 'tel' : (href.indexOf('wa.me/') !== -1 ? 'wa' : '');
    if (!tur || !ads[tur]) return;
    window.gtag('event', 'conversion', { send_to: ads.etiket + '/' + ads[tur] });
  });
  // ── PRO bileşenler (hareket tercihinden bağımsız çalışır) ─────────────
  // canlı saat (7/24 açık olduğu için durum hep "açık"; yalnız Türkiye saati gösterilir)
  var saatYaz = function () {
    var t;
    try { t = new Intl.DateTimeFormat('tr-TR', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Istanbul' }).format(new Date()); } catch (x) { return; }
    [].forEach.call(document.querySelectorAll('.durum-saat'), function (el) { el.textContent = 'saat ' + t; });
  };
  saatYaz(); setInterval(saatYaz, 30000);

  // teklif formu → WhatsApp mesajı (sitede veri saklanmaz)
  [].forEach.call(document.querySelectorAll('form[data-teklif]'), function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var ilce = f.elements.ilce.value, sorun = f.elements.sorun.value, not = f.elements.text.value.trim();
      var msj = 'Merhaba, fiyat bilgisi almak istiyorum.\n' + (ilce ? 'İlçe: ' + ilce + '\n' : '') + 'Sorun: ' + sorun + (not ? '\nNot: ' + not : '');
      var ads = window.W4_ADS;
      if (ads && ads.wa && typeof window.gtag === 'function') window.gtag('event', 'conversion', { send_to: ads.etiket + '/' + ads.wa });
      window.open(f.getAttribute('action') + '?text=' + encodeURIComponent(msj), '_blank', 'noopener');
    });
  });

  // harita: tıklanana kadar Google Haritalar yüklenmez (üçüncü parti istek 0)
  [].forEach.call(document.querySelectorAll('[data-harita]'), function (k) {
    var b = k.querySelector('.harita-ac');
    if (!b) return;
    b.addEventListener('click', function () {
      var fr = document.createElement('iframe');
      fr.src = k.getAttribute('data-harita'); fr.title = 'Konum haritası'; fr.loading = 'lazy';
      fr.referrerPolicy = 'no-referrer-when-downgrade';
      k.innerHTML = ''; k.appendChild(fr);
    });
  });

  // ilçe kartı ↔ şematik harita vurgusu
  [].forEach.call(document.querySelectorAll('.ikart[data-ilce]'), function (kart) {
    var hb = document.querySelector('.hb[data-ilce="' + kart.getAttribute('data-ilce') + '"]');
    if (!hb) return;
    var ac = function () { hb.classList.add('vurgu'); }, kapa = function () { hb.classList.remove('vurgu'); };
    kart.addEventListener('pointerenter', ac); kart.addEventListener('pointerleave', kapa);
    kart.addEventListener('focus', ac); kart.addEventListener('blur', kapa);
  });

  // ── 3D katmanı ──────────────────────────────────────────────────────────
  var azHareket = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var inceIsaret = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (azHareket) return;

  // a) kaydırınca derinlikten açılış — .rv'yi JS ekler; JS patlarsa içerik zaten görünür
  var hedefler = [].slice.call(document.querySelectorAll(
    '.govde .blok>h2,.bolum-ust,.blok-giris,.hkart,.ikart,.is,.tik-liste li,.galeri figure,.surec li,.sss-oge,.guven li,.bolge,.ilt-kart,.kutu-vurgu,.mah-liste li,.ilce-izgara li,.cta-ic>*'));
  hedefler.forEach(function (el) {
    var kardes = el.parentElement ? [].indexOf.call(el.parentElement.children, el) : 0;
    el.style.setProperty('--gec', Math.min(kardes, 6) * 70 + 'ms');
    el.classList.add('rv');
  });
  var acBekle = false;
  var ac = function () {
    acBekle = false;
    var alt = window.innerHeight * 0.92;
    for (var i = hedefler.length - 1; i >= 0; i--) {
      var r = hedefler[i].getBoundingClientRect();
      // geçilip gidilenler de açılsın (hızlı kaydırma, # bağlantısı) → yalnız üst sınır
      if (r.top < alt) { hedefler[i].classList.add('gor'); hedefler.splice(i, 1); }
    }
  };
  window.addEventListener('scroll', function () { if (!acBekle) { acBekle = true; requestAnimationFrame(ac); } }, { passive: true });
  window.addEventListener('resize', ac);
  requestAnimationFrame(ac);
  setTimeout(function () { hedefler.forEach(function (el) { el.classList.add('gor'); }); hedefler = []; }, 6000); // ⛔ güvenlik ağı — kaldırma

  // b) fareyle eğilen kartlar (yalnız fare/kalem; dokunmatikte kapalı)
  if (inceIsaret) {
    [].forEach.call(document.querySelectorAll('[data-egim]'), function (el) {
      var guc = el.classList.contains('hero-gorsel') ? 6 : (el.classList.contains('kam-panel') ? 8 : 10);
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        el.style.setProperty('--ry', ((x - 0.5) * guc).toFixed(2) + 'deg');
        el.style.setProperty('--rx', ((0.5 - y) * guc).toFixed(2) + 'deg');
        el.style.setProperty('--gx', (x * 100).toFixed(1) + '%');
        el.style.setProperty('--gy', (y * 100).toFixed(1) + '%');
        el.classList.add('egim-aktif');
      });
      el.addEventListener('pointerleave', function () {
        el.classList.remove('egim-aktif');
        el.style.setProperty('--rx', '0deg'); el.style.setProperty('--ry', '0deg');
      });
    });
  }

  // kamera demosu: mesafe sayacı kafanın animasyonuyla eşzamanlı (0 → 3,2 m, temsilî)
  var sayac = document.querySelector('.m-sayac'), bas = document.querySelector('.kam-bas');
  if (sayac && bas && bas.getAnimations) {
    var sayacGuncelle = function () {
      var a = bas.getAnimations()[0];
      if (a && a.currentTime != null) {
        var t = (a.currentTime % 8000) / 8000, ilerle = t < 0.6 ? t / 0.6 : (t < 0.92 ? 1 : 1 - (t - 0.92) / 0.08);
        var en = 1 - Math.pow(1 - ilerle, 2);
        sayac.textContent = (en * 3.2).toFixed(1).replace('.', ',');
      }
      setTimeout(sayacGuncelle, 120);
    };
    sayacGuncelle();
  }

  // c) hero: kabarcık sahnesi + paralaks
  var hero = document.querySelector('.hero');
  var tuval = hero && hero.querySelector('.kabarcik');
  var fon = document.querySelector('[data-paralaks]');
  var fare = { x: 0, y: 0, hx: 0, hy: 0 };
  if (hero && inceIsaret) {
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      fare.hx = (e.clientX - r.left) / r.width - 0.5; fare.hy = (e.clientY - r.top) / r.height - 0.5;
    });
    hero.addEventListener('pointerleave', function () { fare.hx = 0; fare.hy = 0; });
  }
  if (!tuval || !tuval.getContext) return;
  var ctx = tuval.getContext('2d'), dpr = Math.min(window.devicePixelRatio || 1, 2), W = 0, H = 0;
  var adet = window.innerWidth < 760 ? 26 : 60, F = 420, kabarciklar = [];
  // tek seferlik kabarcık görseli (her karede gradyan çizmemek için)
  var sprite = document.createElement('canvas'); sprite.width = sprite.height = 64;
  var sc = sprite.getContext('2d');
  var g = sc.createRadialGradient(24, 22, 2, 32, 32, 31);
  var acik = hero.classList.contains('hero-acik');
  if (acik) {   // açık zeminde beyaz parlama kaybolur → kenarı koyu mavi kabarcık
    g.addColorStop(0, 'rgba(255,255,255,1)'); g.addColorStop(.2, 'rgba(186,230,253,.7)');
    g.addColorStop(.6, 'rgba(14,165,233,.14)'); g.addColorStop(.88, 'rgba(3,105,161,.55)'); g.addColorStop(1, 'rgba(3,105,161,0)');
  } else {
    g.addColorStop(0, 'rgba(255,255,255,.95)'); g.addColorStop(.18, 'rgba(190,235,255,.55)');
    g.addColorStop(.6, 'rgba(34,184,255,.12)'); g.addColorStop(.9, 'rgba(34,184,255,.45)'); g.addColorStop(1, 'rgba(34,184,255,0)');
  }
  sc.fillStyle = g; sc.beginPath(); sc.arc(32, 32, 31, 0, Math.PI * 2); sc.fill();
  var yeni = function (b, bas) {
    b.x = (Math.random() - 0.5) * 1600; b.y = (Math.random() - 0.5) * 900;
    b.z = bas ? 200 + Math.random() * 1400 : 1600; b.r = 6 + Math.random() * 16;
    b.vz = 1.2 + Math.random() * 2.2; b.vy = -0.25 - Math.random() * 0.6; b.f = Math.random() * 6.28;
    return b;
  };
  for (var k = 0; k < adet; k++) kabarciklar.push(yeni({}, true));
  var boyut = function () {
    var r = hero.getBoundingClientRect(); W = r.width; H = r.height;
    tuval.width = Math.round(W * dpr); tuval.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  };
  boyut(); window.addEventListener('resize', boyut);
  var gorunur = true;
  var ciz = function (t) {
    fare.x += (fare.hx - fare.x) * 0.06; fare.y += (fare.hy - fare.y) * 0.06;
    var sy = window.scrollY;
    gorunur = sy < H + 50 && !document.hidden;
    if (fon) fon.style.transform = 'translate3d(' + (fare.x * -24).toFixed(1) + 'px,' + (sy * 0.28 + fare.y * -16).toFixed(1) + 'px,0) scale(1.06)';
    if (gorunur) {
      ctx.clearRect(0, 0, W, H);
      var cx = W * (0.62 + fare.x * 0.08), cy = H * (0.5 + fare.y * 0.08);
      kabarciklar.sort(function (a, b) { return b.z - a.z; });
      for (var i = 0; i < kabarciklar.length; i++) {
        var b = kabarciklar[i];
        b.z -= b.vz; b.y += b.vy; b.f += 0.02;
        if (b.z < 40) yeni(b, false);
        var olcek = F / b.z;
        var px = cx + (b.x + Math.sin(b.f) * 18 - fare.x * 160) * olcek;
        var py = cy + (b.y - fare.y * 100) * olcek;
        var rr = Math.min(b.r * olcek, acik ? 34 : 999);   // açık zeminde dev kabarcık yazıyı bulandırıyordu
        if (px < -rr || px > W + rr || py < -rr || py > H + rr) { if (b.z < 300) yeni(b, false); continue; }
        ctx.globalAlpha = Math.max(0, Math.min(1, (1600 - b.z) / 900)) * Math.min(1, b.z / 160) * (acik ? 0.6 : 0.85);
        ctx.drawImage(sprite, px - rr, py - rr, rr * 2, rr * 2);
      }
      ctx.globalAlpha = 1;
    }
    requestAnimationFrame(ciz);
  };
  requestAnimationFrame(ciz);
})();
