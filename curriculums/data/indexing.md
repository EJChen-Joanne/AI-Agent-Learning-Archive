### 索引（Indexing）

鏈上數據是公開的，但不等於好用。Indexing 的作用，是把區塊、交易、事件和合約狀態整理成產品、分析工具和 AI Agent 能快速查詢的結構化數據。

#### 為什麼要學這個

一個合約可以發出很多 event，一條鏈每天會產生大量區塊和交易。你當然可以直接通過 RPC 讀取，但如果要做用戶歷史、排行榜、協議看板、風控監控、Agent 上下文，就需要穩定的數據索引層。

Indexing 解決的不是「有沒有數據」，而是「能不能按產品需要快速、準確、可回放地查詢數據」。

鏈上是事實來源，索引層是可用數據層。

#### 第一性原理

產品需要的是面向問題的數據模型，而不是原始區塊流。
區塊鏈按區塊和交易組織數據，用戶和產品卻關心「這個地址的倉位」「這個協議的 TVL」「這個訂單是否成交」「這個 Agent 執行過哪些動作」。索引層負責把底層事實轉換成這些查詢對象。

* 事件是重要入口：合約 event 是索引器構建狀態的主要信號。
* RPC 不是數據庫：RPC 適合讀取鏈狀態和發送交易，不適合承載所有複雜歷史查詢。
* 索引要能重放：合約升級、reorg、bug 修復時，需要從某個區塊重新構建數據。

#### 知識節點

**Event Indexing**

Event Indexing 是監聽合約日誌，把鏈上動作整理成可查詢記錄。

例如合約發出 Transfer、OrderCreated、Deposit、Withdraw、VoteCast，索引器可以把這些 event 轉成數據庫表或搜索索引。前端再查詢「某個用戶所有訂單」或「某個池子的最近存款」。

設計 event 時要考慮後續查詢：

* event 是否包含關鍵地址。
* 是否需要 indexed 參數。
* 是否能從 event 還原業務狀態。
* 失敗交易不會產生成功 event。
* 合約升級後 event 是否兼容。

**相關 topic**

```智能合約（Smart Contract）```：先理解 event 為什麼是合約向外部系統留下的日誌。

**Subgraph**

Subgraph 是用聲明式方式描述如何索引合約事件，並通過 GraphQL 暴露查詢接口。

The Graph 的 subgraph 通常包括三部分：要監聽的合約和事件、事件到實體的 mapping、GraphQL schema。它適合構建協議數據 API，例如 token、pool、swap、position、vote。

Subgraph 的價值是讓開發者不用從零寫整套 indexer。但它仍然需要維護：合約地址變更、事件結構變化、reorg、同步延遲和 schema 設計都會影響數據質量。

**相關 topic**

```The Graph Subgraphs```：了解 subgraph、schema、mapping 和 GraphQL 查詢。

**RPC**

RPC 是應用和節點交互的接口，用來讀取鏈狀態、查詢日誌、估算 gas 和發送交易。

RPC 很重要，但它不是萬能索引服務。你可以用 `eth_call` 讀取當前合約狀態，用 `eth_getLogs` 查詢事件日誌，用 `eth_sendRawTransaction` 廣播交易。但如果你頻繁掃大量歷史日誌，公共 RPC 很容易限流或變慢。

常見 RPC 問題包括：

* rate limit。
* 節點不同步。
* archive 數據不可用。
* 多 RPC 返回不一致。
* 查詢區塊範圍過大。
* WebSocket 連接不穩定。

**Data Pipeline**

Data Pipeline 把鏈上數據、鏈下數據、索引結果和業務事件組合成可分析、可監控、可供 AI 使用的數據系統。

一個完整 pipeline 可能包括：

* RPC 或節點數據源。
* event listener。
* 解碼 ABI。
* 數據庫寫入。
* reorg 處理。
* 數據校驗和補償任務。
* API / GraphQL / vector store。
* dashboard、alert 和 Agent context。

AI x Web3 項目尤其需要關注數據來源。Agent 如果拿到的是過期索引或錯誤解碼結果，後續推理再強也會建立在錯誤事實上。

#### 在 AI x Web3 中的位置

AI Agent 需要上下文，而鏈上上下文通常來自索引層。交易歷史、合約事件、用戶倉位、協議狀態、風險信號，都不適合每次臨時從原始區塊裡搜索。

好的索引層應該給 Agent 提供結構化、帶來源、帶時間戳、可回溯的數據。模型負責解釋和推理，索引層負責提供事實。

#### 最小實踐

做一個事件索引設計：

* 選擇一個簡單合約，例如投票、計數器或 NFT mint。
* 列出它應該發出的 event。
* 設計一張查詢表，例如 votes、transfers 或 mints。
* 標出每個字段來自哪個 event 參數或交易字段。
* 寫出如何處理 reorg、重複事件和合約升級。

完成後再問：如果這個數據要給 AI Agent 使用，需要附帶哪些來源字段和更新時間？

#### 擴展閱讀
[Ethereum JSON-RPC API](https://ethereum.org/en/developers/docs/apis/json-rpc/)：理解讀取鏈狀態、查詢日誌和發送交易的底層接口。
[Ethereum Events and Logs](https://ethereum.org/en/developers/docs/smart-contracts/anatomy/#events-and-logs)：理解後端如何監聽鏈上事件。
[The Graph Subgraphs](https://thegraph.com/docs/en/developing/creating-a-subgraph/)：學習 subgraph 的 schema、mapping 和查詢方式。
[Substreams Documentation](https://docs.substreams.dev/)：了解高吞吐鏈上數據 pipeline 的另一種方式。
[Dune Docs](https://docs.dune.com/)：適合用 SQL 分析鏈上數據和構建 dashboard。
