# AIxWeb3 School — Handbook
> 課程期間：2026-05-18 ～ 2026-06-14｜學習全程參考手冊，涵蓋 AI 知識體系、Web3 基礎與 AI × Web3 交叉應用

---

## 目錄

**Part I — AI 知識體系**
1. [LLM（大語言模型）](#1-llm大語言模型)
2. [Prompt（提示詞）](#2-prompt提示詞)
3. [Context（上下文）](#3-context上下文)
4. [RAG（檢索增強生成）](#4-rag檢索增強生成)
5. [Agent（智能體）](#5-agent智能體)
6. [MCP（模型上下文協議）](#6-mcp模型上下文協議)
7. [Frameworks（AI 框架）](#7-frameworks-ai-框架)
8. [Inference（推理服務）](#8-inference推理服務)
9. [Evaluation（評估）](#9-evaluation評估)
10. [Fine-tuning（微調）](#10-fine-tuning微調)
11. [Vibe Coding（AI 輔助編程）](#11-vibe-codingai-輔助編程)

**Part II — Web3 知識體系**
12. [帳戶（Account）](#12-帳戶account)
13. [簽名（Signing）](#13-簽名signing)
14. [交易（Transaction）](#14-交易transaction)
15. [智能合約（Smart Contract）](#15-智能合約smart-contract)
16. [Gas 與費用](#16-gas-與費用)
17. [L1 vs. L2](#17-l1-vs-l2)
18. [區塊瀏覽器](#18-區塊瀏覽器)
19. [錢包體系](#19-錢包體系)
20. [Web3 交易完整週期](#20-web3-交易完整週期)
21. [支付系統：Web2 vs. Web3](#21-支付系統web2-vs-web3)

**Part III — AI × Web3 交叉**
22. [AI Agent 在鏈上的設計](#22-ai-agent-在鏈上的設計)
23. [Session Key](#23-session-key)
24. [AI 生成 Solidity 的注意事項](#24-ai-生成-solidity-的注意事項)
25. [AI × Web3 角色分工](#25-ai--web3-角色分工)

**Part IV — 安全**
26. [安全邊界原則](#26-安全邊界原則)

**附錄**
27. [術語速查表](#27-術語速查表)
28. [Q&A 清單](#28-qa-清單)
29. [推薦資源索引](#29-推薦資源索引)
30. [交付物 Checklist](#30-交付物-checklist)

---

## Part I — AI 知識體系

### 1. LLM（大語言模型）

**核心定義：** LLM 是把大量文本、代碼和多模態信號壓進參數裡的概率模型。它生成的是概率上合理的輸出，不是天然可信的事實。

**第一性原理：**
- 把模型當推理層，不當真相源：關鍵事實必須來自數據庫、API、日誌或其他可信系統
- 把輸出變成可檢查對象：摘要、計劃和建議都應落成 schema、引用或日誌
- 不確定時顯式降級：模型不知道時要讓系統說不確定，不是讓模型補完缺口

**核心知識節點：**

| 概念 | 說明 | 注意事項 |
|------|------|---------|
| Token | tokenizer 切分後的文本單元，不等於字或詞 | 代碼、JSON、長標識符比普通文本更吃 token |
| Context Window | 一次請求能處理的最大 token 數 | Claude 200K；超出後早期內容被截斷 |
| Embedding | 把文本映射成向量，衡量語義相近度 | 適合搜索、RAG；不能單獨驗證事實 |
| Transformer | 現代 LLM 核心架構，通過 attention 關注上下文 | 擅長模式組合，沒有事實最終裁決權 |
| Hallucination | 模型生成看似合理但不真實的內容 | 在帶執行能力的系統裡會變成流程風險 |
| Multimodal | 處理文本、圖片、音頻、截圖等多種輸入 | 關鍵判斷仍需回到結構化數據和可信來源 |
| Temperature | 控制輸出隨機性（0=確定，1=隨機） | 代碼生成建議 0.1～0.3 |

**LLM 在 AI × Web3 系統中的位置：**

```
數據層  ──  RPC / 索引器 / 預言機 / 向量庫 / 文檔
                          ↓
編排層  ──  Prompt + Context + RAG + Agent Workflow
                          ↓
  LLM  ──  理解與生成層（把目標轉成計劃，把鏈上數據解釋成人能讀的語言）
                          ↓
執行層  ──  工具調用 / 錢包 / Smart Account / 合約交互
                          ↓
安全層  ──  Guard / Simulation / 權限策略 / 人工確認 / 日誌
```

> LLM 越靠近執行層，系統越要把自然語言輸出變成可驗證對象。

---

### 2. Prompt（提示詞）

**核心定義：** Prompt 是把任務目標、輸入邊界、輸出格式、失敗處理和安全規則寫進一次可執行的溝通協議。它不只是「怎麼問 AI」，而是一份工作說明書。

**第一性原理：**
- **Prompt 是軟約束，不是安全邊界**：真正的邊界必須由代碼、權限、校驗和審計承擔
- 指令分層：系統規則 / 開發者規則 / 用戶目標 / 檢索內容不能混在同一層
- 高風險動作（寫入、發送、支付、簽名）不能只靠 prompt 攔截

**Instruction 四段式寫法：**

```
1. 任務目標  — 你是什麼角色、要完成什麼
2. 可用輸入  — 哪些信息可以使用
3. 禁止行為  — 不能做什麼
4. 輸出格式和失敗格式  — 成功時輸出什麼 schema，遇到不確定時輸出什麼
```

**核心知識節點：**

| 概念 | 說明 |
|------|------|
| Few-shot | 在 prompt 裡放示例，讓模型模仿輸出格式和判斷方式；示例要跟 eval 一起維護 |
| Structured Output | 讓模型按固定 JSON schema 返回，便於後續代碼處理和回歸測試 |
| Prompt Injection | 攻擊者通過文檔/網頁/用戶輸入讓模型忽略原始規則、洩露信息或調用危險工具 |

**防止 Prompt Injection 的可靠做法：**
- 外部內容標記為不可信數據（不給系統指令同等優先級）
- 工具調用前做參數校驗
- 敏感動作強制走 allowlist 和 human approval
- 不把密鑰、主權限和不可撤銷動作交給模型

---

### 3. Context（上下文）

**核心定義：** Context 是模型這一次能看到、能使用、能被影響的信息空間。真正難的不是塞更多內容進去，而是把不同信息分清楚。

**第一性原理：**
- 模型只能基於它看見的上下文行動；系統必須決定什麼能進上下文、帶著什麼身份進去
- Context 是信息治理問題，不是文本拼接問題
- 每類信息要標注來源、時效、權限和可信度

**上下文分層架構：**

| 層級 | 內容 | 特性 |
|------|------|------|
| 指令層 | 系統規則、工具使用規則、禁止事項 | 最高優先級，不得被外部內容覆蓋 |
| 任務層 | 用戶目標、本次會話參數 | 每次請求更新 |
| 事實層 | 鏈上狀態、工具結果、simulation | 必須實時查詢，不能長期緩存 |
| 知識層 | 文檔、標準、論壇、歷史案例 | 需要來源、版本和廢棄狀態標注 |
| 記憶層 | 用戶偏好和項目配置 | 不能替代實時授權 |

**核心知識節點：**

| 概念 | 說明 |
|------|------|
| Context Engineering | 設計上下文進入模型的方式：選源、排序、裁剪、隔離不可信內容 |
| Memory | 跨請求保留的信息（偏好、歷史任務），不能替代當次實時授權 |
| Knowledge Base | 系統可檢索的外部知識庫，需維護來源、版本、廢棄狀態 |

> 記憶不能替代實時授權。用戶過去允許某個動作，不代表現在仍然允許。

---

### 4. RAG（檢索增強生成）

**核心定義：** RAG 是把外部知識取回、篩選、引用、交給模型使用的證據鏈，用來解決 LLM 訓練知識過期和 context window 放不下所有資料的問題。

**第一性原理：**
- RAG 的可靠性取決於證據鏈，不取決於「向量庫」這個名詞
- 檢索結果是候選證據，不是事實：仍要看來源、時間、版本和適用範圍
- 檢索失敗要允許拒答，不是讓模型補全

**RAG 三個關鍵判斷：**

```
文檔怎麼切（Chunking）
          ↓
查詢時取哪些內容（Retriever + Rerank）
          ↓
生成時如何引用和拒答（Citation + 來源邊界）
```

**核心知識節點：**

| 概念 | 說明 |
|------|------|
| Chunking | 按結構切分文檔（標題、函數說明、FAQ），每個 chunk 保留來源 URL、版本 |
| Vector DB | 存 embedding + metadata，按語義相似度檢索；向量相似 ≠ 答案正確 |
| Retriever | 取回候選材料，可結合向量 + 關鍵詞 + metadata filter |
| Rerank | 初步檢索後重新排序，把更相關/更可信/更完整的排前面 |
| Citation | 答案裡的關鍵結論連接回來源，是用戶驗證答案的入口 |

> 沒有 citation 和 freshness 的 RAG，只是把幻覺從模型內部搬到了檢索系統裡。

---

### 5. Agent（智能體）

**核心定義：** Agent 是能圍繞目標持續調用工具、讀取狀態、調整步驟的 AI 系統。它的關鍵不在「像人」，而在於能否在明確權限和可審計流程裡把建議推進到行動。

**第一性原理：**
- **Agent 不是自主權本身，而是被約束的執行循環**
- 工具比回答更危險：讀數據、寫數據庫、發送請求、改配置不是同一風險等級
- 狀態必須外置和可查，不能只藏在模型 context 裡
- 停止條件要明確：目標達成、超出預算、信息不足、風險越界、用戶拒絕

**Agent 核心組件：**

```
┌─────────────────────────────────────────────────────────┐
│                       AI Agent                          │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│  │  Memory  │  │ Planning │  │  Tool Use            │  │
│  │（記憶層） │  │（規劃層） │  │（工具調用）           │  │
│  └──────────┘  └──────────┘  └──────────────────────┘  │
│                                                         │
│  ┌──────────┐  ┌────────────────────────────────────┐   │
│  │  State   │  │       Guardrails（安全護欄）         │   │
│  │（狀態層） │  └────────────────────────────────────┘   │
│  └──────────┘                                           │
└─────────────────────────────────────────────────────────┘
```

**核心知識節點：**

| 概念 | 說明 |
|------|------|
| Tool Use | 調用外部能力（API、DB、代碼執行等）；讓 Agent 從「會回答」變成「能做事」 |
| Planning | 把目標拆成步驟（ReAct 模式：Reason → Act → Observe） |
| State | 任務狀態（目標、步驟、工具返回、錯誤、預算、確認記錄）；必須外置可查可恢復 |
| Reflection | Agent 檢查中間結果並修正；適合提升質量，不能替代外部驗證 |
| Multi-Agent | 多個 Agent 分工協作；注意上下文傳遞丟失和責任邊界模糊問題 |
| Handoff | Agent 之間的任務移交（multi-agent 系統） |
| Guardrails | 輸入/輸出的安全過濾層，防止有害或異常操作 |

**Prompt / Workflow / Agent 差異：**

| 維度 | Prompt | Workflow | Agent |
|------|--------|----------|-------|
| 結構 | 單次輸入 → 輸出 | 固定步驟串聯 | 動態決策 + 工具調用循環 |
| 自主性 | 無 | 低 | 高 |
| 狀態管理 | 無狀態 | 有限狀態 | 持久狀態 |
| 錯誤風險 | 最低 | 中 | 最高（Web3 場景） |
| 典型工具 | API 直接調用 | LangGraph、n8n | OpenAI Agents SDK、Claude Code |

> Web3 場景風險排序：Agent > Workflow > Prompt（Agent 可能在無人確認下執行鏈上操作）

---

### 6. MCP（模型上下文協議）

**核心定義：** MCP（Model Context Protocol）是 Anthropic 提出的標準協議，把模型和外部工具、數據源之間的連接標準化——讓工具接入變得可描述、可發現、可限制。

**第一性原理：**
- 模型不應該直接擁有世界；它應該通過明確協議訪問被授權的上下文和工具
- 工具要有 schema：沒有 schema，模型調用工具就是猜參數
- 權限在協議外也必須成立：真正的授權、審計和隔離由系統實現
- 錯誤要可傳遞：工具失敗/超時/權限不足必須明確返回

**MCP 架構：**

| 角色 | 職責 |
|------|------|
| MCP Server | 暴露 resources、tools、prompts；定義邊界（只讀/副作用/授權） |
| MCP Client | 連接模型和 server；負責用戶確認、權限提示、會話隔離 |
| Tool Schema | 描述工具名字、用途、參數、返回值和約束 |

**MCP vs. 傳統 API：**
- 傳統 API：開發者在代碼中硬編碼調用邏輯
- MCP：模型動態發現並調用工具，工具能力由 MCP Server 描述，模型自主選擇

> MCP 標準化工具入口，但不能替代帳戶權限、交易模擬、簽名確認和審計日誌。

---

### 7. Frameworks（AI 框架）

**核心定義：** AI Framework 把模型、工具、狀態、檢索、評估和部署組織成可維護的系統。框架選錯，問題通常不是「跑不起來」，而是「調不動、測不了、換不掉」。

**第一性原理：**
- **框架是系統邊界的表達，不是智能本身**
- 先理解工作流，再決定用不用框架：不要讓產品邏輯遷就框架
- 框架要能退出：難以換模型、換部署方式的框架，長期成本很高

**主要框架對比：**

| 框架 | 定位 | 適用場景 |
|------|------|---------|
| LangChain | 組件庫：模型接入、prompt、工具、retriever、agent | 快速組合能力；注意不要讓邊界遷就框架 |
| LangGraph | 工作流 + 狀態機，任務表示成有向圖 | 多輪工具調用、分支、重試、人工確認、長期運行 |
| OpenAI Agents SDK | Agent 工作流：tools、handoff、guardrails、tracing | 組織多 Agent 協作和工具調用 |
| DSPy | 把 prompt pipeline 寫成可優化程序 | 有明確數據集和評估指標的結構化任務 |
| Hermes | 工具調用和結構化輸出的模型生態 | 評估模型 tool calling 穩定性 |

**何時需要顯式狀態管理（LangGraph 等）：**
- 關心任務走到哪一步、是否能從失敗點恢復
- 有人工確認節點或分支邏輯
- 多輪工具調用且需要審計記錄

---

### 8. Inference（推理服務）

**核心定義：** 訓練決定模型學到了什麼，推理決定模型在真實產品裡如何響應。Inference 是延遲、成本、上下文、穩定性和部署邊界的綜合選擇。

**第一性原理：**
- 推理服務的核心不是「跑出答案」，而是在約束條件下交付可用答案
- 質量有代價：更強模型意味著更高成本、更長延遲或更複雜部署
- 服務要可替換：把模型調用封裝清楚，才有機會做 fallback、灰度和評估

**部署模式對比：**

| 模式 | 優點 | 限制 | 適用場景 |
|------|------|------|---------|
| API Model | 上手快、模型更新快、基礎設施負擔低 | 成本、速率限制、隱私風險 | 大多數產品早期 |
| Local Model | 隱私保護、成本可控、可離線 | 顯存、並發、部署複雜 | 隱私敏感、特定任務 |
| Quantization | 降低顯存和計算需求（FP16→INT8/INT4） | 可能降低輸出質量 | 邊緣設備、資源受限環境 |

**成熟推理服務的必要問題：**
- 請求失敗時怎麼重試或降級？
- 模型版本怎麼灰度？
- 輸入輸出日誌如何脫敏？
- 成本、延遲和錯誤率如何監控？

> 鏈上動作不可逆，推理層要留下可審計記錄：用了哪個模型、輸入來自哪裡、輸出是什麼。

---

### 9. Evaluation（評估）

**核心定義：** Evaluation 是把「感覺效果不錯」變成「系統可持續改進」的方法。沒有 eval，prompt、模型、RAG、Agent 的變化都只能靠主觀試用，遲早被回歸問題拖住。

**第一性原理：**
- 不能被重複測量的 AI 行為，就不能被穩定改進
- 先測任務，不只測模型：用戶真正關心的是整條鏈路是否完成任務
- 評估要貼近產品：離真實輸入越遠，eval 越容易變成自我安慰

**Eval 核心組件：**

| 組件 | 說明 |
|------|------|
| Harness | 餵樣本、調用系統、收集輸出、運行 grader、記錄結果的框架 |
| Golden Set | 被認真挑選的測試樣本（早期 30～100 條），覆蓋正常 + 邊界 + 高風險 + 注入 |
| LLM-as-Judge | 用模型評分模型輸出；適合開放式任務，不能替代規則評分和人工抽檢 |
| Regression | 防止舊問題復發；每次 prompt/模型/retriever 變更前後都要跑 |
| Observability | 線上記錄輸入、工具調用、輸出、錯誤、用戶反饋、成本延遲 |

**AI × Web3 場景需要特別評估：**
- 交易解釋是否準確
- 風險提示是否漏報
- 工具調用參數是否越界
- 是否能拒絕不確定請求
- 是否能識別 Prompt Injection
- 高風險動作是否要求 human check

---

### 10. Fine-tuning（微調）

**核心定義：** Fine-tuning 讓模型更穩定地學習某種格式、風格、領域任務或行為模式。它不適合補實時知識、修權限邊界或替代評估。

**第一性原理：**
- Fine-tuning 改的是模型行為分佈，不是產品系統邊界
- **先有 eval，再談 fine-tuning**：否則不知道微調後是真的變好了還是在少數樣本上變順了
- 先修數據，再修模型：壞數據會把壞習慣訓練得更穩定
- 別用微調存實時知識：用 RAG 或工具來補

**何時考慮 Fine-tuning（先排除其他選項）：**

```
prompt 不清楚？→ 先優化 prompt
上下文缺了？→ 先補 context / RAG
輸出格式沒有 schema？→ 先加 structured output
以上都做了仍不穩定 → 才考慮 fine-tuning
```

**核心知識節點：**

| 概念 | 說明 |
|------|------|
| SFT（監督微調） | 用輸入-輸出樣本讓模型學習特定任務格式或風格 |
| LoRA | 低秩適配（Low-Rank Adaptation），降低訓練成本；不更新全部參數 |
| PEFT | 參數高效微調方法統稱（LoRA 是其中之一） |
| Overfitting | 模型把訓練數據記太死；訓練集太小/風格太單一/輪數太多都會導致 |

---

### 11. Vibe Coding（AI 輔助編程）

**核心定義：** Vibe Coding 是人和 AI Coding Agent 共同迭代軟件的工作方式：人負責方向、約束和驗收，Agent 負責生成、修改、搜索和執行部分工程動作。

**第一性原理：**
- AI Coding 的核心不是自動生成代碼，而是**把工程反饋循環壓短**
- 任務要小：越具體越有邊界，Agent 越容易產出可審查結果
- 上下文要準：讓 Agent 看對文件和設計約束，比寫長篇需求更重要
- 驗證要硬：運行測試、類型檢查、構建，比「看起來對」可靠
- AI 能幫你寫更多代碼，但不能替你承擔工程判斷

**適用 vs. 不適用場景：**

| 適用 | 不適用 |
|------|--------|
| 搭原型、修小 bug | 無邊界重寫整個項目 |
| 補測試、寫腳本 | 直接上線 AI 生成的合約代碼 |
| 解釋陌生代碼 | 繞過工程審查流程 |
| 重構局部模塊 | 把密鑰/生產配置交給 Agent |

**工具概覽：**

| 工具 | 定位 |
|------|------|
| Claude Code | CLI + IDE 整合，Anthropic 官方，深度代碼理解 |
| Codex CLI | OpenAI 出品，適合腳本自動化 |
| gh CLI | 把 AI 改動接回 issue、PR 和 review 流程 |

**AI Coding 最小安全規範：**
1. 明確哪些文件可以改、哪些命令可以跑
2. 每次改動後看 `git diff` 和測試結果
3. 確認不含密鑰、日誌、構建產物
4. 鏈上相關代碼（合約、簽名、支付腳本）必須人工審查，不能只靠 Agent 生成後直接上線

---

## Part II — Web3 知識體系

### 12. 帳戶（Account）

**以太坊帳戶類型：**

| 類型 | 全名 | 控制方式 | 特點 |
|------|------|---------|------|
| EOA | Externally Owned Account | 私鑰 | 最基本的帳戶，無代碼 |
| 合約帳戶 | Contract Account | 代碼邏輯 | 由 EOA 或其他合約觸發 |

**地址的本質（單向不可逆）：**
```
助記詞（Mnemonic）
    ↓（BIP-39）
種子（Seed）
    ↓（BIP-44 HD Wallet）
私鑰（Private Key）
    ↓（橢圓曲線 ECDSA）
公鑰（Public Key）
    ↓（Keccak-256 Hash）
地址（Address）
```

知道地址無法反推私鑰。

---

### 13. 簽名（Signing）

**核心公式：**
```
message + private key → signature
```

**簽名 ≠ 加密：**
- 加密（Encryption）：用公鑰加密，私鑰解密 → 保護數據隱私
- 簽名（Signing）：用私鑰簽名，公鑰驗證 → 證明身份與授權

**為什麼簽名不等於普通登入：**
- Web2 登入：撤銷密碼即可取消授權
- Web3 簽名：一旦簽名的交易被廣播上鏈，無法撤銷

---

### 14. 交易（Transaction）

**關鍵參數：**

| 參數 | 說明 | 注意事項 |
|------|------|---------|
| `gas` | 交易手續費 = gas count × gas price | Gas 不足交易失敗，費用不退 |
| `nonce` | 確保交易冪等的序號（ETH 帳戶模型） | 每筆交易 nonce 唯一且遞增 |
| `calldata` | 鏈上交易的「靈魂」，執行端解析後決定合約行為 | 合約調用的函數選擇器和參數都在這裡 |
| `value` | 隨交易發送的 ETH 數量 | |
| `to` | 目標地址（EOA 或合約） | |

**EIP-1559（倫敦升級後的 Gas 機制）：**
- `baseFee`：由網路自動調整，銷毀（burn）掉
- `priorityFee`（小費）：支付給礦工/驗證者
- `maxFeePerGas`：用戶願意支付的上限

**不同鏈的 Nonce 機制：**
- **以太坊**：帳戶模型，nonce 按順序排列
- **Tron / Solana**：無 nonce，用交易 Hash 確保唯一性
- **Bitcoin**：UTXO 模型，原生冪等（每個 UTXO 只能使用一次）

---

### 15. 智能合約（Smart Contract）

**定義：** 部署在區塊鏈上的自執行代碼，觸發條件滿足時自動執行，任何人可驗證。

**不可更改性（Immutability）：** 合約代碼一旦部署，邏輯無法修改。
- **補救方法：Proxy Pattern**（代理模式）
  - 將合約拆成「Proxy（入口）+ Implementation（邏輯）」
  - 升級時只部署新的 Implementation，Proxy 的地址不變
  - 缺點：增加複雜度，需要嚴格的 upgrade 權限管理

**常見合約標準（OpenZeppelin）：**
- **ERC-20**：同質化代幣標準（如 USDC、DAI）
- **ERC-721**：非同質化代幣標準（NFT）
- **ERC-4337**：帳戶抽象標準（Account Abstraction）

---

### 16. Gas 與費用

```
gas fee = gas count × gas price
```

- Gas **不足**：交易 revert（失敗），已消耗的 gas 費不退
- Gas **過多**：多餘的 gas 退回給發送者
- 設定 Gas Limit 的原則：略高於估算值（留 10-20% 餘量）

---

### 17. L1 vs. L2

| 維度 | L1（如以太坊主網） | L2（如 Optimism、Arbitrum） |
|------|-----------------|--------------------------|
| 安全性 | 最高（原生共識） | 繼承 L1 安全 |
| 交易速度 | 較慢（~12s/block） | 更快 |
| Gas 費用 | 較高 | 顯著降低 |
| 測試網 | Sepolia（ETH L1 測試網） | 各 L2 有對應測試網（如 Optimism Sepolia） |

---

### 18. 區塊瀏覽器（Block Explorer）

用於查詢鏈上所有公開資訊的工具（如 Sepolia Etherscan）。

**可查詢的資訊：**
- 交易哈希（Tx Hash）
- 交易狀態（Success / Failed）
- Gas 使用量與費用
- 區塊高度（Block Height）
- 合約代碼與 ABI
- **Internal Transactions**：合約在執行過程中產生的內部調用（不是用戶直接發起的），可追蹤資金在合約間的流動

---

### 19. 錢包體系

**錢包的本質：**
- 錢包不儲存資產，資產在鏈上；錢包儲存的是**私鑰**
- 私鑰 = 一串大數，透過數學算法保證安全性

**錢包分類（實現原理）：**

```
┌─────────────────────────────────────────────────────┐
│                  Wallet App（使用介面）               │
└──────────────────┬──────────────────────────────────┘
                   │ 使用
      ┌────────────┼────────────┐
      ▼            ▼            ▼
 實現原理分類  多簽錢包實現  托管方式分類
      │            │            │
  EOA錢包      MPC多簽      自託管錢包
 （私鑰錢包）  (gg18/20等)  （用戶持有私鑰）
      │            │            │
  合約錢包     合約多簽      全託管錢包
  (Safe等)   (Safe等)    （如交易所）
      │                         │
  AA錢包                    混合托管錢包
 （帳戶抽象）                （Hybrid）
```

**各類型說明：**

| 類型 | 控制方式 | 特點 |
|------|---------|------|
| EOA 錢包 | 私鑰直接控制 | 最基本，MetaMask 即此類；私鑰丟失 = 資產永久丟失 |
| MPC 錢包 | 私鑰拆分多份（gg18/gg20） | 無單點洩漏風險，適合企業級 |
| 合約錢包（Safe） | 多簽 m/n | 可設交易限額、白名單；代表：Safe |
| AA 錢包（ERC-4337） | 智能帳戶可編程 | 支持 Gas 代付、批量交易、Session Key |

**托管方式：**

| 方式 | 私鑰持有者 | 例子 |
|------|----------|------|
| 自託管 | 用戶自己 | MetaMask |
| 全託管 | 第三方機構 | Coinbase、幣安 |
| 混合托管（Hybrid） | 用戶+機構共同 | MPC 方案 |

**錢包安全三道防線：**

1. **私鑰洩漏防護**
   - 助記詞/私鑰絕不上網、不截圖、不分享
   - Server 端：使用 TEE（Trusted Execution Environment）保護私鑰

2. **簽名欺騙防護**
   - 禁用 `eth_sign`（原始哈希簽名，用戶無法看清簽的是什麼）
   - 使用 EIP-712 結構化簽名，讓用戶看清楚在簽什麼

3. **權限濫用防護**
   - 審查 `approve` 授權額度（不要無限授權）
   - 定期撤銷不用的授權（使用 revoke.cash 等工具）

---

### 20. Web3 交易完整週期

**交易生命週期：**

```
構造（Construct）→ 模擬（Simulate）→ 簽名（Sign）→ 廣播（Broadcast）→ 上鏈（On-chain）→ 確認（Confirm）
```

**交易模擬（Simulate）— 關鍵原則：必須在簽名前進行**

- 在提交交易前驗證執行結果
- 工具：tenderly、alchemy simulate、本地 fork
- 可以預知：Gas 消耗、執行結果、是否 revert

**鏈上數據監聽（Server 端）：**

```
Web3 Block Chain
       │
       │ pull 方式同步數據
       ▼
鏈上數據監聽服務（tc）
       │
       ├──→ 解析每個 block 中的交易和 event
       │          │
       │          ▼
       │    檢測到用戶轉帳
       │          │
       │          ▼
       │    等待 block confirmation ──→ 處理潛在的 reorg 問題
       │          │
       │          ▼
       └──→ KYA/KYT screening（合規篩查）
```

**Block Confirmation 的重要性：**
- 剛上鏈的交易可能因為 **reorg（鏈重組）** 而被回滾
- 通常等待 6～32 個 block 確認後才視為最終（finality）

---

### 21. 支付系統：Web2 vs. Web3

**Web2 支付模型（銀行轉帳）：**

```
用戶
 │ 1. 購物
 ▼
xxx電商平台 ──→ 2. 創建/支付單 ──→ 支付服務(tc) ──→ 3. 獲取支付單信息 ──→ Bank Institution
                                        │                                        │
                                        ◄────────────── 5. callback ─────────────┘
                                        │
 ▲                                      │
 └──────────── 6. 支付成功callback ──────┘
```

**三條核心流程：**
- **請求流**：電商 → 支付服務 → 銀行（3 個對象）
- **資金流**：用戶存款 → 銀行記帳 → 商家帳戶
- **安全檢查**：KYC 身份認證、apiKey 驗證、mfa 驗證

**Web2 的信任來源：** 信任機構後端（Bank Institution）

**Web3 支付的抽象替換：**
- Bank Institution → Web3 Block Chain
- Different Chain ≈ Different Banks（L1 / L2 可理解為不同銀行）

**Web3 的信任來源：**

| 機制 | 說明 |
|------|------|
| 透明性（Transparency） | 所有交易公開可查 |
| 不可篡改性（Immutability） | 已確認交易無法更改 |
| 共識機制（Consensus） | PoW / PoS 保證交易真實性 |
| 私鑰簽名（Private Key Signing） | 密碼學保證身份 |

---

## Part III — AI × Web3 交叉

### 22. AI Agent 在鏈上的設計

**核心原則：**
- AI 可執行：生成、解釋、分析、模擬
- 人必須確認：簽名、授權（approve）、轉帳、合約寫入

**確認節點設計模式：**

```
AI 生成方案
     │
     ▼
人工審查（Review） ← 最重要的節點
     │
     ▼（確認後）
錢包簽名確認
     │
     ▼
鏈上執行
     │
     ▼
區塊瀏覽器驗證
```

**一個相對穩的 AI × Web3 Agent 架構：**

1. 用戶提出目標和約束
2. Agent 讀取上下文並生成計劃
3. 系統把計劃拆成只讀步驟和候選寫入步驟
4. 只讀工具自動執行，寫入工具進入 policy 檢查
5. Simulation 展示鏈上影響
6. 用戶確認高風險動作
7. Wallet / Smart Account 執行
8. 日誌記錄每一步和最終狀態

> 最危險的設計：讓 Agent 同時擁有模糊目標、廣泛工具、長期記憶和大額資產權限。

---

### 23. Session Key

**定義：** 在帳戶抽象（ERC-4337）框架下，一種授予 AI Agent 有限執行權限的機制。

**工作方式：**
- 主帳戶（用戶控制）生成一個 Session Key
- Session Key 只能執行特定操作（如：只能轉帳給白名單地址、只能在限額內操作）
- Session Key 有時間限制（如 24 小時後自動失效）

**對 AI Agent 的意義：**
- Agent 持有 Session Key，可以在授權範圍內自主執行，不需每次確認
- 但 Session Key 範圍設計不當，仍可能被濫用

---

### 24. AI 生成 Solidity 的注意事項

**已知風險類型：**
- 整數溢出（現代 Solidity ≥ 0.8 已有保護）
- 重入攻擊（Reentrancy）
- 訪問控制缺失（Missing Access Control）
- 隨機數可預測（Block-based randomness）
- 幻覺：AI 可能生成不存在的函數、錯誤的 ABI

**快速審查工具：**
- **Slither**：靜態分析工具（Trail of Bits 出品）
- **MythX**：自動化安全掃描
- **OpenZeppelin**：使用經過審計的標準合約，避免從零寫起

---

### 25. AI × Web3 角色分工

| 任務 | AI 做 | 人做 |
|------|-------|------|
| 合約生成 | 生成 Solidity 草稿 | 審查、測試、審計 |
| 交易構造 | 生成交易參數 | 驗證、模擬、簽名 |
| 安全分析 | 初步漏洞掃描 | 最終判斷 |
| 鏈上讀取 | 查詢、解析數據 | 核實結果 |
| 鏈上寫入 | 準備 calldata | **必須人工確認** |

---

## Part IV — 安全

### 26. 安全邊界原則

**三條必知的安全邊界：**

**1. 地址 ≠ 匿名**
- 區塊鏈地址是「假名（Pseudonymous）」，不是「匿名（Anonymous）」
- 所有交易紀錄公開，透過鏈路分析（Chain Analysis）可以追蹤身份
- KYA/KYT（Know Your Address / Know Your Transaction）是合規工具

**2. 簽名 ≠ 普通登入**
- Web3 簽名授權的後果可能包括：授權轉移資產、批准合約代為操作
- 惡意網站可以偽裝成「只是登入」，實際上讓你簽了資產轉移授權
- 簽名前必須確認：簽的是什麼？給誰？有什麼後果？

**3. 授權 ≠ 轉帳**
- `approve` 操作：允許某合約代你操作你的代幣（ERC-20）
- 「授權」本身不轉錢，但授權後合約可以在任何時候執行 `transferFrom`
- 應避免無限授權（`type(uint256).max`）

**AI Agent 安全原則：**
- AI Agent **絕對不能接觸私鑰或助記詞**
- 涉及簽名、授權、轉帳、合約寫入的操作**保留人工確認**
- 在測試網驗證後才在主網執行
- 提交材料中**不能包含真實助記詞/私鑰截圖**

**AI 應用安全（OWASP Top 10 for LLM 重點）：**
- Prompt Injection：惡意輸入讓模型忽略原始規則
- 過度代理（Excessive Agency）：賦予 Agent 超出必要的工具或權限
- 敏感信息洩露：模型輸出包含私鑰、密碼、內部數據

**Server 端錢包安全：**
- **資金量拆分**：Hot Wallet 只存少量運營資金
- **私鑰保護**：使用 TEE（Trusted Execution Environment），私鑰無任何暴露
- **安全屬於 Web3 的核心要素**：不是可以事後加入的插件

---

## 27. 術語速查表

| 術語 | 英文 | 定義 |
|------|------|------|
| 大型語言模型 | LLM (Large Language Model) | 在大規模文本上訓練的神經網路，透過預測下一 token 生成文字 |
| Token | Token | LLM 處理文字的最小單位（tokenizer 切分後的 segment） |
| 上下文窗口 | Context Window | 模型一次能處理的最大 token 數量 |
| 幻覺 | Hallucination | LLM 生成的聽起來合理但實際錯誤的內容 |
| 系統提示 | System Prompt | 定義模型行為基調的前置指令 |
| 溫度 | Temperature | 控制 LLM 輸出隨機性的參數（0=確定，1=隨機） |
| 工具調用 | Tool Use / Function Calling | 讓模型呼叫外部 API 或函數的能力 |
| 提示詞 | Prompt | 把任務目標、邊界、輸出格式寫成可執行的溝通協議 |
| 提示詞注入 | Prompt Injection | 通過輸入讓模型忽略原始規則或調用危險工具的攻擊方式 |
| 結構化輸出 | Structured Output | 讓模型按固定 JSON schema 返回結果 |
| 上下文 | Context | 模型這一次能看到的全部信息空間 |
| 上下文工程 | Context Engineering | 設計信息進入模型方式的工程方法 |
| 記憶 | Memory | 跨請求保留的信息（偏好、歷史任務） |
| 嵌入 | Embedding | 把文本映射成向量，用來衡量語義相近度 |
| Transformer | Transformer | 現代 LLM 的核心架構，通過 attention 關注上下文 |
| 檢索增強生成 | RAG (Retrieval-Augmented Generation) | 把外部知識取回交給模型使用，減少幻覺和過期知識 |
| 向量數據庫 | Vector DB | 存儲 embedding 並按相似度檢索的數據庫 |
| 引用 | Citation | 把答案裡的結論連接回來源，讓用戶可驗證 |
| 代理 | Agent | 具備規劃、記憶、工具調用能力的自主 AI 系統 |
| 護欄 | Guardrails | 限制 Agent 行為範圍的安全過濾機制 |
| 反思 | Reflection | Agent 檢查中間結果並修正下一步的能力 |
| 多 Agent 系統 | Multi-Agent | 多個 Agent 分工協作的架構 |
| 任務移交 | Handoff | Multi-agent 系統中任務從一個 Agent 移交給另一個 |
| 模型上下文協議 | MCP (Model Context Protocol) | 標準化 AI 與外部工具連接的協議 |
| 推理服務 | Inference | 把訓練好的模型變成可被應用調用的服務 |
| 量化 | Quantization | 降低模型精度（FP16→INT8）以減少顯存和計算需求 |
| 評估 | Evaluation (Eval) | 用明確樣本和指標判斷 AI 系統是否真的變好了 |
| 回歸測試集 | Regression Set | 防止舊問題復發的固定測試樣本集 |
| 可觀測性 | Observability | 線上觀察系統行為（輸入、輸出、工具調用、錯誤）的能力 |
| 微調 | Fine-tuning | 在預訓練模型上繼續訓練以適配特定任務或格式 |
| 監督微調 | SFT (Supervised Fine-Tuning) | 用輸入-輸出樣本讓模型學習特定任務 |
| 低秩適配 | LoRA (Low-Rank Adaptation) | 參數高效微調方法，不更新全部參數 |
| AI 輔助編程 | Vibe Coding | 人和 AI Coding Agent 共同迭代軟件的工作方式 |
| 外部帳戶 | EOA (Externally Owned Account) | 由私鑰控制的以太坊基本帳戶 |
| 帳戶抽象 | AA (Account Abstraction) | ERC-4337 標準，讓合約帳戶具備 EOA 的使用體驗 |
| 多方計算 | MPC (Multi-Party Computation) | 私鑰拆分成多份分散保管的技術 |
| 助記詞 | Mnemonic / Seed Phrase | 12/24 個單詞，可恢復整個錢包的主密鑰 |
| 私鑰 | Private Key | 控制帳戶的密碼學秘密，唯一且不可逆 |
| 簽名 | Signature | 用私鑰對信息簽名，證明身份與授權 |
| Gas | Gas | 以太坊交易的計算費用單位 |
| Nonce | Nonce | 確保交易唯一性的序號（以太坊帳戶模型） |
| Calldata | Calldata | 交易中攜帶的數據，決定合約執行的函數與參數 |
| 智能合約 | Smart Contract | 部署在區塊鏈上的自執行代碼 |
| 代理模式 | Proxy Pattern | 將合約邏輯與入口分離，實現可升級合約的設計模式 |
| 重入攻擊 | Reentrancy Attack | 合約在完成狀態更新前被外部調用再次進入的漏洞 |
| ERC-20 | ERC-20 | 以太坊同質化代幣標準（如 USDC） |
| ERC-721 | ERC-721 | 以太坊非同質化代幣標準（NFT） |
| ERC-4337 | ERC-4337 | 以太坊帳戶抽象標準 |
| UTXO | UTXO (Unspent Transaction Output) | Bitcoin 的帳戶模型，每筆資金只能使用一次 |
| 鏈重組 | Reorg (Chain Reorganization) | 最長鏈規則導致的交易回滾現象 |
| 最終性 | Finality | 交易被確認為永久不可逆的狀態 |
| 測試網 | Testnet | 不含真實價值的測試環境（如 Sepolia） |
| 區塊瀏覽器 | Block Explorer | 查詢鏈上數據的工具（如 Etherscan） |
| KYC | KYC (Know Your Customer) | 用戶身份驗證流程 |
| KYA/KYT | KYA/KYT | 地址/交易合規篩查工具 |
| 多簽 | Multi-sig | 需要多個簽名才能執行操作的安全機制 |
| 授權 | Approve | ERC-20 中允許合約代為操作代幣的操作 |
| 交易模擬 | Simulate | 在提交前預先執行交易以驗證結果 |
| 會話密鑰 | Session Key | ERC-4337 中授予 Agent 有限且有時效的操作權限 |
| 可信執行環境 | TEE (Trusted Execution Environment) | 硬體隔離的可信任計算空間，私鑰無法被外部讀取 |
| PoW / PoS | Proof of Work / Proof of Stake | 區塊鏈共識機制 |
| L1 / L2 | Layer 1 / Layer 2 | L1 是基礎鏈，L2 是建立在 L1 之上的擴展方案 |
| 假名性 | Pseudonymous | 地址公開但不直接綁定真實身份 |
| 狀態圖 | State Graph | LangGraph 等框架中組織 Agent 行為的有向圖 |

---

## 28. Q&A 清單

> 帶 ✅ 表示已掌握

### AI 基礎

1. **LLM 的「幻覺」如何在 Web3 場景下造成具體風險？**
   - AI 可能生成不存在的合約地址、錯誤的函數簽名、虛假的 ABI
   - 後果：交易失敗、資金發送至錯誤地址（不可逆）
   - 對策：所有 AI 生成的地址/函數必須在區塊瀏覽器或官方文件中交叉驗證

2. **context window 有多長？完整合約 ABI 會佔多少 token？**
   - Claude：200K tokens；GPT-4：128K tokens
   - 中等複雜度合約 ABI 約 2,000～10,000 tokens，仍在可用範圍內

3. **temperature 和 max_tokens 如何影響 API 輸出？**
   - temperature 0.1～0.3：適合代碼生成（確定性強）
   - temperature 0.7～1.0：適合創意寫作（多樣性高）
   - max_tokens：控制最大輸出長度，不影響質量

4. **Prompt / Workflow / Agent 在 Web3 場景下哪個風險最高？**
   - Agent 風險最高：可能在無人確認下執行鏈上寫入操作

5. **Prompt Injection 的原理是什麼？如何防範？**
   - 攻擊者通過文檔、網頁或用戶輸入讓模型忽略原始規則或調用危險工具
   - 防範：外部內容標記不可信、工具調用前做參數校驗、敏感動作走 allowlist 和 human approval

6. **什麼是 Context Engineering？為什麼它比「塞更多內容進 prompt」更重要？**
   - Context Engineering 是設計信息進入模型的方式：選源、排序、裁剪、隔離不可信內容
   - 塞滿 context window 不代表模型會正確使用每個細節；信息層級不清楚會導致優先級混亂

7. **RAG 的核心挑戰是什麼？**
   - 不是「接一個向量庫」這麼簡單，而是建立可驗證的證據鏈
   - 三個關鍵判斷：文檔怎麼切、查詢時取什麼、生成時如何引用和拒答

8. **何時應該使用 Fine-tuning？何時不應該？**
   - 應該：已有 eval 確認問題穩定存在，且 prompt/context/schema 都優化過仍不穩定，任務格式/風格需要持續一致
   - 不應該：補實時知識、修權限邊界、替代評估

9. **AI Coding Agent 在 Web3 代碼中的邊界在哪裡？**
   - 可以：生成腳本、解釋 ABI、補測試、修小 bug
   - 不可以：直接上線 AI 生成的合約代碼；合約/簽名/支付腳本必須人工審查 + 測試網驗證

10. **LLM-as-Judge 的局限性是什麼？**
    - Judge 模型也會偏、會漏、會被輸出風格影響
    - 更穩做法：可自動判斷字段用規則評分，開放式質量用 LLM judge，高風險樣本保留人工抽檢

### Web3 基礎

11. **助記詞如何衍生出私鑰和地址？這個過程可逆嗎？**
    - 助記詞 →（BIP-39）→ 種子 →（BIP-44 + ECDSA）→ 私鑰 → 公鑰 →（Keccak-256）→ 地址
    - 完全單向不可逆

12. **簽名和加密的差別？**
    - 簽名：私鑰簽 → 公鑰驗，證明「是我做的」
    - 加密：公鑰加密 → 私鑰解密，保護「別人看不到」

13. **Gas Limit 和 Gas Price 分別是什麼？Gas 不夠時資金會損失嗎？**
    - Gas Limit：願意消耗的最大 Gas 單位數
    - Gas Price：每單位 Gas 的價格（Gwei）
    - Gas 不足：交易 revert，但**已消耗的 Gas 費不退**

14. **智能合約「不可更改」的補救方法（proxy pattern）？**
    - 部署 Proxy 合約（儲存狀態，邏輯指向 Implementation）
    - 升級時只需部署新 Implementation，Proxy 指針更新
    - 注意：Proxy 的 upgrade 權限本身必須嚴格管理

15. **ERC-4337 帳戶抽象和傳統 EOA 的最大差別？對 AI Agent 的意義？**
    - EOA：私鑰直接控制，無法編程
    - AA：智能合約帳戶，可設規則（限額、白名單、Session Key）
    - AI Agent 意義：透過 Session Key 讓 Agent 在受限範圍內自主操作

16. **區塊瀏覽器上的「Internal Transactions」是什麼？**
    - 合約執行過程中觸發的內部調用（合約 → 合約）
    - 不是用戶直接發起的，但會影響資金流動

### AI × Web3 交叉

17. **AI Agent 在鏈上操作時如何設計「人工確認節點」？**
    - 讀操作：可以 AI 自主執行
    - 寫操作（交易廣播）：必須人工確認
    - 最佳實踐：顯示預計 Gas、交易影響、目標地址，用戶確認後才簽名

18. **Session Key 如何讓 AI Agent 有限度地執行鏈上操作？**
    - 主帳戶生成 Session Key，限定：操作類型、目標地址白名單、金額上限、有效期
    - Agent 用 Session Key 在限制範圍內操作，主私鑰不暴露

19. **AI 生成的 Solidity 代碼如何快速做安全審查？**
    - 工具：Slither（靜態分析）、MythX（自動化審計）
    - 使用 OpenZeppelin 標準合約替代從零自寫
    - 人工檢查：訪問控制、重入保護、整數邊界

20. **Evaluation 在 AI × Web3 場景中為什麼比普通 AI 應用更重要？**
    - 錯誤可能影響資產、權限、治理判斷和鏈上執行
    - 需要特別評估風險提示是否漏報、工具調用參數是否越界、是否能識別 Prompt Injection

---

## 29. 推薦資源索引

### Module A — AI 基礎

| 材料 | 連結 | 類型 | 優先度 |
|------|------|------|--------|
| What is a Large Language Model? | [YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 影片 | ★★★ |
| Hugging Face LLM Course Chapter 1 | [huggingface.co](https://huggingface.co/learn/llm-course/chapter1/1) | 文章 | ★★★ |
| Anthropic: Building with the Claude API | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | 課程 | ★★★ |
| Claude Code 101 | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-code-101) | 教程 | ★★★ |
| Microsoft《AI Agents for Beginners》 | [github.com/microsoft](https://github.com/microsoft/ai-agents-for-beginners) | 課程 | ★★★ |
| Anthropic: Building Effective Agents | [anthropic.com](https://www.anthropic.com/research/building-effective-agents) | 文章 | ★★★ |
| OWASP Top 10 for LLM Applications | [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | 文件 | ★★★ |
| OpenAI Agents SDK | [openai.github.io](https://openai.github.io/openai-agents-python/) | 文件 | ★★☆ |
| LangGraph Overview | [langchain-ai.github.io](https://langchain-ai.github.io/langgraph/) | 文件 | ★★☆ |
| OpenAI Prompt Engineering Guide | [platform.openai.com](https://platform.openai.com/docs/guides/prompt-engineering) | 文件 | ★★☆ |
| OpenAI Structured Outputs | [platform.openai.com](https://platform.openai.com/docs/guides/structured-outputs) | 文件 | ★★☆ |
| OpenAI Fine-tuning Guide | [platform.openai.com](https://platform.openai.com/docs/guides/fine-tuning) | 文件 | ★★☆ |
| OpenAI Evals | [github.com/openai](https://github.com/openai/evals) | 工具 | ★★☆ |
| DSPy Documentation | [dspy-docs.vercel.app](https://dspy-docs.vercel.app/) | 文件 | ★☆☆ |
| Hugging Face PEFT Documentation | [huggingface.co](https://huggingface.co/docs/peft) | 文件 | ★☆☆ |
| Claude Code Overview | [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code/overview) | 文件 | ★★★ |

### Module B — Web3 基礎

| 材料 | 連結 | 類型 | 優先度 |
|------|------|------|--------|
| Ethereum Accounts 文件 | [ethereum.org](https://ethereum.org/en/developers/docs/accounts/) | 文件 | ★★★ |
| MetaMask Getting Started | [support.metamask.io](https://support.metamask.io/getting-started/) | 教程 | ★★★ |
| Remix IDE | [remix.ethereum.org](https://remix.ethereum.org/) | 工具 | ★★★ |
| Sepolia Faucet (Chainlink) | [faucets.chain.link](https://faucets.chain.link/sepolia) | 工具 | ★★★ |
| Ethereum Development Documentation | [ethereum.org/developers](https://ethereum.org/en/developers/docs/) | 文件 | ★★☆ |
| OpenZeppelin Contracts | [docs.openzeppelin.com](https://docs.openzeppelin.com/contracts) | 文件 | ★★☆ |
| ERC-4337 文件 | [docs.erc4337.io](https://docs.erc4337.io/) | 文件 | ★☆☆ |
| Safe Overview | [docs.safe.global](https://docs.safe.global/) | 文件 | ★☆☆ |
| Hardhat | [hardhat.org](https://hardhat.org/docs/getting-started) | 工具 | ★☆☆ |

---

## 30. 交付物 Checklist

### Module A｜AI 基礎
- [ ] 觀看 What is a Large Language Model?（影片）
- [ ] 閱讀 Hugging Face LLM Course Chapter 1
- [ ] 閱讀 Anthropic: Building with the Claude API（Quick Start + Tool Use）
- [x] 取得 API Key，跑通第一個 LLM API 請求（含截圖）
- [x] 安裝並設定 Learning Agent 工具（Claude Code / Codex / Hermes）
- [ ] 閱讀 Microsoft《AI Agents for Beginners》前三章
- [x] 完成至少一次對話式學習任務（用 agent 整理 Week 1 大綱）
- [ ] 閱讀 Anthropic: Building Effective Agents

### Module B｜Web3 基礎
- [x] 閱讀 Ethereum Accounts 文件
- [x] 創建測試錢包，能說明地址、助記詞、私鑰的區別與安全責任
- [x] 切換至 Sepolia 測試網，領取測試幣
- [x] 發送一筆測試交易，記錄：交易哈希、狀態、Gas、區塊高度
- [x] 在 Remix IDE 部署最小智能合約，完成讀取 + 寫入操作

### Module C｜AI × Web3 交叉實驗
- [ ] 讓 AI 生成 SimpleStorage 合約說明與部署步驟
- [ ] 人工複核 AI 輸出，標記不可靠部分
- [ ] 在測試網執行，在區塊瀏覽器驗證
- [ ] 畫出「AI 生成 → 人工複核 → 錢包確認 → 鏈上執行 → 驗證」流程圖

### 安全意識確認
- [ ] 能說清楚：地址 ≠ 匿名、簽名 ≠ 普通登入、授權 ≠ 轉帳
- [ ] 確認 AI Agent 不直接接觸私鑰／助記詞
- [ ] 提交材料中不包含真實助記詞／私鑰截圖

### Eval 與工程實踐
- [ ] 為一個 AI 原型準備最小 Golden Set（30 條樣本）
- [ ] 實作一個最小 Harness（可重複運行的 eval 流程）
- [ ] 記錄一次 Prompt 修改前後的 eval 差異

### GitHub Repo 與交付
- [x] GitHub Repo 初始化（README、notes/、prompts/、demos/、logs/、resources.md）
- [ ] 提交 Learning Agent 設定記錄
- [ ] 提交可互動學習產物（quiz / 流程圖 / 概念卡片）到 demos/
- [ ] 整理「行業觀察清單」（信息源 + 3-5 條高品質內容觀察筆記）

---

*最後更新：2026-05-20*
