### 帳戶抽象（Account Abstraction）

帳戶抽象把「帳戶如何驗證操作、誰來付 gas、哪些權限可以自動執行」從固定的 EOA 模式裡釋放出來，讓錢包更像可編程帳戶系統。

#### 為什麼要學這個

普通 EOA 錢包的限制很明顯：用戶必須保管私鑰，必須用原生代幣付 gas，簽名權限很粗，自動化很難做，恢復體驗也不友好。

Account Abstraction 試圖把帳戶變成智能合約，讓帳戶自己定義驗證邏輯和執行策略。這樣就可以支援多簽、社交恢復、gas sponsorship、session key、限額、批量交易和更細粒度權限。

帳戶抽象的核心不是「免 gas」，而是把帳戶控制權從單一私鑰擴展成可編程規則。

#### 第一性原理

當帳戶本身可以編程，權限就可以從「有私鑰 / 沒私鑰」變成「在什麼條件下允許什麼動作」。
這對 AI x Web3 特別重要。Agent 不應該拿用戶主私鑰，也不應該擁有無限交易權限。更合理的方式是給 Agent 一個可限制、可過期、可撤銷、可審計的行動空間。

* 驗證邏輯可定製：帳戶可以用多簽、Passkey、社交恢復或模組規則驗證操作。
* 支付邏輯可定製：gas 可以由用戶、應用、paymaster 或其他資產承擔。
* 權限可以最小化：session key 可以只允許特定合約、額度、時間和方法。

#### 知識節點

**ERC-4337**

ERC-4337 是以太坊生態最重要的帳戶抽象標準之一，用 alt mempool 和 EntryPoint 實現智能帳戶交易流程。

在 ERC-4337 裡，用戶不直接發送普通交易，而是創建 UserOperation。Bundler 收集這些操作，提交到鏈上的 EntryPoint 合約。EntryPoint 再調用智能帳戶驗證和執行邏輯。

流程簡化如下：

* 用戶或應用生成 UserOperation。
* 智能帳戶驗證簽名、nonce、餘額或策略。
* Bundler 打包並提交操作。
* EntryPoint 調用帳戶執行目標動作。
* Paymaster 可選擇贊助 gas。

**相關 topic**

```EIP-4337```：標準原文，適合理解 UserOperation、EntryPoint、Bundler 和 Paymaster。

**Smart Account**

Smart Account 是由合約控制的帳戶，可以把權限、恢復、批量執行和策略寫進帳戶邏輯。

EOA 的驗證邏輯基本固定：誰有私鑰，誰就能簽名。Smart Account 則可以規定：

* 需要多個簽名才能轉移大額資產。
* 小額交易可以自動通過。
* 某些 dApp 可以在一定額度內調用。
* 錢包丟失後可以通過恢復人或設備找回。
* 交易可以批量執行，減少用戶確認次數。

風險也隨之增加。智能帳戶本身是合約，合約 bug、模組權限、升級邏輯和外部依賴都會變成帳戶風險。

**相關 topic**

```錢包（Wallet）```：先理解 EOA、簽名、交易和 gas 的基礎體驗。
```智能合約（Smart Contract）```：Smart Account 本質上也是管理資產和權限的合約系統。

**Bundler**

Bundler 負責收集 UserOperation，模擬驗證並提交到 EntryPoint。

在 ERC-4337 裡，Bundler 類似交易打包服務，但它處理的是 UserOperation，不是普通錢包直接發出的交易。Bundler 需要判斷操作是否有效、是否能支付 gas、是否會在執行中失敗。

對應用來說，Bundler 是基礎設施依賴。Bundler 不穩定，用戶操作就可能卡住；模擬不充分，失敗交易會帶來體驗和成本問題。

**Paymaster**

Paymaster 允許第三方為用戶操作支付 gas，或者讓用戶用非原生資產承擔費用。

Paymaster 常用於 onboarding：新用戶沒有 ETH，也可以完成第一筆操作。它也可以用於活動補貼、訂閱、白名單交易或應用內 gas 抽象。

但 Paymaster 不是免費午餐。它需要風控：

* 贊助哪些方法？
* 每個用戶額度是多少？
* 是否限制目標合約？
* 如何防止 spam 和套利？
* 誰承擔失敗操作成本？

**Session Key**

Session Key 是給應用或 Agent 的臨時權限，不應該等同於用戶主私鑰。

Session Key 可以被限制為：只在某段時間有效，只能調用某個合約，只能使用某些方法，只能花費某個額度，只能在特定鏈上執行。

這正是 Agent Wallet 的關鍵基礎。你不希望 AI Agent 每次都打斷用戶簽名，也不希望它擁有無限權限。Session Key 提供中間狀態：讓 Agent 可以自動執行低風險動作，但高風險動作仍然需要用戶確認。

#### 在 AI x Web3 中的位置

Account Abstraction 是 AI Agent 上鏈執行的重要底座。沒有帳戶抽象，Agent 往往只能停留在「給建議」或「讓用戶每一步都簽名」。有了智能帳戶、Paymaster 和 Session Key，Agent 才可能在受限範圍內自動執行。

但越自動化，越需要清楚的 policy：能調用什麼、額度多少、多久過期、誰能撤銷、日誌在哪裡、失敗後怎麼處理。帳戶抽象不是讓 AI 更自由，而是讓 AI 的自由被規則包起來。

#### 最小實踐

設計一個 Agent Session Key 策略：

* 選擇一個具體場景，例如「每小時最多再平衡一次測試網小額資產」。
* 寫清楚允許調用的合約地址和方法。
* 設置額度、過期時間、鏈 ID 和最大交易次數。
* 寫出哪些動作必須回到用戶錢包確認。
* 說明如何撤銷 session key，以及如何審計它執行過什麼。

重點不是馬上部署完整 AA 錢包，而是學會把權限從「全部允許」拆成可驗證規則。

#### 擴展閱讀
[EIP-4337](https://eips.ethereum.org/EIPS/eip-4337)：帳戶抽象標準原文。
[ERC-4337 Documentation](https://erc4337.io/docs/)：開發者視角理解 EntryPoint、Bundler、Paymaster 和 Smart Account。
[Ethereum Account Abstraction](https://ethereum.org/en/roadmap/account-abstraction/)：從以太坊路線圖角度理解帳戶抽象為什麼重要。
[Safe Smart Accounts](https://docs.safe.global/)：了解多簽和智能帳戶在真實項目中的使用方式。
[Rhinestone Smart Sessions](https://docs.rhinestone.wtf/)：學習 session key、權限策略和模組化智能帳戶設計。
