# Java Reference — hosted, offline-capable

A Progressive Web App (PWA) version of the course reference. Lives at a GitHub Pages
URL, updates live when you push, and works offline once loaded.

## Files
- `index.html` — the reference page (PWA-enabled)
- `manifest.webmanifest` — home-screen icon + app metadata
- `sw.js` — service worker (network-first: latest when online, cached copy when offline)
- `icon-192.png`, `icon-512.png`, `icon-maskable-512.png` — home-screen icons
- `reference-source.json` — canonical content source (kept here for regeneration)
- `java-reference.html` — the plain (non-PWA) build, input to rebuild.py
- `java-reference.pdf` — print edition
- `rebuild.py` — re-stamps the cache version and re-injects PWA tags after a content update

## One-time setup
1. Create a GitHub repo (e.g. `java-reference`). It can be **public** (Pages is free for public repos).
2. Upload every file in this folder to the repo root (drag-and-drop in GitHub's web UI works,
   even from your phone's browser).
3. Repo → **Settings → Pages** → Source: *Deploy from a branch* → Branch: `main`, folder: `/ (root)` → Save.
4. Wait ~1 minute. Your page is live at:  `https://<username>.github.io/<repo>/`

## Add to Android home screen
1. Open that URL in **Chrome** on your phone.
2. Menu (⋮) → **Add to Home screen** → Add.
3. It installs with the icon and opens full-screen, like an app.

## Updating (live propagation)
When the reference is regenerated:
1. Drop the new `reference-source.json` and `java-reference.html` into this folder.
2. Run `python3 rebuild.py` (re-injects PWA tags, bumps the cache version).
3. Commit and push (or re-upload `index.html`, `sw.js`, `reference-source.json` via GitHub web).
4. Next time you open the icon **while online**, the new version loads and re-caches automatically.
   Offline, you keep the last version until you're online again.

No server to run. No manual copy to the phone. Push once, the phone catches up on next open.
