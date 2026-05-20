### 氛圍編程（Vibe Coding）

Vibe Coding 不是「把需求丟給 AI 然後等代碼出現」。更準確地說，它是一種人和 AI Coding Agent 共同迭代軟件的工作方式：人負責方向、約束和驗收，Agent 負責生成、修改、搜索和執行一部分工程動作。

#### 為什麼要學這個

AI Coding Agent 已經能讀代碼、改文件、跑測試、解釋錯誤、生成 PR。對 builder 來說，這會明顯改變開發速度。但速度變快之後，真正的問題變成：你能不能清楚描述任務，能不能審查結果，能不能控制改動範圍，能不能驗證沒有引入新 bug。

Vibe Coding 最容易被誤解成「憑感覺寫代碼」。實際可用的做法正好相反：你要更清楚地管理 repo、任務、上下文、測試和提交邊界。

AI 能幫你寫更多代碼，但不能替你承擔工程判斷。

#### 第一性原理

AI Coding 的核心不是自動生成代碼，而是把工程反饋循環壓短。
過去你需要自己搜索文件、理解模塊、改代碼、跑測試、看錯誤、再修改。現在 Agent 可以並行承擔很多步驟。但如果反饋循環裡沒有測試、審查和版本控制，速度只會放大混亂。

任務要小：越具體、越有邊界，Agent 越容易產出可審查結果。
上下文要準：讓 Agent 看對文件、設計約束和錯誤輸出，比寫長篇需求更重要。
驗證要硬：運行測試、類型檢查、構建、截圖或日誌，比「看起來對」可靠。

#### 知識節點

**Vibe Coding**

難度：初級。先理解人和 AI Coding Agent 怎麼分工：人負責目標、邊界和驗收，Agent 負責搜索、生成、修改和執行。

Vibe Coding 是一種快速和 AI 共同探索代碼的方式。你可以先描述目標，讓 Agent 生成方案或 patch，再通過運行、檢查、追問和迭代收斂。

它適合：

* 搭原型
* 修小 bug
* 補測試
* 寫腳本
* 重構局部模塊
* 解釋陌生代碼

它不適合無邊界地「重寫整個項目」。如果任務範圍太大，Agent 很容易改到不該改的地方，或者引入看似合理但不符合項目約束的抽象。

**Claude Code / Codex CLI**

難度：初級。重點不是背命令，而是學會把 AI Agent 安全地接入本地 repo、終端和測試流程。

Claude Code、Codex CLI 這類工具把 AI Agent 放進本地開發環境，讓它可以讀文件、編輯文件、運行命令、理解測試輸出。

這類工具的關鍵價值不是「聊天」，而是能在 repo 裡行動。也正因為它能行動，你需要明確：

* 哪些文件可以改
* 哪些命令可以跑
* 是否允許安裝依賴
* 是否允許訪問網絡
* 什麼時候必須停下來讓人確認

**相關 topic**

```Claude Code Docs```：了解 Claude Code 的本地開發工作流。

```Model / API Config```

難度：中級。這一層要處理模型選擇、API key、工具權限、上下文、成本和日誌，不只是「能不能調用成功」。

AI Coding 不是只看「哪個模型最強」。你還要管理模型、API key、上下文窗口、工具權限、代理設置、成本和日誌。

常見問題包括：

* 本地和 CI 用的模型不一致
* API key 洩漏到日誌或提交裡
* 上下文太長導致成本失控
* Agent 使用了不合適的工具權限
* 輸出風格和項目規範不一致

好的配置應該能被團隊復用，而不是每個人在本機隨手調。

OpenCLI 是這一層可以關注的工具之一。它把網站、瀏覽器會話、Electron 應用和本地二進制工具統一成可被命令行調用的接口，讓 AI Agent 可以通過更穩定的命令去發現、學習和執行工具，而不是每次都臨時操作頁面。它還可以復用本地瀏覽器登錄態，並把 gh、docker 等本地 CLI 暴露到同一個工具入口裡。

這類工具的價值不在於「又多一個 AI 編程產品」，而在於把 Agent 可調用的外部能力變得更清楚：有哪些命令、需要什麼權限、輸出格式是什麼、失敗時怎麼診斷。

```GitHub / gh```

難度：中級。你需要把 AI 生成的改動放回版本控制、issue、PR 和 review 流程裡，而不是只看一次聊天輸出。

GitHub 和 gh CLI 是 AI Coding 工作流裡的協作邊界。Agent 可以幫你看 issue、生成 branch、讀 PR diff、寫提交信息、整理 review，但版本控制仍然是人類審查的關鍵線。

一個實用原則：讓 Agent 多做局部 patch，少做不可追蹤的大改動。

每次改動後至少看：

* git diff
* 修改文件列表
* 測試結果
* 是否包含不該提交的密鑰、日誌、構建產物

```CLI / Script```

難度：中級。這一層開始把 Agent 輸出變成真實命令和腳本，所以要特別關注讀寫範圍、dry run 和外部副作用。

很多開發任務不需要完整應用界面，先寫 CLI 或腳本更快。Agent 很適合幫你生成一次性腳本、數據遷移腳本、檢查腳本和批量修改腳本。

但腳本有兩個邊界：

* 讀寫文件前要確認範圍。
* 會修改外部狀態的腳本要先 dry run。

如果腳本會刪文件、發請求、改數據庫、提交交易或調用生產 API，就不能只靠 Agent 判斷。

```Repo Workflow```

難度：高級。你要把 AI Coding 接進完整工程流程，並能判斷什麼時候應該讓 Agent 繼續，什麼時候必須由人停下來審查。

Repo Workflow 是把 AI Coding 放進正常工程流程：issue、branch、commit、test、review、merge、release。

不要讓 AI 繞過這些流程。更好的方式是讓它參與這些流程：

* 從 issue 提煉任務邊界
* 搜索相關文件
* 生成最小 patch
* 跑測試並解釋失敗
* 補充 changelog 或文檔
* 寫 PR summary 和驗證說明

AI Coding 的質量，最終還是要落到 repo workflow 裡。

#### 在 AI x Web3 中的位置

AI x Web3 項目通常同時有前端、合約、腳本、索引器、Agent 後端和文檔。Vibe Coding 可以顯著加快探索速度，尤其適合 hackathon 和早期原型。

但鏈上相關代碼的風險更高。合約、簽名、權限、支付、遷移腳本不能只靠 Agent 生成後直接上線。AI Coding 可以幫你寫測試、解釋 ABI、生成腳本，但高風險動作必須經過審查、模擬和多方確認。

#### 最小實踐

選擇一個小功能，讓 AI Coding Agent 完成一輪完整工程閉環：

* 寫清楚任務邊界和不能改的文件。
* 讓 Agent 搜索相關代碼並給出計劃。
* 讓 Agent 做最小 patch。
* 運行測試或構建。
* 查看 git diff，手動審查結果。
* 要求 Agent 寫一段 PR summary 和驗證說明。

完成後記錄：哪些信息給少了，哪些測試缺失，哪些改動需要人類判斷。

**挑戰**

在自己的電腦上安裝並配置至少一個 Vibe Coding 工具，例如 Claude Code、Codex CLI 或 OpenCLI，並確認它能在一個測試 repo 中正常使用。

完成標準：

* 能啟動工具並讀取當前項目。
* 已配置必要的模型、API key、瀏覽器橋接或本地工具權限。
* 能讓工具完成一個只讀任務，例如解釋目錄結構、搜索相關文件或總結某段代碼。
* 能讓工具完成一個低風險小改動，例如補一段注釋、生成一個腳本或修改一處測試。
* 保留驗證記錄：工具版本、配置方式、執行命令、關鍵輸出或截圖。

#### 擴展閱讀
[Claude Code Overview](https://docs.anthropic.com/en/docs/claude-code/overview)：了解 Claude Code 如何進入本地開發流程。
[Claude Code CLI Reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)：查看常用命令和參數。
[OpenAI Codex CLI Getting Started](https://github.com/openai/codex)：了解 Codex CLI 的基礎使用方式。
[GitHub CLI Manual](https://cli.github.com/manual/)：學習用 gh 管理 issue、PR、repo 和 CI 狀態。
[OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents)：理解 AI Agent 進入工具工作流時的 guardrails 和 tracing。
