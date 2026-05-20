### 框架（Frameworks）

AI Framework 不是為了讓你少寫幾行 API 調用，而是把模型、工具、狀態、檢索、評估和部署組織成一個可維護的系統。框架選錯，問題通常不是「跑不起來」，而是後面調不動、測不了、換不掉。

#### 為什麼要學這個

剛開始做 AI 應用時，直接調用一個模型 API 就夠了。真正進入產品後，你會很快遇到更複雜的問題：prompt 要版本管理，工具調用要有 schema，Agent 要記錄 state，失敗要重試，用戶反饋要進入評估，線上行為要能追蹤。

Frameworks 解決的是這些工程組織問題。它們不替你定義產品價值，也不保證模型輸出正確，但可以幫你把複雜系統拆成更清楚的模塊。

學框架時最重要的判斷不是「哪個最流行」，而是：它到底幫你管理了哪一層複雜度，又把哪些複雜度藏起來了。

#### 第一性原理

框架是系統邊界的表達，不是智能本身。先理解工作流，再決定用不用框架。
很多失敗的 AI 項目不是輸在沒有框架，而是先引入框架，再讓產品邏輯遷就框架。更穩的方式是先畫清楚輸入、狀態、工具、輸出、評估和失敗路徑，再看哪些部分值得交給框架。

簡單鏈路先保持簡單：一次模型調用、一次檢索、一次格式化輸出，不一定需要複雜 Agent 框架。
長流程需要顯式狀態：多步任務、工具調用、人工確認、失敗恢復，應該有可查詢的 state，而不是只靠聊天歷史。
框架要能退出：如果某個框架讓你很難換模型、換向量庫、換部署方式，長期成本會很高。

#### 知識節點

**LangChain**

LangChain 是最常見的 LLM 應用開發框架之一，覆蓋模型接入、prompt、工具調用、retriever、agent、output parser 等模塊。

它適合快速把模型能力和外部系統接起來，也適合學習 AI 應用常見組件。但使用時要小心「抽象太早」：如果你還沒搞清楚自己的工作流，直接套一堆 chain 和 agent，後面排查問題會變難。

LangChain 更像一套組件庫。它適合幫你組合能力，不適合替你決定產品邊界。

**相關 topic**

```提示詞（Prompt）```：框架裡的 prompt 管理仍然要回到任務邊界和輸出格式。

**LangGraph**

LangGraph 更偏向工作流和狀態機。它把 Agent 或多步驟任務表示成 graph：節點負責執行動作，邊負責控制流，state 負責記錄過程。

當任務只是「問一次，答一次」，LangGraph 可能太重。
但如果任務需要多輪工具調用、重試、人工確認、分支、恢復和長期運行，顯式 graph 會比一長串 prompt 歷史更可靠。

一個實用判斷是：只要你開始關心任務走到哪一步、能否恢復、失敗後從哪裡繼續，就應該考慮 graph / state machine。

**相關 topic**

```智能體（Agent）```：先理解 Agent 為什麼需要目標、工具、狀態和停止條件。

```OpenAI Agents SDK```

OpenAI Agents SDK 用來構建帶工具、handoff、guardrails、tracing 的 Agent 應用。它的價值在於把 Agent 工作流裡的常見工程問題做成可組合結構。

你可以用它組織：

* Agent 的指令和工具
* 多 Agent 之間的 handoff
* 工具調用和結構化輸出
* guardrails 和運行時追蹤

關鍵仍然是邊界：SDK 可以幫你執行流程，但你要定義哪些工具可用、哪些動作需要確認、什麼輸出算失敗。

```DSPy```

DSPy 關注的是把 prompt / LM pipeline 寫成可優化的程序。它不是讓你手工調一句 prompt，而是把輸入輸出、模塊和指標定義清楚，再用 optimizer 改進 prompt 或調用策略。

當你的任務只是寫一段文案，DSPy 未必必要。
當你有明確數據集、評估指標和可重複任務時，它會更有價值，比如分類、抽取、問答、rerank、複雜推理鏈。

DSPy 的關鍵啟發是：不要只靠感覺調 prompt，要讓任務、數據和指標進入系統。

**相關 topic**

```評估（Evaluation）```：沒有 eval，自動優化很容易優化到錯誤目標。

```Hermes```

Hermes 在這裡更適合作為「面向工具調用和結構化輸出的模型 / agent 生態」來理解，而不是通用框架。

它提醒我們一件事：框架不是唯一抽象層。模型本身是否擅長 tool calling、JSON mode、long context、reasoning，也會影響系統設計。一個工具調用能力穩定的模型，可以減少很多解析和兜底成本；反過來，模型能力不穩定時，再好的框架也要補大量 guard。

看 Hermes 這類方向時，不要只看榜單分數，要看它是否能穩定地產生你需要的結構化輸出和工具調用格式。

```Learning Agent```

Learning Agent 指系統可以從反饋、日誌、評估結果或用戶修正中改進。這裡的「學習」不一定是訓練模型，也可以是更新 prompt、調整 retriever、補充規則、改進測試集。

真實產品裡，Learning Agent 最容易踩的坑是把線上反饋直接變成行為變化。這樣會引入數據污染、越權學習和不可解釋變化。

更穩的流程是：

* 記錄失敗樣本。
* 人工或規則標注原因。
* 加入 eval / regression set。
* 修改 prompt、檢索、工具或模型配置。
* 通過測試後再上線。

學習能力要先進評估閉環，再進入生產系統。

#### 在 AI x Web3 中的位置

Frameworks 在 AI x Web3 裡負責把模型能力接到產品流程裡：讀取上下文、調用工具、生成結構化動作、記錄 trace、進入 eval。

但它不應該直接替代 Web3 側的權限、簽名、交易模擬和帳戶規則。框架可以組織 Agent，不能替用戶承擔資產風險。

比較穩的分工是：

* AI Framework 管理 prompt、tools、state、eval 和 trace。
* Web3 基礎設施管理帳戶、簽名、合約、交易和鏈上狀態。
* 產品層定義用戶目標、權限邊界、確認流程和失敗處理。

#### 最小實踐

做一個「文檔問答 + 工具調用」的最小框架對比。

同一個任務，用兩種方式實現：

* 直接調用模型 API：用戶問題 + 檢索結果 + JSON 輸出。
* 使用一個框架：同樣的輸入輸出，但加入 tool schema、trace、失敗重試和測試樣本。

對比四件事：

* 哪個版本更容易讀懂？
* 哪個版本更容易加工具？
* 哪個版本更容易定位錯誤？
* 哪個版本更容易寫回歸測試？

這個練習的重點不是選冠軍，而是看清框架到底幫了你什麼。

#### 擴展閱讀
[LangChain Agents Docs](https://python.langchain.com/docs/modules/agents/)：了解 LangChain 如何組織模型、工具和 Agent。
[LangGraph Docs](https://langchain-ai.github.io/langgraph/)：適合學習有狀態、可恢復的 Agent workflow。
[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)：查看 OpenAI 生態裡 Agent、handoff、guardrails、tracing 的組織方式。
[DSPy Documentation](https://dspy-docs.vercel.app/)：理解用 signatures、modules 和 optimizers 管理 LM pipeline 的思路。
[Nous Hermes Function Calling](https://huggingface.co/NousResearch/Hermes-2-Pro-Mistral-7B)：看工具調用和結構化輸出在模型層的實現樣例。
