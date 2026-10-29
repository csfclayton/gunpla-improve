#!/usr/bin/env python3
"""Download original GunplaBase MG index.html and apply SEO/lang improvements."""
import urllib.request

URL = "https://raw.githubusercontent.com/csfclayton/gunpla/main/index.html"

with urllib.request.urlopen(URL) as resp:
    content = resp.read().decode("utf-8")

content = content.replace('<html lang="en">', '<html lang="zh-Hant">')

meta = """    <meta name="description" content="GunplaBase MG — 高達模型 MG 收藏管理大師。建立山積清單、標記已完成神作，快速探索 Ver.Ka、各年代經典高達模型。支援離線使用、多貨幣、批量標籤。" />
    <meta name="theme-color" content="#0a0f1a" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta property="og:title" content="GunplaBase MG — 高達模型收藏管理大師" />
    <meta property="og:description" content="高達模型 MG 收藏管理工具。建立山積清單、標記已完成，支援離線與多貨幣。" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://csfclayton.github.io/gunpla-improve/" />
    <meta property="og:locale" content="zh_HK" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content="GunplaBase MG — 高達模型收藏管理大師" />
    <meta name="twitter:description" content="高達模型 MG 收藏管理工具。建立山積清單、標記已完成，支援離線與多貨幣。" />
"""

needle = '<meta name="viewport" content="width=device-width, initial-scale=1.0" />'
content = content.replace(needle, needle + "\n" + meta)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Patched index.html written, size:", len(content))
