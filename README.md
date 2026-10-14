# Panetta — sito statico

Pagine: `index.html` · `panificio.html` · `bakery.html` · `menu.html`
Vecchi URL Readymag (`/about/`, `/asportomenu/`, `/panificiodicerchiara/`, `/scoprici/`) → redirect alle nuove pagine.

## Modificare testi / prezzi
Tutto è in `_build.py` (menu, telefoni, indirizzi). Dopo le modifiche:
```
python3 _build.py
```

## Foto e loghi
Mettere i file in `assets/img/`. Ogni segnaposto nell'HTML ha un commento `<!-- FOTO: assets/img/nome.jpg -->`.
Da aggiungere anche: `assets/img/favicon.png`, `assets/img/og.jpg` (1200×630).

## Da completare
- Orari Bakery e Panificio
- P.IVA nel footer
- Logo (header: blocco `marchio`)

## Pubblicazione (GitHub Pages)
Repo → Settings → Pages → Deploy from branch `main` / root.
Dominio: aggiungere un file `CNAME` con `panettabakery.com` e aggiornare i DNS.
