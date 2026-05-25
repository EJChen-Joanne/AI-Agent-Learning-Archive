# Week 1 個人學習計畫
> AIxWeb3 School｜2026-05-18（週一）～ 2026-05-24（週日）

---

## 本週學習目標

| # | 目標 |
|---|------|
| 1 | 理解 LLM、prompt、workflow、agent、tool use、AI coding 的基本概念 |
| 2 | 理解帳戶、錢包、簽名、交易、Gas、合約、測試網和區塊瀏覽器如何構成鏈上操作鏈 |
| 3 | 完成至少一次 AI 工具實踐、一次測試網互動，以及一個 AI × Web3 最小交叉實驗 |
| 4 | 建立權限、安全、人工確認、日誌、驗證材料和失敗恢復意識 |
| 5 | 為 Week 2 的支付、身份、權限、安全隱私、治理協作等方向建立共同語言 |

---

## 每日學習計畫（自習 3–5 hr + 晚間線上課）

> **學習策略（個人化調整）**
> AI / Agent 為本週主攻方向，前兩天深入紮根；Web3 採「系統性快速掃描」策略，確保概念完整不留空白，但不在工具細節上花過多時間；週四以「AI 主導 × Web3 執行」的交叉實驗串聯兩條線，週五做全面複習與交付。

---

### 週一 5/18｜AI 基礎深耕 — LLM 原理與 API 動手（4 hr）

> 重點：把 LLM 的工作方式、四個控制層面、token/context 機制真正弄懂，而不是快速略讀。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 深讀 | [What is a Large Language Model?](https://www.youtube.com/watch?v=zjkBMFhNj_g)（影片，邊看邊暫停做筆記） | 45 min |
| 深讀 | [Hugging Face LLM Course Chapter 1](https://huggingface.co/learn/llm-course/chapter1/1)（仔細閱讀，不要跳過） | 60 min |
| 實作 | 選定平台（優先 Claude / Z.ai），取得 API Key，跑通第一個請求；嘗試修改 temperature、max_tokens 觀察輸出差異 | 60 min |
| 閱讀 | [Anthropic: Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)（重點看 Messages API、System Prompt、Tool Use 三節） | 35 min |

**今日產出**：API 請求截圖 + 筆記：LLM 工作方式、四個控制層面、token 是什麼、context window 限制

---

### 週二 5/19｜Agent 深潛 — 從概念到框架到動手（5 hr）

> 重點：真正理解 Prompt / Workflow / Agent 的差異，並親手設定一個能持續用的 Learning Agent。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 深讀 | AI Agent 入門影片（至課程平台確認連結；邊看邊暫停，記下每個 agent 組件的作用） | 45 min |
| 深讀 | [Microsoft《AI Agents for Beginners》](https://github.com/microsoft/ai-agents-for-beginners) 前三章（含程式碼範例，至少跑一個 notebook） | 75 min |
| 深讀 | [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) — 重點閱讀：Agent、Tool Calling、Handoff、Guardrails 四個核心概念 | 30 min |
| 深讀 | [LangGraph Overview](https://langchain-ai.github.io/langgraph/) + [Hermes Agent Docs](https://hermes-agent.nousresearch.com/docs/)（各快速瀏覽架構，理解 state graph 與 skills 的概念） | 30 min |
| 實作 | 安裝 [Claude Code](https://anthropic.skilljar.com/claude-code-101)（或 Codex CLI / Hermes），完成設定；**搭建 Learning Agent**：把 Week 1 大綱交給 agent，讓它生成學習計畫、概念解釋、Q&A 清單 | 60 min |
| 實作 | 創建個人 GitHub Repo，建立 README、notes/、prompts/、demos/、logs/、resources.md；記錄 agent 設定說明與一次完整對話日誌 | 30 min |

**今日產出**：Agent 概念筆記（Prompt vs Workflow vs Agent 差異）+ Learning Agent 設定記錄 + GitHub Repo 初始化 commit

---

### 週三 5/20｜Web3 系統性速覽 — 概念完整，實作精簡（3 hr）

> 策略：用「讀完即能說清楚」的標準覆蓋所有核心概念，測試網操作一次性完成，不在工具細節上反覆糾結。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 速讀 | [Ethereum Accounts](https://ethereum.org/en/developers/docs/accounts/) + [MetaMask Getting Started](https://support.metamask.io/getting-started/)（重點：帳戶 = 私鑰衍生、錢包 = 私鑰管理入口） | 40 min |
| 速讀 | Web3 運行原理（課程補充材料；提煉：帳戶 → 簽名 → 交易 → Gas → 合約執行 → 狀態更新的完整鏈） | 35 min |
| 實作 | 創建測試錢包 → 切換 Sepolia → [Faucet](https://faucets.chain.link/sepolia) 領幣 → 發送測試交易 → [區塊瀏覽器](https://sepolia.etherscan.io/)記錄哈希、狀態、Gas（一氣呵成） | 50 min |
| 整理 | 用自己的話寫下三條「安全邊界」筆記：地址 ≠ 匿名、簽名 ≠ 普通登入、授權 ≠ 轉帳 | 15 min |

**今日產出**：測試交易哈希 + 區塊瀏覽器截圖 + 安全邊界筆記（三條清楚說得出口）

---

### 週四 5/21｜AI × Web3 交叉實驗 — 用 Agent 驅動合約部署（5 hr）

> 重點：讓 AI Agent 在整條鏈路中扮演「生成 + 解釋」的角色，人來負責「複核 + 執行 + 驗證」，體驗兩者分工的感覺。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 實作 | 讓 Claude Code / Learning Agent **生成一份最小 SimpleStorage 合約說明與部署步驟**；人工仔細閱讀並標記：哪些說法可靠、哪些需要外部驗證 | 45 min |
| 實作 | 用 [Remix IDE](https://remix.ethereum.org/) 實際部署合約，完成一次讀取 + 一次寫入；儲存合約地址與交易哈希 | 75 min |
| 整理 | 畫出「AI 生成 → 人工複核 → 錢包確認 → 鏈上執行 → 區塊瀏覽器驗證」流程圖（放入 repo demos/） | 30 min |
| 深讀 | [OpenZeppelin Contracts 概覽](https://docs.openzeppelin.com/contracts)（快速掃：ERC20/721 是什麼、為什麼要用標準合約） | 25 min |
| 速讀 | [Safe Overview](https://docs.safe.global/) + [ERC-4337](https://docs.erc4337.io/)（各花 10 分鐘，理解「智能帳戶對 AI Agent 有什麼意義」） | 20 min |
| 整理 | 用 agent 生成一個可互動學習產物（quiz / 概念卡片 / CLI demo），放入 repo demos/；README 標注 AI 生成了什麼、人工修改了什麼 | 50 min |

**今日產出**：合約地址 + 交易哈希 + 交叉實驗流程圖 + 可互動學習產物

---

### 週五 5/22｜系統複習 + 全週交付（3 hr）

> 策略：用 Q&A 清單自我檢測本週理解程度；補弱點、整理交付、建立行業觀察習慣。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 複習 | 翻閱本週所有筆記，對照 Q&A 清單逐題自答；標出仍不清楚的題目，用 agent 追問補強 | 45 min |
| 整理 | 把 LLM → workflow → agent → 錢包 → 簽名 → 交易 → 合約串成一段連貫的文字說明（放入 notes/） | 30 min |
| 整理 | 更新 GitHub Repo README（含 agent 設定說明、learning log、proof of work 截圖） | 20 min |
| 整理 | 完成行業觀察清單初稿：選 3–5 條高品質 AI × Web3 內容，每條寫一段觀察筆記 + 建立個人 Follow List | 45 min |

**今日產出**：完整 Week 1 交付物 + Q&A 自答記錄 + GitHub Repo 最終 commit

---

## 待完成 Checklist

### Module A｜AI 基礎

- [ ] 觀看 What is a Large Language Model?（影片）
- [ ] 閱讀 Hugging Face LLM Course Chapter 1
- [ ] 觀看 LLM API 調用入門（影片）
- [ ] 閱讀 Anthropic: Building with the Claude API
- [ ] 選定 API 平台（Claude / OpenAI / Z.ai），取得 API Key
- [ ] 跑通第一個 LLM API 請求（含截圖）
- [ ] 閱讀 AI Agent 入門（影片）
- [ ] 閱讀 Microsoft《AI Agents for Beginners》前兩章
- [ ] 閱讀 OpenAI Agents SDK Intro
- [ ] 閱讀 LangGraph Overview（概覽）
- [ ] 閱讀 Hermes Agent Docs（概覽）
- [ ] 閱讀 Claude Code 101
- [ ] 安裝並設定 Learning Agent 工具（Claude Code / Codex / Hermes）
- [ ] 完成至少一次對話式學習任務（用 agent 整理 Week 1 大綱）

### Module B｜Web3 基礎

- [ ] 閱讀 Ethereum Accounts 文件
- [ ] 閱讀 MetaMask Getting Started
- [ ] 閱讀 Web3 運行原理（補充材料）
- [ ] 閱讀 Ethereum Development Documentation（快速瀏覽架構）
- [ ] 創建測試錢包，能說明地址、助記詞、私鑰的區別與安全責任
- [ ] 切換至 Sepolia 測試網
- [ ] 領取測試幣（Sepolia Faucet）
- [ ] 發送一筆測試交易
- [ ] 至區塊瀏覽器記錄：交易哈希、狀態、Gas、區塊高度
- [ ] 在 Remix IDE 部署最小智能合約
- [ ] 完成一次合約讀取操作
- [ ] 完成一次合約寫入操作
- [ ] 保存合約地址、交易哈希與區塊瀏覽器連結

### Module C｜最小交叉實驗

- [ ] 選定一條鏈路（AI coding → 合約部署 / agent workflow → 錢包確認）
- [ ] 讓 AI 生成合約互動說明或腳本
- [ ] 人工複核 AI 輸出，標記不可靠部分
- [ ] 在測試網執行
- [ ] 在區塊瀏覽器驗證結果
- [ ] 畫出完整流程圖（AI 生成 → 人工複核 → 錢包確認 → 鏈上執行 → 驗證）

### GitHub Repo 與交付物

- [x] 創建個人 GitHub Repo（含 README、notes/、prompts/、demos/、logs/、resources.md）
- [ ] 提交 Learning Agent 設定記錄與 API 路徑說明
- [ ] 提交至少一次 agent 協助學習或編碼的日誌
- [x] 提交可互動學習產物到 demos/（quiz / 流程圖 / 概念卡片）
- [x] README 說明：讓 agent 做了什麼、人工修改了什麼、哪些輸出不可靠
- [ ] 整理一份「行業觀察清單」（信息源、關鍵連結、觀察筆記、待驗證問題）

### 安全意識確認

- [ ] 能說明「地址 ≠ 匿名、簽名 ≠ 普通登入、授權 ≠ 轉帳」
- [ ] 確認 AI Agent 不直接接觸私鑰／助記詞
- [ ] 確認涉及簽名、授權、轉帳、合約寫入的動作保留人工確認
- [ ] 提交材料中不包含真實助記詞／私鑰截圖

---

## Q&A 清單（待學習中釐清）

### LLM 與 AI 基礎

1. **LLM 的「幻覺」（hallucination）如何在 Web3 場景下造成具體風險？** 例如 AI 編造不存在的合約地址或函數簽名會發生什麼？
2. **上下文窗口（context window）有多長？** 一份完整的智能合約 ABI 放進去會佔多少 token？
3. **temperature 和 max_tokens 的數值如何影響 API 輸出品質？** 在代碼生成場景下，temperature 應該設多少比較合適？
4. **Prompt、Workflow、Agent 的失控風險分別是什麼？** 在 Web3 場景下，哪個風險等級最高？
5. **AI Coding 工具（Claude Code / Codex）生成的 Solidity 代碼有多可靠？** 是否有已知的常見錯誤類型？
6. **MCP（Model Context Protocol）是什麼？** 它和傳統 API 調用有什麼本質差異？
7. **Guardrails 在實際 agent 系統中怎麼實作？** 有哪些開源工具可以用？
8. **Agent 的「狀態管理」和傳統後端的 session 管理有什麼異同？**

### Web3 基礎

9. **助記詞（mnemonic）如何數學上衍生出私鑰和地址？** 這個過程可逆嗎？
10. **簽名（signing）和加密（encryption）的差別是什麼？** 為什麼簽名不等於加密保護資料？
11. **Gas Limit 和 Gas Price 分別是什麼？** 交易 Gas 不夠時會發生什麼，資金會損失嗎？
12. **L1 和 L2 的實際使用體驗差別？** Sepolia 是 L1 測試網嗎？L2 有對應的測試網嗎？
13. **智能合約「不可更改」是什麼意思？** 如果合約有 bug，有什麼補救方法（proxy pattern）？
14. **ERC-4337 帳戶抽象和傳統 EOA 的最大差別是什麼？** 對 AI Agent 有什麼具體意義？
15. **區塊瀏覽器上的「Internal Transactions」是什麼？** 和普通交易有何不同？

### AI × Web3 交叉

16. **AI Agent 在執行鏈上操作時，如何設計「人工確認節點」？** 業界有哪些 best practice？
17. **「Session Key」在帳戶抽象中是什麼？** 它如何讓 AI Agent 有限度地執行鏈上操作而不需每次授權？
18. **AI 生成的 Solidity 代碼如何快速做安全審查？** 有沒有自動化工具輔助？
19. **如果 AI Agent 在測試網執行了預料外的操作，如何復原或追蹤？** 主網上呢？
20. **Web3 治理（governance）中，AI 可以扮演什麼角色？** DAO 投票有哪些現有的 AI 整合案例？

---

## 推薦材料索引

> ⚠️ 標註「待補充」的影片連結請至課程平台（web3career.build）確認原始連結。

### Module A — AI 基礎

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| What is a Large Language Model? | [YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 影片 | ★★★ | Andrej Karpathy 1hr 講座，建立 LLM 最小直覺，先看 |
| Hugging Face LLM Course Chapter 1 | [huggingface.co](https://huggingface.co/learn/llm-course/chapter1/1) | 文章 | ★★★ | 系統理解 LLM 工作原理 |
| LLM API 調用入門 | ⚠️ 待補充 | 影片 | ★★★ | 邊看邊寫 API 調用，必做；請至課程平台確認連結 |
| Anthropic: Building with the Claude API | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | 課程 | ★★★ | 官方完整入門（84 堂課、8+ hr），重點先看 Quick Start |
| Z.ai API 開發者文檔 | [docs.z.ai](https://docs.z.ai/devpack/overview) | 文件 | ★★☆ | 無 OpenAI/Claude 會員時的替代路徑，OpenAI 相容介面 |
| Z.ai Coding Plan | [z.ai/subscribe](https://z.ai/subscribe) | 訂閱 | ★★☆ | 解鎖 GLM 全系列模型調用，$10/mo 起 |
| Claude Code 101 | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-code-101) | 教程 | ★★★ | AI coding 工具快速上手 |
| AI Agent 入門 | ⚠️ 待補充 | 影片 | ★★★ | Agent 基礎概念；請至課程平台確認連結 |
| Microsoft《AI Agents for Beginners》 | [github.com/microsoft](https://github.com/microsoft/ai-agents-for-beginners) | 課程 | ★★★ | 15 堂課，從概念到代碼，有 Jupyter Notebook |
| OpenAI Agents SDK Intro | [openai.github.io](https://openai.github.io/openai-agents-python/) | 文件 | ★★☆ | 理解 handoff、guardrails、tracing 等 agent 原語 |
| LangGraph Overview | [langchain-ai.github.io](https://langchain-ai.github.io/langgraph/) | 文件 | ★★☆ | 理解 agent 的狀態圖組織方式 |
| Hermes Agent Docs | [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/docs/) | 文件 | ★★☆ | 理解 agent、tool calling、skills、跨 session 記憶 |
| Zread.ai（解讀 OpenClaw / Hermes） | [zread.ai](https://zread.ai/) · [OpenClaw repo](https://github.com/openclaw/openclaw) | 工具 | ★☆☆ | 理解 agent 進入執行層後的架構變化 |

### Module B — Web3 基礎

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| Ethereum Accounts 文件 | [ethereum.org](https://ethereum.org/en/developers/docs/accounts/) | 文件 | ★★★ | 理解帳戶與地址，必讀 |
| MetaMask Getting Started | [support.metamask.io](https://support.metamask.io/getting-started/) | 教程 | ★★★ | 理解錢包使用與安全責任 |
| Web3 運行原理 | ⚠️ 待補充 | 文章 | ★★★ | 課程補充材料；請至課程平台確認連結 |
| Ethereum Development Documentation | [ethereum.org/developers](https://ethereum.org/en/developers/docs/) | 文件 | ★★☆ | 學習路徑總入口 |
| Remix IDE | [remix.ethereum.org](https://remix.ethereum.org/) | 工具 | ★★★ | 最小合約互動入口，直接在瀏覽器動手 |
| Sepolia Faucet | [Chainlink](https://faucets.chain.link/sepolia) · [Alchemy](https://www.alchemy.com/faucets/ethereum-sepolia) · [Google Cloud](https://cloud.google.com/application/web3/faucet/ethereum/sepolia) | 工具 | ★★★ | 三個選一個領取測試幣，Week 1 必用 |
| OpenZeppelin Contracts | [docs.openzeppelin.com](https://docs.openzeppelin.com/contracts) | 文件 | ★★☆ | 合約通用組件（ERC20/721）與安全實踐 |
| Safe Overview | [docs.safe.global](https://docs.safe.global/) | 文件 | ★☆☆ | 智能帳戶與多簽，高級延展 |
| ERC-4337 文件 | [docs.erc4337.io](https://docs.erc4337.io/) · [EIP 原文](https://eips.ethereum.org/EIPS/eip-4337) | 文件 | ★☆☆ | 帳戶抽象標準，高級延展 |
| Hardhat | [hardhat.org](https://hardhat.org/docs/getting-started) | 工具 | ★☆☆ | 更工程化的合約開發路徑，Week 1 選做 |
| Foundry | [book.getfoundry.sh](https://book.getfoundry.sh/) | 工具 | ★☆☆ | Rust-based 工具鏈，速度快，Week 1 選做 |
| viem | [viem.sh](https://viem.sh/) | 工具 | ★☆☆ | TypeScript 鏈上讀寫介面，有前端基礎再看 |
| wagmi | [wagmi.sh](https://wagmi.sh/) | 工具 | ★☆☆ | React hooks for Ethereum，有前端基礎再看 |
| Neo-Cypherpunk Movement Introduction | [Web3Privacy Academy](https://academy.web3privacy.info/p/neo-cypherpunk-1011) | 文章 | ★☆☆ | 理解 Web3 的意識形態根源，選讀 |

---

## 本週交付物總覽

| 交付物 | 狀態 | 說明 |
|--------|------|------|
| GitHub Repo | 待建立 | 含 README、notes/、prompts/、demos/、logs/、resources.md |
| Learning Agent 設定記錄 | 待完成 | 工具名稱、API 路徑、模型選擇說明 |
| Agent 協助學習日誌 | 待完成 | 至少一次完整對話日誌 |
| 測試網交易記錄 | 待完成 | 錢包地址、交易哈希、區塊瀏覽器連結 |
| 智能合約部署記錄 | 待完成 | 合約地址、讀/寫交易哈希 |
| 基礎概念說明 | 待完成 | LLM→agent→錢包→簽名→交易→合約串成一條鏈 |
| 最小交叉實驗說明 | 待完成 | 流程、邊界、風險、驗證材料 |
| 可互動學習產物 | 待完成 | quiz / 流程圖 / 概念卡片（放入 demos/） |
| 行業觀察清單 | 待完成 | 信息源 + 3–5 條高品質內容筆記 |

---

## 進度日誌

| 日期 | 完成項目 | 遇到的問題 | 下一步 |
|------|---------|-----------|--------|
| 2026-05-18 | 使用ClaudeCode設定個人學習助手，使用telegram設定完/goal每日任務、/notes每日重點統整 | 尚未make agent live 24/7、資料源不足| 部署agent、設定Hermes agent/OpenClaw、增加學習資料源 |
| 2026-05-19 | | | |
| 2026-05-20 | | | |
| 2026-05-21 | | | |
| 2026-05-22 | | | |

---

*生成時間：2026-05-18｜由 Claude Code 協助整理，內容需人工複核與調整*
