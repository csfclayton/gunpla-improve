# GunplaBase MG (Improved)

Improved version of [csfclayton/gunpla](https://csfclayton.github.io/gunpla/).

## Changes already applied in the patch

- `lang="zh-Hant"` (was `en`)
- Added `meta description`
- Added Open Graph tags (`og:title`, `og:description`, `og:type`, `og:url`, `og:locale`)
- Added Twitter Card tags
- Added `theme-color` and Apple mobile web-app meta tags

## How to use the full improved page

The full `index.html` is ~480 KB (minified React app). Because of API size limits it cannot be pushed in one go from this tool.

**Easiest way (recommended):**

1. Open the original file: https://raw.githubusercontent.com/csfclayton/gunpla/main/index.html
2. Follow the exact instructions in [PATCH.md](./PATCH.md) — you only need to replace the first ~15 lines of the `<head>`.
3. Save as `index.html` and push to this repo (or to your main gunpla repo).
4. Enable **GitHub Pages** (Settings → Pages → Deploy from branch `main` / root).

After that the site will be live at:
https://csfclayton.github.io/gunpla-improve/

## Files in this repo

- `README.md` — this file
- `IMPROVEMENTS.md` — detailed improvement notes
- `PATCH.md` — exact copy-paste patch for the head section

## Next possible improvements (need source code)

Virtual list for performance, better a11y, full JSON backup, complete PWA, etc. See IMPROVEMENTS.md.
