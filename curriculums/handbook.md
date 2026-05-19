# AIxWeb3 School — Week 1 Handbook
> 課程期間：2026-05-18 ～ 2026-05-22｜本手冊綜合課程計畫、講座筆記與圖解，作為學習全程參考手冊

---

## 目錄

1. [核心思維框架](#1-核心思維框架)
2. [AI 基礎知識](#2-ai-基礎知識)
3. [Web3 基礎知識](#3-web3-基礎知識)
4. [錢包體系詳解](#4-錢包體系詳解)
5. [Web3 交易完整週期](#5-web3-交易完整週期)
6. [支付系統：Web2 vs. Web3 對比](#6-支付系統web2-vs-web3-對比)
7. [AI × Web3 交叉概念](#7-ai--web3-交叉概念)
8. [安全邊界原則](#8-安全邊界原則)
9. [術語速查表（Glossary）](#9-術語速查表glossary)
10. [Q&A 清單](#10-qa-清單)
11. [推薦資源索引](#11-推薦資源索引)
12. [本週交付物 Checklist](#12-本週交付物-checklist)

---

## 1. 核心思維框架

### AI 時代的人機分工

> 來源：0518 講座「AI時代，Web3開發者所需的能力」

**AI 的角色：**
- 協助人設計方案（細化方案、補足缺失、有效快速執行）

**人的角色：**
- 設計方案的決策者
- AI 輸出的審查者（Reviewer）
- 涉及資金、簽名、授權的最終確認者

**關鍵認知：AI 並未降低系統的複雜度，只是放大了個人的執行能力。**

| 維度 | AI 的變化 | 不變的事 |
|------|----------|---------|
| 個人能力 | Coding 更快，個人能力被放大 | 系統本身的複雜度 |
| 錯誤責任 | AI 可生成代碼 | 錯誤成本由人承擔 |
| 安全控制 | AI 可輔助分析 | 安全邊界必須由人守住 |

**結論：駕馭 AI，而不是被 AI 驅動。**

### Web2 與 Web3 並非互斥

- Web3 產品中，Web2 的佔比仍很大（前端頁面、後端管理服務缺一不可）
- Web3 = 在信任層（Trust Layer）上以區塊鏈取代傳統機構後端

---

## 2. AI 基礎知識

### 2.1 LLM（Large Language Model）

**定義：** 在大規模文本語料上訓練的神經網路模型，透過預測下一個 token 來生成語言。

**工作方式：**
- 輸入文字被切分為 **token**（通常 1 token ≈ 0.75 個英文單詞或 1 個中文字）
- 模型根據上下文（context window 中的全部 token）計算概率，逐一輸出下一個 token
- 生成是「自回歸」的（autoregressive）：每次生成的 token 會加入下一步的上下文

**四個控制層面：**

| 控制層面 | 說明 | 對應參數/機制 |
|---------|------|--------------|
| 角色設定 | 定義模型身份與行為基調 | System Prompt |
| 輸出控制 | 影響輸出的隨機性與長度 | `temperature`、`max_tokens` |
| 知識邊界 | 模型訓練截止日期內的知識 | Knowledge Cutoff |
| 工具能力 | 賦予模型呼叫外部工具的能力 | Tool Use / Function Calling |

**重要限制：**
- **Context Window**：模型一次能處理的最大 token 數量（如 Claude 200K tokens）；超出後早期內容會被截斷或遺忘
- **幻覺（Hallucination）**：模型可能生成聽起來合理但實際錯誤的內容，在 Web3 場景（如合約地址、函數簽名）中風險極高
- **Temperature**：數值越高（如 1.0），輸出越多樣/創意；數值越低（如 0.1），輸出越確定/保守。代碼生成建議用低 temperature（0.1～0.3）

### 2.2 Prompt / Workflow / Agent 差異

| 維度 | Prompt | Workflow | Agent |
|------|--------|----------|-------|
| 結構 | 單次輸入 → 輸出 | 固定步驟串聯 | 動態決策 + 工具調用循環 |
| 自主性 | 無 | 低 | 高 |
| 狀態管理 | 無狀態 | 有限狀態 | 持久狀態（Memory） |
| 錯誤風險 | 最低 | 中 | 最高（Web3 場景） |
| 典型工具 | API 直接調用 | LangGraph、n8n | OpenAI Agents SDK、Claude Code |

**Web3 場景風險排序：** Agent > Workflow > Prompt
（Agent 可能在無人確認下執行鏈上操作）

### 2.3 AI Agent 核心組件

```
┌─────────────────────────────────────────────────┐
│                   AI Agent                       │
│                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │  Memory  │  │ Planning │  │  Tool Use    │  │
│  │（記憶層） │  │（規劃層） │  │（工具調用）  │  │
│  └──────────┘  └──────────┘  └──────────────┘  │
│                                                 │
│  ┌────────────────────────────────────────────┐ │
│  │            Guardrails（安全護欄）           │ │
│  └────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

**關鍵概念：**
- **Memory**：跨 session 的記憶能力（短期 context + 長期存儲）
- **Planning**：任務拆解與執行規劃（ReAct 模式：Reason → Act → Observe）
- **Tool Use / Function Calling**：讓模型呼叫外部 API、搜尋、執行代碼
- **Handoff**：Agent 之間的任務移交（multi-agent 系統）
- **Guardrails**：輸入/輸出的安全過濾層，防止有害或異常操作

### 2.4 MCP（Model Context Protocol）

**定義：** Anthropic 提出的標準協議，讓 AI 模型可以安全、標準化地與外部工具、數據源連接。

**與傳統 API 的本質差異：**
- 傳統 API：開發者在代碼中硬編碼調用邏輯
- MCP：模型動態發現並調用工具，工具的能力描述由 MCP Server 提供，模型自主選擇

### 2.5 AI Coding 工具

| 工具 | 定位 | 特點 |
|------|------|------|
| Claude Code | CLI + IDE 整合 | Anthropic 官方，深度代碼理解 |
| Codex CLI | 命令列工具 | OpenAI 出品，適合腳本自動化 |
| Hermes Agent | 開源 Agent 框架 | Nous Research，支持 skills 與跨 session 記憶 |

---

## 3. Web3 基礎知識

### 3.1 帳戶（Account）

**以太坊帳戶類型：**

| 類型 | 全名 | 控制方式 | 特點 |
|------|------|---------|------|
| EOA | Externally Owned Account | 私鑰 | 最基本的帳戶，無代碼 |
| 合約帳戶 | Contract Account | 代碼邏輯 | 由 EOA 或其他合約觸發 |

**地址的本質：**
- 助記詞（Mnemonic）→（BIP-39）→ 種子（Seed）→（BIP-44 HD Wallet）→ 私鑰（Private Key）→（橢圓曲線 ECDSA）→ 公鑰（Public Key）→（Keccak-256 Hash）→ 地址（Address）
- 此過程**單向不可逆**：知道地址無法反推私鑰

### 3.2 簽名（Signing）

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

### 3.3 交易（Transaction）

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

### 3.4 智能合約（Smart Contract）

**定義：** 部署在區塊鏈上的自執行代碼，觸發條件滿足時自動執行，任何人可驗證。

**不可更改性（Immutability）：** 合約代碼一旦部署，邏輯無法修改。
- **補救方法：Proxy Pattern**（代理模式）
  - 將合約拆成「Proxy（入口）+ Implementation（邏輯）」
  - 升級時只部署新的 Implementation，Proxy 的地址不變
  - 缺點：增加複雜度，需要嚴格的 upgrade 權限管理

**常見合約標準（OpenZeppelin）：**
- **ERC-20**：同質化代幣標準（如 USDC、DAI）
- **ERC-721**：非同質化代幣標準（NFT）
- **ERC-4337**：帳戶抽象標準（Account Abstraction，見下）

### 3.5 Gas 與費用

```
gas fee = gas count × gas price
```

- Gas **不足**：交易 revert（失敗），已消耗的 gas 費不退
- Gas **過多**：多餘的 gas 退回給發送者
- 設定 Gas Limit 的原則：略高於估算值（留 10-20% 餘量）

### 3.6 L1 vs. L2

| 維度 | L1（如以太坊主網） | L2（如 Optimism、Arbitrum） |
|------|-----------------|--------------------------|
| 安全性 | 最高（原生共識） | 繼承 L1 安全 |
| 交易速度 | 較慢（~12s/block） | 更快 |
| Gas 費用 | 較高 | 顯著降低 |
| 測試網 | Sepolia（ETH L1 測試網） | 各 L2 有對應測試網（如 Optimism Sepolia） |

### 3.7 區塊瀏覽器（Block Explorer）

用於查詢鏈上所有公開資訊的工具（如 Sepolia Etherscan）。

**可查詢的資訊：**
- 交易哈希（Tx Hash）
- 交易狀態（Success / Failed）
- Gas 使用量與費用
- 區塊高度（Block Height）
- 合約代碼與 ABI
- **Internal Transactions**：合約在執行過程中產生的內部調用（不是用戶直接發起的），可追蹤資金在合約間的流動

---

## 4. 錢包體系詳解

> 來源：0518 講座 + lecture_0518_3.jpg

### 4.1 錢包的本質

錢包在 Web3 中扮演的是用戶的**「身份」**及**「資產管理」**入口。
- 錢包不儲存資產，資產在鏈上；錢包儲存的是**私鑰**
- 私鑰 = 一串大數，透過數學算法保證安全性

### 4.2 錢包分類（實現原理）

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

### 4.3 各類型說明

**EOA 錢包（Externally Owned Account）：**
- 用私鑰直接控制
- 最基本，MetaMask 即此類
- 缺點：私鑰丟失 = 資產永久丟失

**MPC 錢包（Multi-Party Computation）：**
- 私鑰拆分成多份，分散保存（gg18/gg20 算法）
- 無單點私鑰洩漏風險
- 適合企業級應用

**合約錢包（Smart Contract Wallet）：**
- 代表：Safe（前身 Gnosis Safe）
- 支持多簽（Multi-sig）：需要 m/n 個簽名才能執行
- 可設置交易限額、白名單等規則

**AA 錢包（Account Abstraction，ERC-4337）：**
- 結合 EOA 靈活性 + 智能帳戶可編程性
- 支持 Gas 代付（Paymaster）、批量交易、Session Key 等
- 對 AI Agent 意義重大：可以給 Agent 有限的執行權限（Session Key）

**托管方式：**
| 方式 | 私鑰持有者 | 安全責任 | 例子 |
|------|----------|---------|------|
| 自託管 | 用戶自己 | 用戶完全負責 | MetaMask |
| 全託管 | 第三方機構 | 機構負責 | Coinbase、幣安 |
| 混合托管（Hybrid） | 用戶+機構共同 | 分擔 | MPC 方案 |

### 4.4 錢包安全三道防線

1. **私鑰洩漏防護**
   - 助記詞/私鑰絕不上網、不截圖、不分享
   - Server 端：使用 TEE（Trusted Execution Environment）可信任空間保護私鑰，無任何暴露

2. **簽名欺騙防護**
   - 禁用 `eth_sign`（原始哈希簽名，用戶無法看清簽的是什麼）
   - 提升簽名可視性（使用 EIP-712 結構化簽名，讓用戶看清楚在簽什麼）

3. **權限濫用防護**
   - 審查 `approve` 授權額度（不要無限授權）
   - 定期撤銷不用的授權（使用 revoke.cash 等工具）

---

## 5. Web3 交易完整週期

### 5.1 交易生命週期

```
構造（Construct）→ 模擬（Simulate）→ 簽名（Sign）→ 廣播（Broadcast）→ 上鏈（On-chain）→ 確認（Confirm）
```

### 5.2 交易模擬（Simulate）

> 關鍵原則：**必須在簽名前進行模擬**

- 在提交交易前驗證執行結果
- 工具：tenderly、alchemy simulate、本地 fork
- 可以預知：Gas 消耗、執行結果、是否 revert

### 5.3 鏈上數據監聽（Server 端）

> 來源：lecture_0518_4.jpg

```
Web3 Block Chain
       │
       │ 3 pull 方式同步數據
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
       │          │              └──→ 一般等待 block 數量（鏈長度足夠）
       │          ▼
       └──→ kya/kyt screening（合規篩查）
```

**Block Confirmation 的重要性：**
- 剛上鏈的交易可能因為 **reorg（鏈重組）** 而被回滾
- 通常等待 6～32 個 block 確認後才視為最終（finality）

---

## 6. 支付系統：Web2 vs. Web3 對比

> 來源：0518 講座 + lecture_0518_1.jpg & lecture_0518_2.jpg

### 6.1 Web2 支付模型（銀行轉帳）

```
用戶
 │ 1. 購物
 ▼
xxx電商平台 ──→ 2. 創建/支付單 ──→ 支付服務(tc) ──→ 3. 獲取支付單信息 ──→ Bank Institution
                                        │                                        │
                                        ◄────────────── 5. callback ─────────────┘
                                        │         （收到支付單信息）
 ▲                                      │
 └──────────── 6. 支付成功callback ──────┘
                （7. 訂單狀態流轉）
```

**三條核心流程：**
- **請求流**：支付是怎麼完成的？（電商 → 支付服務 → 銀行，共 3 個對象）
- **資金流**：錢是怎麼流轉的？（用戶存款 → 銀行記帳 → 商家帳戶）
- **安全檢查**：KYC 身份認證、服務間 apiKey 驗證、mfa 驗證、服務間信任（防篡改）

**Web2 的信任來源：** 信任機構後端（Bank Institution）

### 6.2 Web3 支付擴展（引入穩定幣）

**抽象替換：**
- Bank Institution → Web3 Block Chain
- Different Chain ≈ Different Banks（L1 / Layer2 可理解為不同銀行）

**Web3 的信任來源：**
- **透明性（Transparency）**：所有交易公開可查
- **不可篡改性（Immutability）**：已確認交易無法更改
- **共識機制（Consensus）**：PoW / PoS 保證交易真實性
- **私鑰簽名（Private Key Signing）**：密碼學保證身份

**Web3 支付流程的差異：**
```
web3 用戶
 │ 2. 支付 USDC
 ▼
Web3 order 支付信息（deposit account）
 │ 交易記錄在鏈上
 ▼
Web3 Block Chain
 │ 3 pull 方式同步數據
 ▼
鏈上數據監聽服務（tc） ──→ 4. 收到資金（檢測到存在向 deposit account 的轉帳）
 │
 ▼
鏈上數據監聽服務（tc）
 │ 1. 對每個 order 訂算 deposit account，並開始通知用戶
```

---

## 7. AI × Web3 交叉概念

### 7.1 AI Agent 在鏈上的人工確認設計

**核心原則：**
- AI 可執行：生成、解釋、分析、模擬
- 人必須確認：簽名、授權（approve）、轉帳、合約寫入

**確認節點設計模式：**

```
AI 生成方案
     │
     ▼
人工審查（Review）← 這是最重要的節點
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

### 7.2 Session Key（會話密鑰）

**定義：** 在帳戶抽象（ERC-4337）框架下，一種授予 AI Agent 有限執行權限的機制。

**工作方式：**
- 主帳戶（用戶控制）生成一個 Session Key
- Session Key 只能執行特定操作（如：只能轉帳給白名單地址、只能在限額內操作）
- Session Key 有時間限制（如 24 小時後自動失效）

**對 AI Agent 的意義：**
- AI Agent 持有 Session Key，可以在授權範圍內自主執行，不需每次都打擾用戶確認
- 但一旦 Session Key 的範圍設計不當，仍可能被濫用

### 7.3 AI 生成 Solidity 代碼的注意事項

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

### 7.4 AI × Web3 的角色分工總結

| 任務 | AI 做 | 人做 |
|------|-------|------|
| 合約生成 | 生成 Solidity 草稿 | 審查、測試、審計 |
| 交易構造 | 生成交易參數 | 驗證、模擬、簽名 |
| 安全分析 | 初步漏洞掃描 | 最終判斷 |
| 鏈上讀取 | 查詢、解析數據 | 核實結果 |
| 鏈上寫入 | 準備 calldata | **必須人工確認** |

---

## 8. 安全邊界原則

### 三條必知的安全邊界

> 來源：0518 講座

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

### AI Agent 安全原則

- AI Agent **絕對不能接觸私鑰或助記詞**
- 涉及簽名、授權、轉帳、合約寫入的操作**保留人工確認**
- 在測試網驗證後才在主網執行
- 提交材料中**不能包含真實助記詞/私鑰截圖**

### Server 端錢包安全

- **資金量拆分**：減少單點風險（Hot Wallet 只存少量運營資金）
- **私鑰保護**：使用 TEE（Trusted Execution Environment）可信任空間，私鑰無任何暴露
- **安全屬於 Web3 的核心要素**：不是可以事後加入的插件

---

## 9. 術語速查表（Glossary）

| 術語 | 英文 | 定義 |
|------|------|------|
| 大型語言模型 | LLM (Large Language Model) | 在大規模文本上訓練的神經網路，透過預測下一 token 生成文字 |
| Token | Token | LLM 處理文字的最小單位，約 0.75 個英文單詞或 1 個中文字 |
| 上下文窗口 | Context Window | 模型一次能處理的最大 token 數量 |
| 幻覺 | Hallucination | LLM 生成的聽起來合理但實際錯誤的內容 |
| 系統提示 | System Prompt | 定義模型行為基調的前置指令 |
| 溫度 | Temperature | 控制 LLM 輸出隨機性的參數（0=確定，1=隨機） |
| 工具調用 | Tool Use / Function Calling | 讓模型呼叫外部 API 或函數的能力 |
| 代理 | Agent | 具備規劃、記憶、工具調用能力的自主 AI 系統 |
| 護欄 | Guardrails | 限制 Agent 行為範圍的安全過濾機制 |
| 模型上下文協議 | MCP (Model Context Protocol) | 標準化 AI 與外部工具連接的協議 |
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
| 同質化代幣 | Fungible Token | 每單位完全相同可互換的代幣（如貨幣） |
| 非同質化代幣 | NFT (Non-Fungible Token) | 每個唯一不可替換的數位資產 |
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
| Session Key | Session Key | ERC-4337 中授予 Agent 有限且有時效的操作權限 |
| TEE | TEE (Trusted Execution Environment) | 硬體隔離的可信任計算空間，私鑰無法被外部讀取 |
| PoW / PoS | Proof of Work / Proof of Stake | 區塊鏈共識機制 |
| L1 / L2 | Layer 1 / Layer 2 | L1 是基礎鏈，L2 是建立在 L1 之上的擴展方案 |
| 假名性 | Pseudonymous | 地址公開但不直接綁定真實身份 |
| 工作流 | Workflow | 固定步驟串聯的自動化流程（介於 Prompt 與 Agent 之間） |
| 狀態圖 | State Graph | LangGraph 等框架中組織 Agent 行為的有向圖 |
| Handoff | Handoff | Multi-agent 系統中任務從一個 Agent 移交給另一個 |

---

## 10. Q&A 清單

> 本節為學習過程中應逐一釐清的問題，帶 ✅ 表示已掌握

### LLM 與 AI 基礎

1. **LLM 的「幻覺」（hallucination）如何在 Web3 場景下造成具體風險？**
   - AI 可能生成不存在的合約地址、錯誤的函數簽名、虛假的 ABI
   - 後果：交易失敗、資金發送至錯誤地址（不可逆）
   - 對策：所有 AI 生成的地址/函數必須在區塊瀏覽器或官方文件中交叉驗證

2. **上下文窗口（context window）有多長？一份完整的智能合約 ABI 放進去會佔多少 token？**
   - Claude：200K tokens；GPT-4：128K tokens
   - 一份中等複雜度合約 ABI 約 2,000～10,000 tokens，仍在可用範圍內

3. **temperature 和 max_tokens 如何影響 API 輸出？**
   - temperature 0.1～0.3：適合代碼生成（確定性強）
   - temperature 0.7～1.0：適合創意寫作（多樣性高）
   - max_tokens：控制最大輸出長度，不影響質量

4. **Prompt / Workflow / Agent 在 Web3 場景下哪個風險最高？**
   - Agent 風險最高：可能在無人確認下執行鏈上寫入操作

5. **AI Coding 工具生成的 Solidity 代碼有多可靠？**
   - 常見錯誤類型：重入漏洞、訪問控制缺失、整數邊界問題
   - 對策：不直接使用，必須用 Slither 掃描 + 人工審查

6. **MCP（Model Context Protocol）是什麼？**
   - 標準化協議，讓模型動態發現並調用外部工具
   - 差異：傳統 API 硬編碼，MCP 模型自主選擇工具

7. **Guardrails 如何實作？**
   - 輸入過濾：檢查 prompt 是否包含危險指令
   - 輸出過濾：確認 Agent 的行動符合預定規則
   - 工具：NeMo Guardrails（NVIDIA）、Lakera Guard

8. **Agent 的「狀態管理」和傳統後端的 session 管理有什麼異同？**
   - 相同：都維護某段時間內的上下文狀態
   - 不同：Agent 狀態可能跨工具調用持久化；傳統 session 通常只在請求週期內有效

### Web3 基礎

9. **助記詞如何衍生出私鑰和地址？這個過程可逆嗎？**
   - 助記詞 →（BIP-39）→ 種子 →（BIP-44 + ECDSA）→ 私鑰 → 公鑰 →（Keccak-256）→ 地址
   - 完全單向不可逆

10. **簽名和加密的差別？**
    - 簽名：私鑰簽 → 公鑰驗，證明「是我做的」
    - 加密：公鑰加密 → 私鑰解密，保護「別人看不到」

11. **Gas Limit 和 Gas Price 分別是什麼？Gas 不夠時資金會損失嗎？**
    - Gas Limit：願意消耗的最大 Gas 單位數
    - Gas Price：每單位 Gas 的價格（Gwei）
    - Gas 不足：交易 revert，但**已消耗的 Gas 費不退**（不是主要資金，但手續費損失）

12. **Sepolia 是 L1 測試網嗎？L2 有對應的測試網嗎？**
    - Sepolia：是以太坊 L1 的測試網
    - L2 測試網舉例：Optimism Sepolia、Arbitrum Sepolia、Base Sepolia

13. **智能合約「不可更改」的補救方法（proxy pattern）？**
    - 部署 Proxy 合約（儲存狀態，邏輯指向 Implementation）
    - 升級時只需部署新 Implementation，Proxy 指針更新
    - 注意：Proxy 的 upgrade 權限本身必須嚴格管理

14. **ERC-4337 帳戶抽象和傳統 EOA 的最大差別？對 AI Agent 的意義？**
    - EOA：私鑰直接控制，無法編程
    - AA：智能合約帳戶，可設規則（限額、白名單、Session Key）
    - AI Agent 意義：透過 Session Key 讓 Agent 在受限範圍內自主操作

15. **區塊瀏覽器上的「Internal Transactions」是什麼？**
    - 合約執行過程中觸發的內部調用（合約 → 合約）
    - 不是用戶直接發起的，但會影響資金流動
    - 追蹤內部交易對於理解 DeFi 資金流向很重要

### AI × Web3 交叉

16. **AI Agent 在鏈上操作時如何設計「人工確認節點」？**
    - 讀操作：可以 AI 自主執行
    - 寫操作（交易廣播）：必須人工確認
    - 最佳實踐：顯示預計 Gas、交易影響、目標地址，用戶確認後才簽名

17. **Session Key 如何讓 AI Agent 有限度地執行鏈上操作？**
    - 主帳戶生成 Session Key，限定：操作類型、目標地址白名單、金額上限、有效期
    - Agent 用 Session Key 在限制範圍內操作，主私鑰不暴露

18. **AI 生成的 Solidity 代碼如何快速做安全審查？**
    - 工具：Slither（靜態分析）、MythX（自動化審計）
    - 使用 OpenZeppelin 標準合約替代從零自寫
    - 人工檢查：訪問控制、重入保護、整數邊界

19. **如果 AI Agent 在測試網執行了預料外的操作，如何追蹤？**
    - 測試網：在區塊瀏覽器查看所有交易記錄，交易哈希即為完整追蹤線索
    - 主網：同樣可追蹤，但資金損失不可逆 → 嚴格先在測試網驗證

20. **Web3 治理（governance）中，AI 可以扮演什麼角色？**
    - 提案摘要分析、投票模擬、歷史投票模式分析
    - DAO 案例：Snapshot + AI 提案生成；Tally 的 AI 投票助手
    - 但：最終投票決策應由人類持有者確認

---

## 11. 資源索引

### Module A — AI 基礎

| 材料 | 連結 | 類型 | 優先度 |
|------|------|------|--------|
| What is a Large Language Model? | [YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g) | 影片 | ★★★ |
| Hugging Face LLM Course Chapter 1 | [huggingface.co](https://huggingface.co/learn/llm-course/chapter1/1) | 文章 | ★★★ |
| Anthropic: Building with the Claude API | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | 課程 | ★★★ |
| Claude Code 101 | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-code-101) | 教程 | ★★★ |
| Microsoft《AI Agents for Beginners》 | [github.com/microsoft](https://github.com/microsoft/ai-agents-for-beginners) | 課程 | ★★★ |
| OpenAI Agents SDK | [openai.github.io](https://openai.github.io/openai-agents-python/) | 文件 | ★★☆ |
| LangGraph Overview | [langchain-ai.github.io](https://langchain-ai.github.io/langgraph/) | 文件 | ★★☆ |
| Hermes Agent Docs | [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/docs/) | 文件 | ★★☆ |
| Z.ai API 開發者文檔 | [docs.z.ai](https://docs.z.ai/devpack/overview) | 文件 | ★★☆ |

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
| Foundry | [book.getfoundry.sh](https://book.getfoundry.sh/) | 工具 | ★☆☆ |

---

## 12. Checklist

### Module A｜AI 基礎
- [ ] 觀看 What is a Large Language Model?（影片）
- [ ] 閱讀 Hugging Face LLM Course Chapter 1
- [ ] 閱讀 Anthropic: Building with the Claude API（Quick Start + Tool Use）
- [ ] 取得 API Key，跑通第一個 LLM API 請求（含截圖）
- [ ] 安裝並設定 Learning Agent 工具（Claude Code / Codex / Hermes）
- [ ] 閱讀 Microsoft《AI Agents for Beginners》前三章
- [ ] 完成至少一次對話式學習任務（用 agent 整理 Week 1 大綱）

### Module B｜Web3 基礎
- [ ] 閱讀 Ethereum Accounts 文件
- [ ] 創建測試錢包，能說明地址、助記詞、私鑰的區別與安全責任
- [ ] 切換至 Sepolia 測試網，領取測試幣
- [ ] 發送一筆測試交易，記錄：交易哈希、狀態、Gas、區塊高度
- [ ] 在 Remix IDE 部署最小智能合約，完成讀取 + 寫入操作

### Module C｜AI × Web3 交叉實驗
- [ ] 讓 AI 生成 SimpleStorage 合約說明與部署步驟
- [ ] 人工複核 AI 輸出，標記不可靠部分
- [ ] 在測試網執行，在區塊瀏覽器驗證
- [ ] 畫出「AI 生成 → 人工複核 → 錢包確認 → 鏈上執行 → 驗證」流程圖

### 安全意識確認
- [ ] 能說清楚：地址 ≠ 匿名、簽名 ≠ 普通登入、授權 ≠ 轉帳
- [ ] 確認 AI Agent 不直接接觸私鑰／助記詞
- [ ] 提交材料中不包含真實助記詞／私鑰截圖

### GitHub Repo 與交付
- [ ] GitHub Repo 初始化（README、notes/、prompts/、demos/、logs/、resources.md）
- [ ] 提交 Learning Agent 設定記錄
- [ ] 提交可互動學習產物（quiz / 流程圖 / 概念卡片）到 demos/
- [ ] 整理「行業觀察清單」（信息源 + 3-5 條高品質內容觀察筆記）

---

*最後更新：2026-05-19｜整合來源：Week 1 課程計畫 + 0518 講座筆記（Pito Li）+ 講座圖解（lecture_0518_1~4）*
