# GunplaBase MG 改善版本說明

## 已實作的改善（直接可用）

1. **語言標記修正**
   - `<html lang="en">` → `<html lang="zh-Hant">`
   - 對螢幕閱讀器、搜尋引擎、翻譯工具更正確

2. **SEO 與社群分享優化**
   - 加入 `meta description`
   - 加入 Open Graph (`og:title`, `og:description`, `og:url`, `og:locale`)
   - 加入 Twitter Card
   - 加入 `theme-color`（手機瀏覽器地址列顏色）
   - 加入 Apple mobile web app meta（方便「加入主畫面」）

## 如何使用

1. 下載 `index.html`（本倉庫）
2. 或直接啟用 GitHub Pages 指向 main branch
3. 等待更新後訪問 https://csfclayton.github.io/gunpla-improve/

## 仍需原始碼才能完善的部分

目前 repo 只有打包後的單一 `index.html`（約 480KB 的 minified React），以下功能需要原始 React 專案才能優雅實作：

### 高優先
- **虛擬列表 (Virtual List)**：用 `react-window` 或 `@tanstack/react-virtual`，大幅改善 226 張卡片的滾動效能
- **更完整的匯出/匯入**：雖然已有 CSV 匯出，可再加強 JSON 完整備份（包含評分、標籤、狀態）
- **無障礙 (a11y)**：為大量按鈕補上 `aria-label`，改善鍵盤導航

### 中優先
- 完整 PWA（manifest.json + icons）
- 統計頁面圖表強化
- 自訂模型更好的 UI

## 建議作者

如果作者有原始 Vite + React 專案，建議：
1. 把這個改善的 meta / lang 合回去
2. 加入虛擬列表
3. 考慮開源原始碼，方便社群一起改善
