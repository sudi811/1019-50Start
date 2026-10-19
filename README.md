# 50 Startups Regression Explorer 🚀

> 中興大學 人工智慧與資安 (L07 50 Startup LR)  
> 線性迴歸特徵探索、模型評估與新創獲利即時預測互動式 Web 平台

🔗 **GitHub Pages 線上展示網址**：[https://sudi811.github.io/1019-50Start/](https://sudi811.github.io/1019-50Start/)

---

## 📌 專案特色

* **探索 1 ~ 5 個特徵對於獲利的影響**：
  * **逐步選取 (Stepwise)**：重現課堂實作之特徵加入順序，對比 RMSE 與 $R^2$。
  * **5-Fold CV 最佳組合 (Exhaustive)**：窮舉所有組合，以交叉驗證誤差挑選最佳自變數集合。
* **支援多種迴歸演算法**：
  * Linear Regression (多元線性迴歸)
  * Ridge (L2 正則化)
  * Lasso (L1 正則化)
* **互動式新創公司獲利即時模擬計算機 (Live Simulator)**：
  * 可自由調整「研發支出 (R&D Spend)」、「行政管理支出 (Administration)」、「行銷經費 (Marketing Spend)」與「註冊州別 (State)」，即時套用迴歸方程式推估淨利。
* **全前端無伺服器架構**：採用純 HTML5 / CSS3 / JavaScript + Chart.js，可直接在 GitHub Pages 免費靜態託管。

---

## 📂 專案檔案結構

* `index.html`：互動式 Web 儀表板入口頁面
* `style.css`：現代化響應式 UI 樣式表
* `app.js`：前端互動邏輯、Chart.js 圖表渲染、即時獲利預測計算
* `main.py`：Python 機器學習實驗腳本 (Scikit-Learn + Matplotlib)
* `experiment_result.png`：Python 產出之特徵數量與 RMSE / R² 評估折線圖
* `data.json`：50 Startups 原始資料與預先計算之模型統計資料

---

## 💻 本地執行方式

### 1. 執行 Python 模型實驗
```bash
python main.py
```

### 2. 開啟互動式網頁
直接在瀏覽器雙擊開啟 `index.html`，或使用 Python 簡易伺服器：
```bash
python -m http.server 8080
```
並在瀏覽器造訪 `http://localhost:8080`。

---

## 🌐 GitHub Pages 啟用步驟

1. 進入本儲存庫 GitHub 頁面：[https://github.com/sudi811/1019-50Start](https://github.com/sudi811/1019-50Start)
2. 點擊頂部的 **Settings**（設定）
3. 在左側選單點選 **Pages**
4. 在 **Build and deployment** > **Branch** 下拉選單選擇：
   * 分支：`main`
   * 目錄：`/(root)`
5. 點擊 **Save**，等待 1~2 分鐘即可透過 [https://sudi811.github.io/1019-50Start/](https://sudi811.github.io/1019-50Start/) 瀏覽！