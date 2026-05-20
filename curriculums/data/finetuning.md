### 微調（Fine-tuning）

Fine-tuning 不是「模型效果不好就訓練一下」。它適合讓模型更穩定地學習某種格式、風格、領域任務或行為模式，但不適合用來補實時知識、修權限邊界或替代評估。

#### 為什麼要學這個

很多人遇到模型回答不好，會第一時間想到 fine-tuning。實際工程裡，fine-tuning 往往不是第一步。

你應該先問：

* 是 prompt 不清楚嗎？
* 是上下文缺了嗎？
* 是檢索沒拿到正確資料嗎？
* 是輸出格式沒有 schema 嗎？
* 是模型本身能力不夠嗎？
* 是否已經有 eval 證明問題穩定存在？

Fine-tuning 的價值在於讓模型在一類任務上更一致，而不是讓模型憑空知道最新事實。沒有數據、沒有評估、沒有明確目標的微調，很容易只是把問題變得更難排查。

#### 第一性原理

Fine-tuning 改的是模型行為分佈，不是產品系統邊界。
微調可以讓模型更像你的數據，但它不會自動帶來事實正確、權限安全、引用可靠或工具調用安全。訓練進去的偏差，也會更穩定地被模型復現。

先有 eval，再談 fine-tuning：否則你不知道微調後到底變好了還是只是在少數樣本上變順了。
先修數據，再修模型：壞數據會把壞習慣訓練得更穩定。
別用微調存實時知識：實時狀態、價格、文檔更新和用戶數據更適合放在檢索或工具裡。

#### 知識節點

**SFT**

SFT 是 Supervised Fine-Tuning，監督微調。它使用輸入和期望輸出樣本，讓模型學習某類任務的回答方式。

SFT 適合：

* 固定格式輸出
* 特定語氣或風格
* 特定任務流程
* 領域術語和回答習慣
* 工具調用樣式

但 SFT 對數據質量非常敏感。如果樣本裡有錯誤、格式不一致、邊界不清，模型會把這些問題學進去。

**LoRA**

LoRA 是 Low-Rank Adaptation，一種參數高效微調方法。它不直接更新全部模型參數，而是訓練較小的適配參數，從而降低訓練成本和顯存需求。

LoRA 常用於開源模型微調，適合資源有限、想快速試驗特定任務的團隊。

它的核心價值是降低實驗成本，但不是魔法。任務定義、數據質量、評估方法仍然決定最終效果。

```PEFT```

PEFT 是 Parameter-Efficient Fine-Tuning，參數高效微調方法的統稱，LoRA 是其中一種。

PEFT 的意義在於：你不一定需要重新訓練整個模型，也可以通過較小參數調整，讓模型適配某個任務或領域。

適合 PEFT 的場景通常有：

* 模型較大，完全微調成本太高
* 任務範圍明確
* 數據量中等
* 需要多版本 adapter 並行試驗

```Dataset```

Dataset 是 fine-tuning 的核心資產。

一個可用的數據集不只是「很多問答對」。它要有清楚的任務定義、輸入來源、輸出標準、質量檢查和切分方式。

至少要區分：

* 訓練集：用於訓練
* 驗證集：用於調參和選擇版本
* 測試集：用於最終評估
* 回歸集：用於防止歷史問題復發

不要把測試集拿去訓練。這會讓評估失去意義。

```Overfitting```

Overfitting 是模型把訓練數據記得太死，導致對新樣本表現變差。

微調時尤其容易出現：

* 訓練樣本太少
* 樣本風格太單一
* 訓練輪數太多
* 目標格式過度僵化
* 驗證集和訓練集太像

過擬合的結果是：模型在你準備的例子上看起來很好，但真實用戶一問就崩。

#### 在 AI x Web3 中的位置

AI x Web3 場景裡，fine-tuning 可以用於特定任務，例如交易解釋風格、治理摘要格式、風險標籤輸出、合約注釋風格、工具調用樣式。

但它不適合替代：

* 鏈上實時狀態查詢
* 合約安全審計
* 交易模擬
* 錢包權限控制
* 用戶確認
* 外部事實引用

換句話說，fine-tuning 可以讓模型更懂你的任務格式，但不能讓模型直接變成可信執行層。

#### 最小實踐

做一個「結構化摘要格式」的微調前評估。

先不要訓練。先準備 50 條樣本：

* 輸入：一段技術文檔或提案。
* 輸出：固定 JSON 字段，例如 summary、risks、open_questions、sources。

然後比較三種方案：

* 只改 prompt。
* Prompt + few-shot。
* 小規模 fine-tuning 或 adapter 方案。

每種方案都用同一套 eval 檢查：

* 字段是否完整
* 是否編造來源
* 風險點是否漏掉
* 輸出是否穩定

只有當前兩種方案無法穩定解決問題時，再考慮 fine-tuning。

#### 擴展閱讀
[OpenAI Fine-tuning Guide](https://platform.openai.com/docs/guides/fine-tuning)：了解 fine-tuning 的適用場景、數據格式和訓練流程。
[Hugging Face PEFT Documentation](https://huggingface.co/docs/peft)：學習 LoRA、adapter 等參數高效微調方法。
[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)：LoRA 原始論文，適合理解低秩適配的基本思想。
[TRL Documentation](https://huggingface.co/docs/trl)：了解 SFT、偏好優化等訓練流程工具。
[OpenAI Evals API Reference](https://platform.openai.com/docs/guides/evals)：微調前後都需要用 eval 判斷效果是否真的提升。
