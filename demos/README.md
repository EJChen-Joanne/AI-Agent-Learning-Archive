## Learning Bot 設定說明

`demos/learning_bot.py` 是一個 Telegram Bot，由 Claude Haiku 驅動，每日透過指令推送學習重點、目標與知識測驗。

### 指令

| 指令 | 功能 |
|------|------|
| `/notes` | 根據今日學習規劃，從課綱中隨機抽取片段，生成當日三大學習重點 |
| `/goal` | 讀取 `week1.md` 今日段落，生成具體學習目標與完成標準 |
| `/test` | 從 `terms.json` 隨機抽取 5 題選擇題（優先選近 7 天未出現的術語） |

### 環境變數

在 `demos/.env` 中設定以下三個變數：

```env
CLAUDE_API_KEY=sk-ant-...
TELEGRAM_TOKEN=...
CHAT_ID=...
```

取得方式：
- `CLAUDE_API_KEY`：[Anthropic Console](https://console.anthropic.com/) → API Keys
- `TELEGRAM_TOKEN`：在 Telegram 向 [@BotFather](https://t.me/BotFather) 發送 `/newbot` 取得
- `CHAT_ID`：啟動 Bot 後向 [@userinfobot](https://t.me/userinfobot) 取得你的 chat ID

### 安裝與啟動

```bash
cd demos
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install anthropic python-dotenv requests
python learning_bot.py
```

Bot 啟動後以長輪詢（long polling）方式監聽，保持終端運行即可接收指令。

### 架構說明

```
Telegram 使用者
      │ /notes / /goal / /test
      ▼
learning_bot.py（長輪詢監聽）
      │
      ├─ /notes → sample_sections() 隨機抽取課綱片段
      │         → get_today_plan() 讀取今日規劃
      │         → ask_claude() 生成學習重點
      │
      ├─ /goal  → get_today_plan() 讀取今日規劃
      │         → ask_claude() 生成目標清單
      │
      └─ /test  → load_terms() 讀取 terms.json
                → pick_daily_terms() 避開近期出題紀錄
                → build_question() 生成四選一題目
                → handle_quiz_answer() 計分與即時回饋
```

資料流：`curriculums/` 目錄 → Bot → Claude Haiku API → Telegram

*最後更新：2026-05-20*