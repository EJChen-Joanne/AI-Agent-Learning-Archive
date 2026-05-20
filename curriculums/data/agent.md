### 智能體（Agent）

Agent 是能圍繞目標持續調用工具、讀取狀態、調整步驟的 AI 系統。它的關鍵不在「像人」，而在於它能不能在明確權限和可審計流程裡，把建議推進到行動。

#### 為什麼要學這個

LLM 一次回答問題，通常只是在生成文本。Agent 更進一步：它可以拆任務、查資料、調用 API、寫代碼、生成操作草稿、等待反饋再繼續下一步。

這也是 Agent 真正的風險點。一旦它能調用工具、寫入系統、提交請求或觸發支付，錯誤就不再只是「答錯」，而會變成「做錯」。所以 Agent 的核心不是讓模型更像人，而是讓執行循環有清楚邊界。

學 Agent 的重點不是追逐框架，而是建立分工：模型負責提出候選行動，系統負責限制行動空間，用戶負責批准高風險邊界。

#### 第一性原理

Agent 不是自主權本身，而是被約束的執行循環。目標、工具、狀態、權限和停止條件缺一不可。
一個 Agent 如果只有模型和工具，就像一個會說話的腳本執行器。真正可用的 Agent 必須知道自己能做什麼、不能做什麼、做完如何驗證、失敗如何停止、誰能審計它做過的事。

工具比回答更危險：讀數據、寫數據庫、發送請求、改配置不是同一風險等級。
狀態必須外置和可查：任務進度、工具結果、失敗原因、用戶確認都要記錄，不應只藏在模型上下文裡。
停止條件要明確：達到目標、超出預算、信息不足、風險越界、用戶拒絕，都應該讓 Agent 停下來。

#### 知識節點

**Tool Use**

Tool Use 是 Agent 調用外部能力：搜索、數據庫、API、代碼執行、郵件、支付接口、內部系統等。

工具讓 Agent 從「會回答」變成「能做事」。但工具也讓 Prompt Injection 和模型誤判變得危險。一個能讀網頁的 Agent 被惡意網頁影響，和一個能寫入系統的 Agent 被惡意網頁影響，後果完全不同。

工具設計要明確：

* 輸入 schema
* 權限範圍
* 是否只讀
* 是否會產生外部副作用
* 調用前後如何記錄
* 哪些調用需要人工確認

**相關 topic**

```Web3 Tool Use```：繼續看 RPC、錢包和合約工具如何接入 Agent。
```MCP```：了解工具和上下文協議化的一種方式。

**Planning**

Planning 是把目標拆成步驟。比如「幫我分析這個 DAO 提案」可以拆成讀取提案、檢索歷史討論、總結爭議、檢查投票機制、生成風險清單。

計劃有用，但不能神化。模型生成的計劃只是候選路線，不是授權。越靠近高風險動作，計劃越需要被系統規則拆開檢查。

一個好的 Agent plan 應該能暴露：

* 每一步需要什麼工具
* 每一步讀還是寫
* 哪些步驟可自動執行
* 哪些步驟需要用戶確認
* 失敗時是否可以重試
* 最終如何驗證任務完成

```State```

State 是 Agent 當前任務的狀態，包括用戶目標、已完成步驟、工具返回、錯誤、預算、確認記錄和最終輸出。

很多 Agent Demo 把 state 只放在 prompt 歷史裡，這不夠。生產系統需要可查詢、可恢復、可審計的 state。否則你很難回答：Agent 為什麼調用了這個工具？它是否已經拿到用戶確認？哪一步開始偏離目標？

在有外部執行的場景裡，state 還應該記錄環境、版本、關鍵參數、工具調用結果、確認請求和撤銷事件。

**相關 topic**

```Agent Workflow```：看 Agent 從目標到執行的流程拆分。
```Chain-aware Context```：理解鏈上狀態如何進入並影響 Agent 決策。

```Reflection```

Reflection 是讓 Agent 檢查自己的中間結果，例如發現信息不足、工具失敗、計劃不合理，然後修正下一步。

它適合提升複雜任務質量，但不能替代外部驗證。Agent 自我反思仍然由模型完成，模型可能給自己的錯誤找理由。尤其是寫入、授權、支付這類動作，reflection 只能作為輔助診斷，不能作為最終安全判斷。

自我檢查可以提高質量，確定性檢查才能承載風險。

```Multi-Agent```

Multi-Agent 是多個 Agent 分工協作，例如研究 Agent 讀資料，開發 Agent 寫代碼，安全 Agent 做風險審查，執行 Agent 調用工具。

它適合複雜工作流，但也會放大協調問題：上下文傳遞丟失、責任邊界模糊、一個 Agent 的錯誤被另一個 Agent 當成事實、工具權限擴散。

做 Multi-Agent 時，要先問一個樸素問題：多個 Agent 是否真的減少複雜度？如果只是把一個不清楚的流程拆成多個不清楚的角色，系統會更難調試。

#### 在 AI x Web3 中的位置

Agent 位在模型能力和鏈上執行之間。它可以把用戶目標推進成多步流程，但不能繞過帳戶、權限和結算規則。

一個相對穩的 AI x Web3 Agent 架構通常是：

* 用戶提出目標和約束。
* Agent 讀取上下文並生成計劃。
* 系統把計劃拆成只讀步驟和候選寫入步驟。
* 只讀工具自動執行，寫入工具進入 policy 檢查。
* Simulation 展示鏈上影響。
* 用戶確認高風險動作。
* Wallet / Smart Account 執行。
* 日誌記錄每一步和最終狀態。

最危險的設計是讓 Agent 同時擁有模糊目標、廣泛工具、長期記憶和大額資產權限。

#### 最小實踐

做一個「DAO 提案研究 Agent」的最小版本。

它只能執行只讀動作：

* 讀取提案正文
* 檢索論壇討論
* 總結支持和反對理由
* 標記缺失信息
* 輸出投票前檢查清單

不要讓它直接投票。相反，要求它在輸出裡明確：

* 用了哪些來源
* 哪些結論證據不足
* 是否發現治理或資金風險
* 如果用戶要投票，還需要人工檢查什麼

完成後，再設計一個權限升級版本：只有當用戶明確授權，並經過投票交易 simulation 後，系統才允許生成投票交易草稿。

#### 擴展閱讀
[OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents)：理解 Agent 工作流、工具、guardrails、知識和監控的基礎組成。
[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)：查看用 SDK 構建帶工具、handoff、streaming 和 tracing 的 Agent 應用。
[LangGraph Documentation](https://langchain-ai.github.io/langgraph/)：適合學習有狀態、多步驟、可恢復的 Agent workflow。
[Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)：從工程角度區分 workflow 和 agent，適合校準複雜度。
[OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)：重點看過度代理、Prompt Injection、工具濫用和敏感信息洩露風險。
