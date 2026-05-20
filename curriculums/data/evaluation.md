### 評估（Evaluation）

Evaluation 是把「感覺效果不錯」變成「系統可持續改進」的方法。沒有 eval，prompt、模型、RAG、Agent 和工具調用的變化都只能靠主觀試用判斷，遲早會被回歸問題拖住。

#### 為什麼要學這個

AI 應用最大的問題之一，是輸出質量不穩定。你改了一句 prompt，某些問題變好了，另一些問題變差了；換了模型，平均效果提升，但關鍵場景出錯；接了 RAG，答案更長了，但引用反而不準。

Evaluation 要解決的就是這些問題：用明確樣本、指標、評分方式和回歸測試，判斷系統是不是真的變好了。

學 eval 的目標不是做一份漂亮報告，而是讓團隊能回答：這次改動有沒有讓關鍵任務更可靠？有沒有引入新的失敗模式？

#### 第一性原理

不能被重複測量的 AI 行為，就不能被穩定改進。
AI 系統的輸出有概率性，用戶問題又很開放。如果沒有固定樣本和評估標準，你很難知道系統變化來自真實改進、運氣、還是測試樣本太少。

先測任務，不只測模型：用戶真正關心的是整條鏈路是否完成任務，而不是模型榜單分數。
先保住關鍵失敗場景：高風險錯誤、常見問題、邊界條件，要進入 regression set。
評估要貼近產品：離真實輸入越遠，eval 越容易變成自我安慰。

#### 知識節點

**Harness**

Harness 是運行 eval 的框架。它負責餵樣本、調用系統、收集輸出、運行 grader、記錄結果。

一個最小 harness 至少需要：

* 輸入樣本
* 期望輸出或評分規則
* 被測系統版本
* 模型和參數配置
* 運行日誌
* 結果報告

Harness 的價值是可重複。沒有可重複運行的 eval，你就很難比較不同 prompt、不同模型、不同檢索策略。

**Golden Set**

Golden Set 是一組被認真挑選和標注的測試樣本。

它不一定要很大。早期 30 到 100 條高質量樣本，往往比一堆隨便收集的問題更有用。關鍵是覆蓋真實任務和關鍵失敗模式。

Golden Set 應該包含：

* 常見正常問題
* 邊界問題
* 容易誤判的問題
* 高風險問題
* 歷史 bug
* 用戶真實反饋樣本

每修一個重要 bug，都應該考慮把它變成 regression 樣本。

```LLM-as-Judge```

LLM-as-Judge 是用模型來給模型輸出評分。它適合評估開放式答案，比如摘要質量、是否回答完整、是否遵循格式、是否引用來源。

但它不能被神化。Judge 模型也會偏、會漏、會被輸出風格影響。更穩的做法是：

* 對可自動判斷的字段用規則評分。
* 對開放式質量用 LLM judge。
* 對高風險樣本保留人工抽檢。
* 定期校準 judge 和人工評分的一致性。

LLM-as-Judge 是評估工具，不是最終真相。

```Regression```

Regression 是防止舊問題復發。

AI 應用很容易出現「修 A 壞 B」。一次 prompt 修改、一次模型升級、一次 retriever 調整，都可能影響很多舊場景。Regression set 的作用就是把歷史問題固定下來，每次改動都重新跑。

一個實用做法：

* 用戶反饋一個錯誤。
* 復現並記錄輸入。
* 標注期望輸出或拒答條件。
* 加入 regression set。
* 之後每次發布前跑一次。

```Observability```

Observability 是線上觀察系統行為的能力。Eval 多數發生在發布前，observability 發生在真實使用中。

你至少要記錄：

* 輸入類型和來源
* 檢索結果
* 工具調用
* 模型輸出
* 錯誤和重試
* 用戶反饋
* 成本和延遲

沒有 observability，你就不知道真實用戶在哪裡失敗，也不知道該往 golden set 裡補什麼。

#### 在 AI x Web3 中的位置

AI x Web3 系統裡，eval 更重要，因為錯誤可能影響資產、權限、治理判斷和鏈上執行。

需要特別評估：

* 交易解釋是否準確
* 風險提示是否漏報
* 工具調用參數是否越界
* 是否能拒絕不確定請求
* 是否能識別 Prompt Injection
* 引用和來源是否可追溯
* 高風險動作是否要求 human check

Eval 不會替代交易模擬和權限控制，但它能讓你持續發現系統在什麼場景下不可靠。

#### 最小實踐

給一個「交易解釋 / 文檔問答 / Agent 工具調用」原型做最小 eval。

準備 30 條樣本：

* 10 條正常問題
* 10 條邊界或容易混淆的問題
* 5 條歷史 bug 或預期失敗樣本
* 5 條惡意或注入樣本

為每條樣本定義：

* 輸入
* 期望行為
* 必須包含的信息
* 必須拒絕或提醒的情況
* 是否需要引用來源

然後每次改 prompt、模型或檢索策略前後跑一遍，記錄變化。

#### 擴展閱讀
[OpenAI Evals API Reference](https://platform.openai.com/docs/guides/evals)：查看 OpenAI 平台如何創建和運行 eval。
[OpenAI: How evals drive the next chapter in AI](https://openai.com/research/evals)：從產品和業務角度理解 eval 為什麼重要。
[OpenAI Evals GitHub](https://github.com/openai/evals)：開源 eval 框架和樣例，適合理解 benchmark / grader 的組織方式。
[LangSmith Evaluation Docs](https://docs.smith.langchain.com/evaluation)：了解 LLM 應用的 dataset、experiment、feedback 和 tracing。
[RAGAS Documentation](https://docs.ragas.io/)：適合學習 RAG 場景下的回答質量、上下文相關性和 faithfulness 評估。
