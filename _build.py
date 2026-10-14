#!/usr/bin/env python3
"""Genera il sito Panetta (statico, per GitHub Pages).
  python3 _build.py              -> genera le pagine in questa cartella
  python3 _build.py --preview X  -> genera una copia di anteprima in X (link con index.html)
Testi e contatti: qui sotto. Prezzi: menu_data.py
"""
import json, os, sys, html, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from menu_data import MENU

SRC = os.path.dirname(os.path.abspath(__file__))
DOMINIO = "https://panettabakery.com"
TEL_B = ("0861 1640185", "+3908611640185")
TEL_P = ("334 8919180", "+393348919180")
EMAIL = "panetta.social@gmail.com"
INSTA = "https://www.instagram.com/panetta_bakery_colledara/"
MAPS_B = "https://www.google.com/maps/search/?api=1&query=Panetta+Bakery+Via+Nuova+7+Colledara"
MAPS_P = "https://www.google.com/maps/search/?api=1&query=Via+del+Mulino+Cerchiara+Isola+del+Gran+Sasso"
IUB = "https://www.iubenda.com/privacy-policy/91127097"

# pagine: chiave -> percorso (stessi URL del vecchio sito)
PAGINE = {"home": "", "panificio": "panificiodicerchiara/", "menu": "asportomenu/"}
e = html.escape
PREVIEW = False

def url(chiave, depth):
    p = PAGINE[chiave]
    if PREVIEW: p = p + "index.html"
    return ("../" * depth + p) or "./"

def foto(nome, ar="4/5"):
    # sostituire con: <img src="assets/img/NOME" alt="...">
    return f'<figure class="foto" style="--ar:{ar}" data-foto="{nome}"></figure>'

LD_BAKERY = {"@context": "https://schema.org", "@type": "Bakery", "name": "Panetta Bakery", "url": DOMINIO + "/",
             "telephone": "+39 0861 1640185", "email": EMAIL, "hasMenu": DOMINIO + "/asportomenu/", "sameAs": [INSTA],
             "address": {"@type": "PostalAddress", "streetAddress": "Via Nuova 7", "addressLocality": "Colledara",
                         "addressRegion": "TE", "addressCountry": "IT"}}
LD_PANIFICIO = {"@context": "https://schema.org", "@type": "Bakery", "name": "Panificio di Cerchiara",
                "alternateName": "Panificio di Cerchiara di Danilo Panetta", "foundingDate": "1968",
                "url": DOMINIO + "/panificiodicerchiara/", "telephone": "+39 334 8919180", "email": EMAIL,
                "address": {"@type": "PostalAddress", "streetAddress": "Via del Mulino, Cerchiara",
                            "addressLocality": "Isola del Gran Sasso d'Italia", "addressRegion": "TE", "addressCountry": "IT"}}

def pagina(chiave, titolo, desc, sezione, corpo, ld=None, script=""):
    d = PAGINE[chiave].count("/")
    b = "../" * d
    canon = DOMINIO + "/" + PAGINE[chiave]
    nav = [("home", "La Bakery"), ("panificio", "Il Panificio"), ("menu", "Menu asporto")]
    nav_h = "".join('<a href="%s"%s>%s</a>' % (url(k, d), ' aria-current="page"' if k == chiave else "", t) for k, t in nav)
    nav_m = "".join(f'<a href="{url(k, d)}">{t}</a>' for k, t in nav)
    sub = "Panificio di Cerchiara" if sezione == "panificio" else "Bakery · Colledara"
    logo = "logo-panificio" if sezione == "panificio" else "logo-bakery"
    logo_ext = "png" if sezione == "panificio" else "svg"
    alt_logo = "Panetta · Panificio di Cerchiara" if sezione == "panificio" else "Panetta Bakery"
    cur = lambda s: ' aria-current="true"' if sezione == s else ""
    ldj = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ""
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titolo)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Panetta Bakery">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{e(titolo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMINIO}/assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#904B4B">
<link rel="icon" href="{b}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{b}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bree+Serif&family=Merriweather:ital,wght@0,400;0,700;1,400&family=Ultra&display=swap">
<link rel="stylesheet" href="{b}assets/style.css">
<script>var _iub=_iub||[];_iub.csConfiguration={{"siteId":3799849,"cookiePolicyId":91127097,"lang":"it","storage":{{"useSiteId":true}}}};</script>
<script src="https://cs.iubenda.com/autoblocking/3799849.js"></script>
<script src="https://cdn.iubenda.com/cs/iubenda_cs.js" charset="UTF-8" async></script>
{ldj}
</head>
<body>
<a class="sr" href="#contenuto">Vai al contenuto</a>
<header class="header"><div class="wrap" style="position:relative">
  <a class="logo" href="{url('home', d)}"><img src="{b}assets/img/{logo}.{logo_ext}" alt="{alt_logo}" class="logo--{logo}"></a>
  <nav class="nav" aria-label="Principale">{nav_h}<a class="btn btn--sm" href="tel:{TEL_B[1]}">Chiamaci</a></nav>
  <details class="burger"><summary>Menu</summary><nav aria-label="Principale mobile">{nav_m}<a href="#contatti">Contatti</a><a href="tel:{TEL_B[1]}">Chiamaci</a></nav></details>
</div></header>
<div class="fregio" aria-hidden="true"></div>
<main id="contenuto">
{corpo}
</main>
<footer class="footer" id="contatti"><div class="wrap">
  <div class="footer__grid">
    <div class="stack"><div class="footer__loghi"><img src="{b}assets/img/logo-bakery-chiaro.svg" alt="Panetta Bakery"><img src="{b}assets/img/logo-panificio-chiaro.png" alt="Panificio di Cerchiara"></div><p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{INSTA}" target="_blank" rel="noopener">Instagram</a></p></div>
    <div class="stack"><span class="label">Panetta Bakery</span><address>Via Nuova 7<br>Colledara (TE), Abruzzo</address><p><a href="tel:{TEL_B[1]}">{TEL_B[0]}</a></p></div>
    <div class="stack"><span class="label">Panificio di Cerchiara</span><address>Via del Mulino, Cerchiara<br>Isola del Gran Sasso (TE)</address><p><a href="tel:{TEL_P[1]}">{TEL_P[0]}</a></p></div>
  </div>
  <div class="footer__base">
    <span>© Panetta Bakery · Panificio di Cerchiara</span>
    <nav aria-label="Note legali"><a href="{IUB}" target="_blank" rel="noopener">Privacy Policy</a><a href="{IUB}/cookie-policy" target="_blank" rel="noopener">Cookie Policy</a><a href="https://www.iubenda.com/termini-e-condizioni/91127097" target="_blank" rel="noopener">Termini e Condizioni</a></nav>
  </div>
</div></footer>
{script}
<script src="{b}assets/site.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------- BLOCCHI
def nastro(voci, cls=""):
    giro = "".join(f"<span>{e(v)}</span><i>✦</i>" for v in voci)
    return f'<div class="nastro {cls}" aria-hidden="true"><div class="nastro__track">{giro * 4}</div></div>'

def tessere(voci):
    # voci: (titolo, href)
    out = []
    for i, (t, h) in enumerate(voci):
        out.append(f'<a class="tessera rv" style="--i:{i}" href="{h}"><span class="tessera__t">{e(t)}</span><span class="tessera__go" aria-hidden="true">→</span></a>')
    return '<div class="tessere">' + "".join(out) + "</div>"

def galleria(prefisso):
    vel = ["0.10", "0.04", "0.14", "0.07", "0.12"]
    return '<div class="galleria">' + "".join(
        f'<figure class="foto rv" style="--i:{i-1}" data-foto="{prefisso}-{i}.jpg"></figure>' for i in range(1, 6)) + "</div>"

def chi_siamo(titolo, testo, foto_nome, bottoni):
    return f"""
<section class="sez sez--tinta" id="chi-siamo"><div class="wrap chi">
  <div class="chi__titolo rv"><span class="label">Chi siamo</span><h2>{titolo}</h2></div>
  <figure class="foto chi__foto rv" style="--ar:4/5" data-par="0.06" data-foto="{foto_nome}"></figure>
  <div class="chi__testo rv" style="--i:1"><p class="giustificato capolettera">{testo}</p><div class="btns">{bottoni}</div></div>
</div></section>"""

def catering_svg():
    import math
    raggi = []
    for i in range(36):
        a = math.radians(i * 10)
        x1, y1 = 250 + 150 * math.cos(a), 250 + 150 * math.sin(a)
        x2, y2 = 250 + 245 * math.cos(a), 250 + 245 * math.sin(a)
        w = 7 if i % 2 else 3
        raggi.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-width="{w}"/>')
    punti = []
    for i in range(48):
        a = math.radians(i * 7.5)
        punti.append(f'<circle cx="{250 + 138 * math.cos(a):.1f}" cy="{250 + 138 * math.sin(a):.1f}" r="5.2"/>')
    return f"""<svg class="catering__badge" viewBox="0 0 500 500" role="img" aria-label="Catering Panetta Bakery">
  <g class="catering__raggi" stroke="#E8B07F" stroke-linecap="round">{''.join(raggi)}</g>
  <circle cx="250" cy="250" r="128" fill="#904B4B" stroke="#FFF9D6" stroke-width="3"/>
  <g class="catering__punti" fill="#FFF9D6">{''.join(punti)}</g>
  <line x1="150" y1="212" x2="350" y2="212" stroke="#FFF9D6" stroke-width="3"/>
  <line x1="150" y1="292" x2="350" y2="292" stroke="#FFF9D6" stroke-width="3"/>
  <text x="250" y="196" text-anchor="middle" fill="#E8B07F" font-family="Bree Serif, Georgia, serif" font-size="22" letter-spacing="4">PANETTA</text>
  <text x="250" y="265" text-anchor="middle" fill="#FFF9D6" font-family="Ultra, Georgia, serif" font-size="46">Catering</text>
  <text x="250" y="325" text-anchor="middle" fill="#E8B07F" font-family="Bree Serif, Georgia, serif" font-size="20" letter-spacing="4">BAKERY</text>
</svg>"""

def catering(d):
    return f"""
<section class="sez sez--scura catering" id="catering"><div class="wrap catering__grid">
  <div class="catering__arte rv">{catering_svg()}</div>
  <div class="stack-lg rv" style="--i:1">
    <span class="label">Panetta Bakery</span>
    <h2 class="catering__titolo">Catering</h2>
    <p class="lead giustificato catering__testo">Per le tue occasioni portiamo in tavola i prodotti del Panificio di Cerchiara: pizze e fritti, pane, dolci e biscotti della tradizione abruzzese, preparati su richiesta. Raccontaci il tuo evento e costruiamo insieme la proposta giusta.</p>
    <p class="lead">Contattaci per informazioni e preventivi.</p>
    <div class="btns"><a class="btn btn--crema" href="tel:{TEL_B[1]}">Chiama {TEL_B[0]}</a><a class="btn btn--line" href="mailto:{EMAIL}?subject=Catering">Scrivici una mail</a></div>
  </div>
</div></section>
"""

# ---------------------------------------------------------------- HOME (Bakery)
def home():
    d = 0
    m = url('menu', d)
    corpo = f"""
<section class="hero"><div class="wrap hero__grid">
  <div class="stack-lg">
    <span class="label rv">Panetta Bakery · Colledara</span>
    <h1 class="rv" style="--i:1">Eh sì, tante cose buone.</h1>
    <p class="lead rv" style="--i:2">Ma dove le trovo? <strong class="accent">Qua!</strong><br>Via Nuova 7, Colledara (TE), Abruzzo.</p>
    <div class="btns rv" style="--i:3"><a class="tondo" href="tel:{TEL_B[1]}">Chiama!</a><a class="tondo" href="{m}">Menu</a><a class="tondo" href="{INSTA}" target="_blank" rel="noopener">Insta</a></div>
  </div>
  <img class="logo-hero rv" style="--i:2" src="assets/img/logo-bakery.svg" alt="Panetta Bakery">
</div></section>

{nastro(["Pane", "Pasta all'uovo", "Pizze", "Caffetteria", "Primi piatti", "Aperitivi"])}
{chi_siamo("Bakery premium quality",
  "La Bakery nasce come punto vendita del Panificio di Cerchiara, con lo scopo di portare la tradizione ed il sapere a confronto con l'innovazione, in un percorso di qualità e sperimentazione.",
  "home-chi-siamo.jpg",
  f'<a class="btn" href="{m}">Menu asporto</a><a class="btn btn--line" href="{url("panificio", d)}">Il Panificio</a>')}

<section class="sez" id="servizi"><div class="wrap stack-lg">
  <div class="testata rv"><span class="label">Panetta Bakery</span><h2>Servizi</h2></div>
  {tessere([("Consumazione sul posto", "#dove"), ("Asporto", m), ("Pane", m + "#pane"), ("Pasta all'uovo", m + "#pasta"),
            ("Pizze", m + "#pizza"), ("Caffetteria", m + "#caffetteria"), ("Primi piatti", m + "#primi"), ("Aperitivi", m)])}
  {galleria("home-g")}
</div></section>

{nastro(["Eh sì, tante cose buone"], "nastro--vuoto")}
{catering(d)}

<section class="sez" id="dove"><div class="wrap due">
  <div class="stack-lg rv">
    <span class="label">Dove siamo</span>
    <h2>Ma dove le trovo?</h2>
    <dl class="info">
      <dt>Indirizzo</dt><dd>Via Nuova 7, Colledara (TE), Abruzzo</dd>
      <dt>Telefono</dt><dd><a href="tel:{TEL_B[1]}">{TEL_B[0]}</a></dd>
      <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
      <dt>Instagram</dt><dd><a href="{INSTA}" target="_blank" rel="noopener">@panetta_bakery_colledara</a></dd>
    </dl>
    <div class="btns"><a class="btn" href="{MAPS_B}" target="_blank" rel="noopener">Apri in Google Maps</a><a class="btn btn--line" href="tel:{TEL_B[1]}">Chiamaci</a></div>
  </div>
  <figure class="foto rv" style="--ar:4/3;--i:1" data-par="0.05" data-foto="home-dove.jpg"></figure>
</div></section>

<section class="sez sez--tinta"><div class="wrap fascia rv">
  <div class="stack"><span class="label">Il Panificio</span><h2>Panificio di Cerchiara, fornai dal 1968.</h2></div>
  <a class="btn btn--line" href="{url('panificio', d)}">Scopri il Panificio</a>
</div></section>
"""
    return pagina("home", "Panetta Bakery — Colledara (TE)",
                  "Dalla tradizione abruzzese dei prodotti del forno: \"Panificio di Cerchiara.\" La bakery, con consumazione sul posto e asporto, propone la vendita di: pane, pasta all'uovo, pizze, caffetteria, primi piatti e aperitivi.",
                  "bakery", corpo, LD_BAKERY)

# ---------------------------------------------------------------- PANIFICIO
def panificio():
    d = 1
    m = url('menu', d)
    corpo = f"""
<section class="hero"><div class="wrap hero__grid">
  <div class="stack-lg">
    <span class="label rv">Panetta Danilo · Fornai dal 1968</span>
    <h1 class="rv" style="--i:1">Panificio di Cerchiara</h1>
    <p class="lead rv" style="--i:2">Biscotti, pasta all'uovo, dolci &amp; pane.</p>
    <div class="btns rv" style="--i:3"><a class="btn" href="tel:{TEL_P[1]}">Info &amp; ordini</a><a class="btn btn--line" href="{url('home', d)}">Scopri la Bakery</a></div>
  </div>
  <img class="logo-hero logo-hero--panificio rv" style="--i:2" src="../assets/img/logo-panificio.png" alt="Panificio di Cerchiara">
</div></section>

{nastro(["Biscotti", "Pasta all'uovo", "Dolci & pane", "Produzione propria", "Fornai dal 1968"])}
{chi_siamo("Dal 1968",
  "Il panificio di Cerchiara nasce nel 1968 nel paese di Cerchiara dalla famiglia Panetta. Ormai da tre generazioni il panificio tramanda, attraverso i propri prodotti, la tradizione dell'arte fornaia cerchiarese in Abruzzo.",
  "panificio-chi-siamo.jpg",
  f'<a class="btn" href="tel:{TEL_P[1]}">Info &amp; ordini</a><a class="btn btn--line" href="#rivendita">Rivendita</a>')}

<section class="sez"><div class="wrap stack-lg">
  <div class="testata rv"><span class="label">Produzione propria</span><h2>Prodotti tipici della tradizione abruzzese.</h2></div>
  <div class="tessere tessere--3">{tessere([("Pane & panini", m + "#pane"), ("Pasta all'uovo", m + "#pasta"), ("Dolci & torte", m + "#torte")])[len('<div class="tessere">'):-len("</div>")]}</div>
  {galleria("panificio-g")}
</div></section>

{nastro(["Panificio di Cerchiara", "Fornai dal 1968"], "nastro--vuoto")}

<section class="sez sez--tinta" id="rivendita"><div class="wrap fascia rv">
  <div class="stack"><span class="label">Rivendita</span><h2>Hai un'attività e vuoi rivendere i nostri prodotti?</h2></div>
  <a class="btn" href="tel:{TEL_P[1]}">Contattaci · {TEL_P[0]}</a>
</div></section>

<section class="sez"><div class="wrap due">
  <div class="stack-lg rv">
    <span class="label">Info &amp; ordini</span>
    <h2>Panificio di Cerchiara</h2>
    <dl class="info">
      <dt>Indirizzo</dt><dd>Via del Mulino, Cerchiara, Isola del Gran Sasso (TE)</dd>
      <dt>Telefono</dt><dd><a href="tel:{TEL_P[1]}">{TEL_P[0]}</a></dd>
      <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
    </dl>
    <div class="btns"><a class="btn" href="{MAPS_P}" target="_blank" rel="noopener">Apri in Google Maps</a><a class="btn btn--line" href="{url('home', d)}">Scopri il punto vendita</a></div>
  </div>
  <figure class="foto rv" style="--ar:4/3;--i:1" data-par="0.05" data-foto="panificio-info.jpg"></figure>
</div></section>
"""
    return pagina("panificio", "Panificio di Cerchiara di Danilo Panetta",
                  "Produzione e rivendita di pane, pasta all'uovo, pizza, torte e molto altro. Il Panificio di Cerchiara, dal 1968, produce prodotti di qualità, nati dalla tradizione abruzzese.",
                  "panificio", corpo, LD_PANIFICIO)

# ---------------------------------------------------------------- MENU
def li_voce(v):
    nome, prezzo, unita, nota = v
    n = f'<span class="nota">{e(nota)}</span>' if nota else ""
    u = f' <span class="unita">{e(unita)}</span>' if unita else ""
    return f'<li><span>{e(nome)}{n}</span><span class="prezzo">{prezzo} €{u}</span></li>'

def menu():
    d = 1
    cats = []
    for c in MENU:
        s = [f'<section class="cat" id="{c["id"]}"><h2>{e(c["titolo"])}</h2>']
        for sub, vv in c["gruppi"]:
            if sub: s.append(f'<p class="sub">{e(sub)}</p>')
            s.append('<ul class="listino">' + "".join(li_voce(v) for v in vv) + "</ul>")
        if c["id"] == "primi":
            s.append('<p class="nota-cat"><strong>Piatto del giorno</strong> — Lasciati proporre i nostri piatti del giorno. Mai uguali, mai gli stessi!</p>')
        s.append("</section>")
        cats.append("".join(s))
    anc = "".join(f'<a href="#{c["id"]}">{e(c["titolo"])}</a>' for c in MENU)
    corpo = f"""
<div class="wrap menu-top">
  <span class="label">Panetta Bakery · Colledara</span>
  <h1>Menu</h1>
  <p class="lead">Asporto: ordina al <a href="tel:{TEL_B[1]}">{TEL_B[0]}</a>.</p>
</div>
<nav class="menu-nav" aria-label="Categorie"><div class="wrap">{anc}</div></nav>
<div class="wrap menu-corpo">
  <div class="stack-lg">{''.join(cats[:4])}</div>
  <div class="stack-lg">{''.join(cats[4:])}</div>
</div>
<section class="sez sez--tinta"><div class="wrap fascia">
  <h2>Ordina qui.</h2>
  <div class="btns"><a class="btn" href="tel:{TEL_B[1]}">Chiama {TEL_B[0]}</a><a class="btn btn--line" href="{url('home', d)}">Torna al sito</a></div>
</div></section>
"""
    return pagina("menu", "Menu Panetta Bakery", "Menu Panetta Bakery, Colledara: pane, pasta fresca all'uovo, pizza e fritti, primi piatti, torte, biscotteria, cornetti e caffetteria.",
                  "bakery", corpo, LD_BAKERY)

# ---------------------------------------------------------------- REDIRECT
def redirect(dest):
    return f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Panetta</title><link rel="canonical" href="{DOMINIO}/{dest}"><meta http-equiv="refresh" content="0; url=../{dest}"></head><body><a href="../{dest}">Panetta</a></body></html>'

# ---------------------------------------------------------------- FOTO
# spazio foto -> (file in assets/img/foto/, testo alternativo)
FOTO = {
    "home-chi-siamo.jpg": ("bakery-primo.jpg", "Un primo piatto della Panetta Bakery"),
    "home-dove.jpg": ("bakery-interno.jpg", "La sala e il bancone della Panetta Bakery a Colledara"),
    "home-g-1.jpg": ("bakery-cupcake.jpg", "Cupcake della Panetta Bakery"),
    "home-g-2.jpg": ("bakery-crostata.jpg", "Crostata al pistacchio"),
    "home-g-3.jpg": ("bakery-pizza-calzone.jpg", "Pizza margherita e calzone fritto"),
    "home-g-4.jpg": ("bakery-biscotti.jpg", "Biscotti, cantucci e dolci da forno"),
    "home-g-5.jpg": ("bakery-lasagna.jpg", "Lasagna al forno"),
    "panificio-chi-siamo.jpg": ("panificio-pane-telo.jpg", "Pagnotta avvolta in un telo di lino accanto al fuoco"),
    "panificio-g-1.jpg": ("panificio-pane-spezzato.jpg", "Mani che spezzano una pagnotta appena sfornata"),
    "panificio-g-2.jpg": ("panificio-panini.jpg", "Panini su un telo da cucina"),
    "panificio-g-3.jpg": ("panificio-pizza-forno.jpg", "Pizza nel forno a legna"),
    "panificio-g-4.jpg": ("panificio-ciambellone.jpg", "Ciambellone tagliato su un piatto"),
    "panificio-g-5.jpg": ("panificio-cesto-pane.jpg", "Pane in un cesto di vimini"),
    "panificio-info.jpg": ("panificio-impasto.jpg", "Mani che lavorano l'impasto sul banco infarinato"),
}

def metti_foto(html_txt, depth):
    import re
    def sost(m):
        slot = m.group(2)
        if slot not in FOTO: return m.group(0)
        f, alt = FOTO[slot]
        return f'{m.group(1)} data-foto="{slot}"><img src="{"../" * depth}assets/img/foto/{f}" alt="{e(alt)}" loading="lazy" decoding="async"></figure>'
    return re.sub(r'(<figure class="foto[^"]*"[^>]*?) data-foto="([^"]+)"></figure>', sost, html_txt)

def build(out):
    def w(rel, txt):
        if rel.endswith(".html"): txt = metti_foto(txt, rel.count("/"))
        p = os.path.join(out, rel); os.makedirs(os.path.dirname(p) or out, exist_ok=True)
        open(p, "w", encoding="utf-8").write(txt)
    w("index.html", home()); w("panificiodicerchiara/index.html", panificio())
    w("asportomenu/index.html", menu())
    w("about/index.html", redirect("#chi-siamo"))
    for old in ("scoprici", "panettabakerycolledara", "bakery"):
        w(f"{old}/index.html", redirect(""))
    w("404.html", '<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Pagina non trovata — Panetta</title><meta http-equiv="refresh" content="3; url=/"></head><body style="font-family:sans-serif;padding:2rem"><p>Pagina non trovata. <a href="/">Torna al sito</a></p></body></html>')
    w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMINIO}/sitemap.xml\n")
    w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"  <url><loc>{DOMINIO}/{p}</loc></url>\n" for p in PAGINE.values()) + "</urlset>\n")
    if out != SRC:
        shutil.copytree(os.path.join(SRC, "assets"), os.path.join(out, "assets"), dirs_exist_ok=True)

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--preview":
        PREVIEW = True; build(sys.argv[2])
    else:
        build(SRC)
    print("ok")
