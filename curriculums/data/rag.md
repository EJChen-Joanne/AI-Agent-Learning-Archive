### 檢索增強生成（RAG）

RAG 不是「給模型接一個向量庫」這麼簡單。它是一條把外部知識取回、篩選、引用、交給模型使用的證據鏈，用來減少過期知識和無來源回答。

#### 為什麼要學這個

LLM 的訓練知識會過期，context window 也放不下整個互聯網、全部協議文檔和歷史治理討論。RAG 的作用是：當用戶提出問題時，系統先從知識庫裡找相關材料，再讓模型基於這些材料回答。

在真實 AI 應用裡，RAG 很常見：產品文檔問答、代碼庫助手、研究摘要、客服知識庫、SDK Copilot、內部知識檢索。但很多 RAG Demo 只做到了「能搜到一些段落」，還沒有做到「答案能被驗證」。

RAG 的核心不是讓回答更長，而是讓回答有來源、有版本、有邊界。沒有 citation 和 freshness 的 RAG，只是把幻覺從模型內部搬到了檢索系統裡。

#### 第一性原理

RAG 的可靠性取決於證據鏈，不取決於向量庫這個名詞。
一個 RAG 系統至少有三次判斷：文檔怎麼切，查詢時取哪些內容，生成時如何引用和拒答。任何一層做錯，模型都會拿著錯誤材料說得很順。

檢索結果不是事實：它只是候選證據，仍要看來源、時間、版本和適用範圍。
引用要能回到原文：答案裡的關鍵判斷應該能追溯到具體文檔、段落或鏈上記錄。
檢索失敗要允許拒答：找不到證據時，系統應該說「不確定」，而不是讓模型補全。

#### 知識節點

**Chunking**

Chunking 是把長文檔切成可檢索片段。切太小，語義斷裂；切太大，檢索結果噪聲多，token 成本高。

技術文檔尤其需要小心切分。函數說明、參數表、風險提示、版本說明、示例代碼經常跨段落出現。如果只按固定字數切，模型可能拿到函數名卻拿不到限制條件。

比較穩的做法是按結構切：標題、API endpoint、函數說明、標準小節、FAQ 問答、審計或變更記錄。每個 chunk 保留來源 URL、標題路徑、更新時間和版本。

**Vector DB**

Vector DB 用來存儲 embedding，並按相似度檢索相關 chunk。它解決的是「語義相近內容怎麼快速找到」的問題。

但向量相似不等於答案正確。一個舊版本 SDK 文檔可能和用戶問題高度相似，卻已經不適用；一個第三方博客可能寫得很像官方文檔，卻缺少權威性。

所以 Vector DB 裡不應該只存向量，還要存 metadata：來源、版本、chain、更新時間、可信等級、是否廢棄。檢索時先過濾，再排序。

**相關 topic**

```Embedding```：先理解文本如何變成可比較的向量。

```Retriever```

Retriever 是根據用戶問題取回候選材料的組件。它可以是向量檢索、關鍵詞檢索、混合檢索、圖檢索，也可以加上 metadata filter。

好的 retriever 不能只看語義相似度。它還要知道用戶問的是哪個產品、哪個版本、哪段時間、官方文檔還是社區討論。比如同一個 API 在不同 SDK 版本裡可能參數不同。

一個實用判斷：如果用戶問題裡有版本、環境、時間、地址或具體對象，你的 retriever 就不應該只做純向量搜索。

```Rerank```

Rerank 是在初步檢索後，對候選材料重新排序，把更相關、更可信、更完整的內容排到前面。

它常用於候選結果很多、相似度接近或混合檢索的場景。對技術文檔問答來說，rerank 可以減少「標題相似但內容不對」的結果；對治理討論來說，它可以把真正討論核心爭議的段落排在閒聊前面。

Rerank 會增加延遲和成本，所以要看場景。面向資產風險或開發者文檔的問答，通常值得加；小型 FAQ 未必需要。

```Citation```

Citation 是把答案裡的關鍵結論連接回來源。它不是裝飾，而是用戶驗證答案的入口。

在技術問答裡，citation 至少要能說明：

* 這句話來自哪份文檔或鏈上記錄
* 來源是否官方
* 文檔版本或更新時間
* 哪些結論只是模型歸納
* 哪些地方沒有足夠證據

如果一個 RAG 系統不能展示來源，用戶就很難判斷答案是基於文檔、基於舊知識，還是模型自己補出來的。

#### 在 AI x Web3 中的位置

RAG 位在 Knowledge Base 和模型之間。它幫 Agent 查資料、補上下文、引用證據，但不負責最終執行。

常見應用包括：

* 協議文檔問答
* 合約接口解釋
* 治理提案和論壇摘要
* 審計報告檢索
* SDK / API Copilot
* 交易解釋時補充項目背景

當 RAG 結果要影響鏈上動作時，還需要接 simulation、policy 和 human check。文檔說某函數「可以調用」，不等於當前用戶「應該簽名」。

#### 最小實踐

做一個「協議文檔 RAG 問答」的最小版本。

選擇一個官方文檔站，抓取 10 到 20 篇頁面，按標題結構切 chunk，存入向量庫。用戶提問時，系統返回答案和引用。

至少測試三類問題：

* 文檔中明確存在的 API 用法
* 文檔中不存在的問題，要求系統拒答
* 舊版本或不確定版本的問題，要求系統提示需要核對版本

輸出時強制區分：

* answer
* sources
* uncertainties
* needs_version_check

這個練習的重點是證據鏈，不是 UI。

#### 擴展閱讀
[OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)：理解向量表示如何支持語義搜索、聚類和 RAG。
[OpenAI File Search Guide](https://platform.openai.com/docs/assistants/tools/file-search)：了解託管文件檢索如何把外部資料接入模型工作流。
[LangChain Retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers/)：查看常見 retriever、向量庫、reranker 和混合檢索集成。
[Pinecone RAG Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)：適合看一個向量數據庫視角下的 RAG 數據流。
[OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)：關注向量和 embedding 風險、Prompt Injection、錯誤信息傳播等安全問題。
