# Week 2 個人學習計畫
> AIxWeb3 School｜2026-05-25（週一）～ 2026-05-31（週日）

---

## 本週定位

> Week 2 對應舊版 Week 3 的「交叉研究」。經過 Week 1 的基礎補齊、learning agent、repo 與最小實踐之後，本週不再繼續做工具入門，而是進入 AI × Web3 的問題空間：判斷哪些方向真的需要 AI 與 Web3 同時出現，哪些只是概念拼貼，並為 Week 3 / Hackathon 前的項目方向收斂準備 proposal。
>
> 如果 Week 1 回答的是「我能不能用 AI 和 Web3 做出一個最小動作」，Week 2 回答的就是「哪些問題值得用 AI × Web3 的方式繼續做，為什麼值得做，風險和邊界在哪裡」。

---

## 本週學習目標

| # | 目標 |
|---|------|
| 1 | 建立 AI × Web3 的問題空間地圖，而不是只記幾個熱門項目或標準名詞 |
| 2 | 理解 payment / commerce、identity / reputation、capability / interoperability、wallet / permission、privacy / security 等方向各自解決的問題 |
| 3 | 學會拆解一個交叉方向中的任務發起方、執行方、付款方、驗證方、風險承擔方和治理 / 仲裁方 |
| 4 | 能判斷 AI 在一個方案中承擔的是理解、生成、規劃、工具調用、自動化、監控、總結還是協作 |
| 5 | 能判斷 Web3 在一個方案中提供的是支付、身份、權限、開放狀態、可驗證記錄、結算、抗審查還是協作機制 |
| 6 | 形成一個可進入 Week 3 繼續打磨的項目初步 proposal 或研究方向說明 |

---

## 統一判斷框架

> 每個方向都用同一組問題判斷，避免項目僅是把 AI 和 Web3 兩個詞放在標題裡。

1. 這個問題如果沒有 AI，是否仍然成立？AI 到底承擔什麼能力？
2. 這個問題如果沒有 Web3，是否仍然成立？Web3 到底提供什麼機制？
3. 誰發起任務，誰執行任務，誰付款，誰驗收，誰承擔失敗成本？
4. 哪些動作可以自動化，哪些動作必須人工確認？
5. 結果如何驗證？驗證成本是否低於人工協調成本？
6. 它更像應用層體驗、開發者工具、協議 / 標準、權限系統、安全機制，還是治理協作流程？
7. 如果這個方向失敗，最可能失敗在需求不存在、信任不可建立、成本過高、介面不成熟、權限風險，還是用戶不願改變流程？

---

## 每日學習計畫（自習 3–5 hr + 晚間線上課）

> **學習策略（個人化調整）**
> 本週核心是建立問題空間地圖、選定主方向並完成初步 proposal。前兩天快速覽完所有方向（Module A + B/C），週三深入鑽研 wallet / permission 與安全議題（Module D/E），週四聚焦隱私安全與治理協作（Module F/G）並選定主方向做深挖，週五完成 proposal 撰寫與全週交付整理。

---

### 週一 5/25｜建立問題空間地圖（Module A）（4 hr）

> 重點：快速覽完所有六大方向，建立問題地圖的整體框架，用統一判斷框架練習辨別「真 AI × Web3」與「概念拼貼」。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 閱讀 | Ethereum 技術入門指南，確保鏈上狀態、交易、合約執行的理解基礎 | 30 min |
| 閱讀 | MCP 官方文檔 + A2A 官方倉庫概覽，理解 agent 與工具 / agent 之間的協作接口 | 45 min |
| 閱讀 | GLM-5.1 Agentic Coding 指南，理解 AI 在 agent workflow 中承擔什麼角色 | 30 min |
| 實作 | 嘗試 GLM-5.1 Chat Completion API，跑通第一個 function calling 請求 | 30 min |
| 整理 | 畫出 AI × Web3 問題地圖：涵蓋 6 個方向，標出每個方向的 AI 作用和 Web3 機制 | 45 min |
| 整理 | 從地圖中選出 2 個感興趣方向，各寫一句：真實用戶是誰、沒有 AI / 沒有 Web3 各缺什麼 | 30 min |

**今日產出**：AI × Web3 問題地圖（含 6 方向）+ 2 個方向初步說明

---

### 週二 5/26｜Payment / Commerce + Identity / Reputation（Module B + C）（5 hr）

> 重點：深入理解支付鏈路和 agent 身份能力層，分清報價、執行、驗收、結算各個環節，以及 MCP / A2A / ERC-8004 / MPP 各解決什麼層級的問題。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 閱讀 | x402 Docs + MPP introduction：開放支付入口與 machine payment framing | 40 min |
| 閱讀 | ERC-8004 / ERC-8183：agent trust、job、escrow、evaluator 等協議方向概覽 | 30 min |
| 閱讀 | Cobo CAW 介紹文檔：理解 Pact 機制、預算控制與審計 | 30 min |
| 整理 | 拆解一個「agent 幫人完成任務並收款」場景：誰下單、誰執行、誰驗收、誰付款、誰仲裁 | 30 min |
| 閱讀 | MCP + A2A 協議比較：工具協作 vs agent-to-agent 協作差異 | 30 min |
| 閱讀 | ENS 官方文檔 + EAS 官方網站：去中心化命名、聲明與能力發現 | 30 min |
| 整理 | 設計一個 agent profile 草圖：能做什麼、如何被調用、如何收費、如何被驗證、失敗如何處理 | 30 min |
| 整理 | 比較 x402、MPP、ERC-8004、ERC-8183 中任意兩個：各解決支付、驗證、身份、結算哪一段 | 30 min |

**今日產出**：agent commerce 場景流程拆解 + agent profile 草圖 + 協議比較筆記

---

### 週三 5/27｜Wallet / Permission + Agent DeFi Execution（Module D + E）（5 hr）

> 重點：理解授權、權限控制和可恢復執行的設計原則，並在 DeFi 執行場景中具體驗證風險邊界。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 閱讀 | ERC-4337 官方文檔 + ERC-7702：帳戶抽象基礎與智能帳戶 | 40 min |
| 閱讀 | Safe Smart Account Guards + Cobo Agentic Wallet 開發者助手 | 30 min |
| 閱讀 | MetaMask — 使用 ERC-8004 為 AI Agent 設計服務器錢包 | 20 min |
| 整理 | 畫出「agent 發起鏈上動作」的執行流程圖：哪些步驟可自動化，哪些必須人工確認 | 45 min |
| 整理 | 為 agent wallet 場景設計權限策略：預算、合約白名單、操作類型、人工確認閾值、撤銷方式 | 30 min |
| 閱讀 | Uniswap / Aave 概覽：swap、approve、deposit、borrow 等動作的風險面 | 40 min |
| 整理 | 列出各 DeFi 動作風險等級：是否可自動化、觸發人工確認條件、失敗後果 | 30 min |

**今日產出**：agent 鏈上動作執行流程圖 + 權限策略設計 + DeFi 動作風險清單

---

### 週四 5/28｜Privacy / Security + Governance + 主方向深挖（Module F + G）（5 hr）

> 重點：建立安全威脅模型，理解治理協作邊界，最後鎖定一個主方向完成深挖。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 閱讀 | MCP 工具注入攻擊防護 + 提示詞注入攻擊說明（OpenAI 文章） | 30 min |
| 閱讀 | 敏感信息披露基本常識 + 代理過剩（Agent Excess）基本知識 | 20 min |
| 整理 | 為自選 agent workflow 寫 threat model：資產、權限、數據、工具調用、外部依賴、失敗後果 | 40 min |
| 整理 | 設計「低風險自動執行 / 高風險人工確認」策略，說明觸發人工確認的條件 | 25 min |
| 閱讀 | Snapshot 官方文檔 + OpenZeppelin Governor：DAO 治理基本工具 | 30 min |
| 整理 | 選一個 DAO / 社區流程，拆出 AI 可輔助的步驟 vs 必須人工確認或治理流程通過的步驟 | 30 min |
| 整理 | 確定主方向，寫出完整問題拆解：參與方、流程、AI 作用、Web3 機制、自動化邊界、驗證方式、主要風險 | 60 min |

**今日產出**：agent workflow threat model + 治理流程拆解 + 主方向問題拆解文件

---

### 週五 5/29｜Project Proposal 撰寫 + 全週交付（3 hr）

> 策略：把本週所有分析收斂成一份可進入 Week 3 的 proposal，更新 repo，整理方向 backlog。

| 時段 | 內容 | 預計時長 |
|------|------|---------|
| 整理 | 撰寫項目初步 proposal：目標用戶、真實場景、最小功能、驗證方式、主要風險、可能賽道、Week 3 下一步 | 60 min |
| 整理 | 補充主方向深挖包：1 張流程圖、1 個典型場景、1 個反例、1 組關鍵風險、1 個最小驗證計畫 | 45 min |
| 整理 | 整理方向 backlog：記錄沒有選擇的 2–3 個方向，說明暫時不選的原因 | 15 min |
| 整理 | 更新 GitHub Repo：補充 Week 2 筆記、流程圖、proposal 到對應資料夾 | 20 min |

**今日產出**：完整 Week 2 交付物 + 項目初步 proposal + GitHub Repo 更新

---

## 待完成 Checklist

### Module A｜問題空間與方向地圖

- [ ] 閱讀 Ethereum 技術入門指南
- [ ] 閱讀比特幣白皮書（理解 Web3 解決的原始問題）
- [ ] 瀏覽 MCP 官方文檔概覽
- [ ] 瀏覽 A2A 官方倉庫概覽
- [ ] 閱讀 GLM-5.1 Agentic Coding 指南
- [ ] 跑通 GLM-5.1 Chat Completion API 的第一個 function calling 請求
- [ ] 畫出 AI × Web3 問題地圖（至少 5 個方向）
- [ ] 用統一判斷框架評估 2 個方向（分別寫「沒有 AI / 沒有 Web3 各缺什麼」）
- [ ] 選定 1 個主方向進入後續深挖

### Module B｜Payment / Commerce / Settlement

- [ ] 閱讀 x402 Docs
- [ ] 閱讀 MPP introduction + 官方文檔
- [ ] 閱讀 ERC-8004 / ERC-8183 方向概覽
- [ ] 閱讀 Cobo CAW 介紹文檔（Pact 機制、預算控制、審計）
- [ ] 拆解一個 agent commerce 場景完整流程（發現 → 報價 → 授權 → 執行 → 驗收 → 付款 → 爭議）
- [ ] 設計最小 payment / commerce flow
- [ ] 比較任意兩個協議（x402 / MPP / ERC-8004 / ERC-8183）

### Module C｜Identity / Reputation / Capability / Interoperability

- [ ] 閱讀 MCP 官方文檔（重點：工具接口層）
- [ ] 閱讀 A2A 官方倉庫（重點：agent-to-agent 協作）
- [ ] 閱讀 ENS 官方文檔
- [ ] 閱讀 EAS 官方網站
- [ ] 設計 agent profile 草圖（能力、調用方式、收費、驗證、失敗處理）
- [ ] 比較 MCP / A2A / ERC-8004 / MPP 中任意兩個，說明各解決哪層協作問題

### Module D｜Wallet / Permission / Safe Execution

- [ ] 閱讀 ERC-4337 官方文檔
- [ ] 閱讀 ERC-7702 官方文檔
- [ ] 閱讀 Safe Smart Account Guards
- [ ] 閱讀 Cobo Agentic Wallet 開發者助手文檔
- [ ] 閱讀 MetaMask ERC-8004 agent wallet 架構說明
- [ ] 畫出 agent 發起鏈上動作的執行流程圖（標出自動化 / 人工確認步驟）
- [ ] 設計 agent wallet 權限策略（預算、合約白名單、操作類型、撤銷方式、日誌記錄）

### Module E｜Agent DeFi Execution

- [ ] 閱讀提示詞注入攻擊說明（OpenAI 文章）
- [ ] 閱讀敏感信息披露基本常識
- [ ] 閱讀代理過剩基本知識
- [ ] 列出 swap / approve / deposit / borrow 各動作的風險等級與自動化邊界
- [ ] 模擬 CAW / policy 攔截 prompt injection 或越權指令，記錄哪些被攔截、哪些沒有

### Module F｜Privacy / Security / Sovereignty

- [ ] 閱讀 MCP 工具注入攻擊防護文章
- [ ] 閱讀可信執行環境（TEE）基本知識
- [ ] 閱讀新密碼朋克運動介紹
- [ ] 為一個 agent workflow 寫完整 threat model（資產、權限、數據、工具調用、外部依賴、失敗後果）
- [ ] 設計低風險 / 高風險自動化邊界策略，說明觸發人工確認條件
- [ ] 找一個「看似酷炫但風險很高」的 AI × Web3 idea 並分析為什麼現在不應直接自動化

### Module G｜Governance / Coordination / Public Goods

- [ ] 閱讀 Snapshot 官方文檔
- [ ] 閱讀 OpenZeppelin Governor 官方文檔
- [ ] 閱讀 Gitcoin 資助機制
- [ ] 選一個 DAO / 社區流程做 AI 輔助步驟 vs 人工確認步驟的拆解
- [ ] 做一個 proposal summarizer / meeting-to-action workflow / contribution tracker 草圖

### 全週交付物

- [ ] AI × Web3 問題地圖（至少 5 個方向，含 AI 作用 + Web3 機制）
- [ ] 方向選擇說明（1 個主方向 + 為什麼不是純 AI 或純 Web3 問題）
- [ ] 主方向問題拆解文件（參與方、流程、AI 作用、Web3 機制、自動化邊界、人工確認點、驗證方式、主要風險）
- [ ] 項目初步 proposal（目標用戶、真實場景、最小功能、驗證方式、主要風險、可能賽道、Week 3 下一步）
- [ ] 參考資料清單（至少 5 條，說明每條幫助判斷什麼）
- [ ] 主方向深挖包（1 張流程圖 + 1 個典型場景 + 1 個反例 + 1 組關鍵風險 + 1 個最小驗證計畫）
- [ ] 方向 backlog（2–3 個未選方向 + 暫時不選的原因）
- [ ] GitHub Repo 更新（Week 2 筆記、流程圖、proposal 更新至對應資料夾）

---

## Q&A 清單（待學習中釐清）

### 問題空間判斷

1. **如何快速判斷一個 AI × Web3 想法是「真需求」還是「概念拼貼」？** 有沒有一個最小的判斷流程？
2. **當一個方向的 AI 部分可以被普通自動化替代、Web3 部分可以被傳統資料庫替代時，這個方向還有價值嗎？**
3. **統一判斷框架中的「驗證成本 vs 人工協調成本」如何量化？** 有什麼工程上的估算方法？

### Payment / Commerce

4. **x402、MPP、ERC-8004、ERC-8183 各在哪個層級？** 它們能組合使用嗎，還是互相競爭的標準？
5. **agent commerce 的「爭議處理」在鏈上如何實作？** oracle、仲裁合約、評價系統有哪些現有方案？
6. **Cobo CAW 的 Pact 機制如何在任務失敗時恢復？** 預算未用完的部分如何退回？

### Identity / Reputation / Capability

7. **MCP 和 A2A 的本質差異是什麼？** 什麼場景下應該用 MCP，什麼場景下應該用 A2A？
8. **agent 的 reputation 如何防止被刷？** 鏈上記錄可以被女巫攻擊嗎？
9. **ERC-8004 的「capability manifest」和 OpenAI function calling schema 是什麼關係？**

### Wallet / Permission / Security

10. **ERC-4337 和 ERC-7702 分別解決什麼？** 它們互補還是重疊？
11. **Session Key 的有效期和撤銷機制如何設計？** 如果 session key 被洩露，怎麼快速應對？
12. **Safe guard / policy 能攔截哪些類型的惡意操作？** 有哪些它無法防止的攻擊向量？

### DeFi Execution / Privacy

13. **prompt injection 攻擊在 DeFi agent 場景下的最危險形式是什麼？** 有沒有具體案例？
14. **approve 操作的最大風險是什麼？** agent 應該如何設計授權上限和過期機制？
15. **可信執行環境（TEE）在 AI × Web3 中的實際應用現況如何？** 主要項目有哪些？

### Governance / Coordination

16. **AI 生成的 DAO 提案總結如何避免「選擇性摘要」的偏差問題？**
17. **Snapshot offchain 投票和 OpenZeppelin Governor onchain 執行如何連接？** 中間有哪些風險點？
18. **公共物品資助（Gitcoin QF）的 Sybil 防禦機制和 AI 分析能力如何結合？**

---

## 推薦材料索引

### Module A — 問題空間基礎

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| Ethereum 技術入門指南 | [ethereum.org](https://ethereum.org/en/developers/docs/) | 文件 | ★★★ | 鏈上技術理解基礎入口 |
| 比特幣白皮書 | [bitcoin.org](https://bitcoin.org/bitcoin.pdf) | 論文 | ★★☆ | 理解 Web3 解決的原始問題：無可信第三方的點對點價值轉移 |
| Model Context Protocol | [modelcontextprotocol.io](https://modelcontextprotocol.io) | 文件 | ★★★ | agent 與工具協作接口 |
| A2A 官方倉庫 | [github.com/google-deepmind/a2a](https://github.com/google-deepmind/a2a) | 文件 | ★★★ | agent-to-agent 協作協議 |
| GLM-5.1 Agentic Coding 指南 | ⚠️ 待補充（課程平台） | 指南 | ★★★ | 理解 AI 在 agent workflow 中的能力定位 |
| GLM-5.1 Chat Completion API | ⚠️ 待補充（課程平台） | API 文件 | ★★★ | 5 分鐘跑通 function calling，最小骨架 |
| Web Search Tool | ⚠️ 待補充（課程平台） | 工具文件 | ★★☆ | 免接 search API，快速搭建帶外部信息源的 agent demo |

### Module B — Payment / Commerce / Settlement

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| x402 Docs | [x402.org](https://x402.org) | 文件 | ★★★ | 開放支付入口與 machine payment framing |
| MPP Introduction | ⚠️ 待補充（課程平台） | 文件 | ★★★ | Machine Payments Protocol 問題背景 |
| MPP 官方文檔 | ⚠️ 待補充（課程平台） | 文件 | ★★★ | 協議細節 |
| ERC-8004 / ERC-8183 | [eips.ethereum.org](https://eips.ethereum.org) | 提案 | ★★☆ | agent trust、job、escrow、evaluator 方向 |
| Stripe Agentic Commerce | [stripe.com](https://stripe.com/blog/agentic-commerce) | 文章 | ★★☆ | Web2 / fintech 側 agent commerce 對照材料 |
| Cobo CAW 介紹 | [cobo.com/products/agentic-wallet/manual](https://www.cobo.com/products/agentic-wallet/manual/start-here/introduction) | 文件 | ★★★ | Pact 機制、預算控制與審計案例 |
| Cobo CAW 索引頁 | [cobo.com/products/agentic-wallet/manual/llms.txt](https://cobo.com/products/agentic-wallet/manual/llms.txt) | 文件 | ★★☆ | LLM 可讀格式的完整索引 |
| Olas | [olas.network](https://olas.network) | 文件 | ★☆☆ | agent economy / autonomous services 方向參考 |

### Module C — Identity / Reputation / Capability

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| MCP 官方文檔 | [modelcontextprotocol.io](https://modelcontextprotocol.io) | 文件 | ★★★ | 工具上下文與 agent-tool 接口 |
| A2A 官方倉庫 | [github.com/google-deepmind/a2a](https://github.com/google-deepmind/a2a) | 文件 | ★★★ | agent-to-agent 協作協議 |
| ERC-8004 / ERC-8183 | [eips.ethereum.org](https://eips.ethereum.org) | 提案 | ★★☆ | agent trust / job / evaluator 方向 |
| ENS 官方文檔 | [docs.ens.domains](https://docs.ens.domains) | 文件 | ★★☆ | 去中心化命名、聲明、聲譽與能力發現 |
| EAS 官方網站 | [attest.org](https://attest.org) | 文件 | ★★☆ | 鏈上或鏈下證明，任意事物皆可 |

### Module D — Wallet / Permission / Safe Execution

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| ERC-4337 官方文檔 | [docs.erc4337.io](https://docs.erc4337.io) | 文件 | ★★★ | 帳戶抽象基礎協議 |
| ERC-7702 官方文檔 | [eips.ethereum.org/EIPS/eip-7702](https://eips.ethereum.org/EIPS/eip-7702) | 文件 | ★★☆ | EOA 轉智能合約，更靈活的帳戶升級路徑 |
| Coinbase Policy Engine | [docs.coinbase.com](https://docs.coinbase.com) | 文件 | ★★☆ | 自定義交易政策參考 |
| Cobo Agentic Wallet 開發者助手 | [cobo.com/products/agentic-wallet](https://cobo.com/products/agentic-wallet) | 文件 | ★★★ | 如何整合原生 agent 錢包 |
| Safe Smart Account Guards | [docs.safe.global](https://docs.safe.global) | 文件 | ★★★ | 多簽、智能帳戶與 guard / policy |
| MetaMask ERC-8004 agent wallet | ⚠️ 待補充（課程平台） | 文章 | ★★☆ | agent identity + backend signer + wallet execution 生產架構 |
| LI.FI Agents | [docs.li.fi/agents/overview](https://docs.li.fi/agents/overview) | 文件 | ★★☆ | agent 查詢鏈上狀態並執行跨鏈動作 |

### Module E / F — DeFi Execution / Privacy / Security

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| 理解提示詞注入攻擊 | ⚠️ 待補充（課程平台） | 文章 | ★★★ | OpenAI 關於 prompt injection 的介紹 |
| 敏感信息披露基本常識 | ⚠️ 待補充（課程平台） | 文章 | ★★★ | 敏感數據洩露風險基本知識 |
| 代理過剩基本知識 | ⚠️ 待補充（課程平台） | 文章 | ★★☆ | Agent Excess 基本知識 |
| MCP 工具注入攻擊防護 | ⚠️ 待補充（課程平台） | 文章 | ★★★ | 如何防止 MCP 間接提示注入攻擊 |
| Safe Smart Account Guards | [docs.safe.global](https://docs.safe.global) | 文件 | ★★☆ | 受限執行與權限控制參考 |
| 可信執行環境（TEE） | ⚠️ 待補充（課程平台） | 文章 | ★★☆ | TEE 基本概念與知識 |
| 新密碼朋克運動 | [Web3Privacy Academy](https://academy.web3privacy.info/p/neo-cypherpunk-1011) | 文章 | ★☆☆ | Neo-Cypherpunk 運動理解 |
| dDocs | ⚠️ 待補充（課程平台） | 工具 | ★☆☆ | end-to-end encrypted collaboration 方向參考 |

### Module G — Governance / Coordination / Public Goods

| 材料 | 連結 | 類型 | 優先度 | 備注 |
|------|------|------|--------|------|
| Ethereum 治理基礎 | [ethereum.org](https://ethereum.org/en/governance/) | 文件 | ★★★ | 以太坊鏈上治理基礎知識 |
| 去中心化自治組織（DAO） | [ethereum.org](https://ethereum.org/en/dao/) | 文件 | ★★★ | DAO 基本知識 |
| Snapshot 官方文檔 | [docs.snapshot.org](https://docs.snapshot.org) | 文件 | ★★★ | offchain voting、proposal、space、strategy |
| OpenZeppelin Governor | [docs.openzeppelin.com](https://docs.openzeppelin.com/contracts/governor) | 文件 | ★★☆ | onchain execution，更偏工程實作 |
| Gitcoin 資助機制 | [gitcoin.co](https://gitcoin.co) | 文章 | ★★☆ | 公共物品資助機制（Quadratic Funding） |

---

## 本週交付物總覽

| 交付物 | 狀態 | 說明 |
|--------|------|------|
| AI × Web3 問題地圖 | 待完成 | 至少 5 個方向，標出 AI 作用與 Web3 機制 |
| 方向選擇說明 | 待完成 | 主方向 + 為什麼不是純 AI 或純 Web3 問題 |
| 主方向問題拆解 | 待完成 | 參與方、流程、AI 作用、Web3 機制、自動化邊界、人工確認點、驗證方式、主要風險 |
| 項目初步 Proposal | 待完成 | 目標用戶、真實場景、最小功能、驗證方式、主要風險、可能賽道、Week 3 下一步 |
| 參考資料清單 | 待完成 | 至少 5 條，說明每條資料幫助判斷什麼 |
| 主方向深挖包 | 待完成 | 1 張流程圖 + 1 個典型場景 + 1 個反例 + 1 組關鍵風險 + 1 個最小驗證計畫 |
| 方向 Backlog | 待完成 | 2–3 個未選方向 + 暫時不選的原因 |
| GitHub Repo 更新 | 待完成 | Week 2 筆記、流程圖、proposal 更新至對應資料夾 |

---

## 進度日誌

| 日期 | 完成項目 | 遇到的問題 | 下一步 |
|------|---------|-----------|--------|
| 2026-05-25 | | | |
| 2026-05-26 | | | |
| 2026-05-27 | | | |
| 2026-05-28 | | | |
| 2026-05-29 | | | |

---

*生成時間：2026-05-25｜由 Claude Code 協助整理，內容需人工複核與調整*
