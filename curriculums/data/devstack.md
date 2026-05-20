### 開發棧（Dev Stack）

Web3 開發棧不是一組隨機工具名，而是一條從寫合約、測合約、部署合約、連接錢包、調用合約到監控結果的工程鏈路。工具選型的目標是讓鏈上開發更可驗證、更可復現、更少事故。

#### 為什麼要學這個

寫一個 Web3 demo 很容易：接錢包、調合約、發交易。但真正做項目時，你會馬上遇到合約編譯、測試、部署腳本、環境變量、RPC、前端 SDK、鏈切換、合約驗證、權限管理和監控。

開發棧的作用不是讓你收集更多工具，而是把開發流程變成可重複的系統。一個項目至少要做到：本地能跑、測試能復現、部署有記錄、前端調用明確、合約地址可追蹤。

工具鏈越清楚，鏈上執行越可控。

可以先把一條最小開發鏈路拆成六步：

* 在本地或瀏覽器 IDE 寫出合約。
* 編譯合約，得到 bytecode 和 ABI。
* 在本地鏈或測試網部署合約。
* 寫測試覆蓋核心狀態變化和權限邊界。
* 前端用合約地址和 ABI 讀取或發送交易。
* 在區塊瀏覽器驗證源碼、交易和事件。

這些步驟缺一環，後面都會變成排查成本。比如前端拿錯 ABI，會出現參數編碼錯誤；部署地址沒有版本記錄，會讓用戶和開發者不知道自己到底在和哪份合約交互；測試只覆蓋 happy path，則權限和失敗分支很容易漏掉。

#### 第一性原理

Web3 工具鏈的核心是把不可逆執行前移到可測試、可模擬、可審查的流程裡。
鏈上交易一旦成功，後悔成本很高。因此開發工具要盡量把錯誤暴露在本地、測試網、模擬環境和 code review 階段，而不是等到主網上線後再發現。

* 本地優先復現：合約邏輯、部署腳本和前端調用都應該能在本地或測試網跑通。
* 地址和 ABI 要版本化：前端調用的到底是哪份合約，必須能追蹤。
* 安全庫不是免審計：OpenZeppelin 等庫降低基礎風險，但組合邏輯仍要自己驗證。

#### 知識節點

**Remix**

Remix 是瀏覽器裡的 Solidity IDE。它可以編寫、編譯、部署和調試合約，適合入門、教學、原型和快速驗證。

它的優勢是低門檻，不需要先搭完整工程。但真實項目仍然需要進入 Git、測試框架、部署腳本和 CI，否則很難復現和協作。

你可以把 Remix 當成「合約實驗台」。最適合用它做三件事：

* 快速複製一段 Solidity 代碼，看能不能編譯。
* 在 JavaScript VM 或測試網部署合約，觀察構造函數、函數調用和 event。
* 用 Deploy & Run 面板理解 read 和 write 調用的區別。

Remix 不適合長期替代工程化 repo。只要項目開始多人協作，就應該把合約放進 Git 倉庫，並用 Hardhat 或 Foundry 固化測試和部署流程。

**相關 topic**

```Remix Documentation```：官方文檔，適合入門 Remix 工作區、編譯器、Deploy & Run、debugger 和插件。

**Hardhat**

Hardhat 提供本地開發網路、編譯、測試、部署腳本和插件生態。對前端團隊來說，它和 TypeScript、ethers、CI 的結合比較自然。

學習 Hardhat 的重點不是記命令，而是理解本地鏈、測試網、部署腳本、合約驗證和環境變量如何組成完整開發流程。

一個典型 repo 會包含：

* `contracts/`：Solidity 合約源碼。
* `test/`：TypeScript 或 Solidity 測試。
* `ignition/` 或 `scripts/`：部署模組和腳本。
* `hardhat.config.ts`：網路、編譯器、插件和變量配置。
* `artifacts/`：編譯生成的 ABI、bytecode 和 metadata。

如果你的項目需要和前端、後端、CI 緊密協作，Hardhat 通常比只用 Remix 更容易把流程固定下來。

**相關 topic**

```Hardhat Documentation```：官方文檔，重點看 getting started、testing、deploying、configuration variables 和 contract verification。

**Foundry**

Foundry 常用工具包括 forge、cast、anvil。它可以用 Solidity 寫測試，運行速度快，也適合做 fuzz testing、腳本部署和鏈上狀態交互。

Foundry 的幾個常見入口：

* `forge test`：運行合約測試。
* `forge build`：編譯合約。
* `anvil`：啟動本地測試鏈。
* `cast call`：讀取鏈上合約。
* `cast send`：發送交易調用合約。

它特別適合訓練「先寫測試，再改合約」的習慣。對安全敏感的合約來說，能快速跑單元測試、fuzz test 和 fork test，比只在 UI 上點幾次更可靠。

**相關 topic**

```Foundry Book```：官方文檔，適合學習 forge、cast、anvil、fuzz testing 和 fork testing。

**OpenZeppelin**

OpenZeppelin Contracts 包含 ERC-20、ERC-721、AccessControl、Ownable、Pausable 等常見模組。使用成熟庫可以減少重複造輪子，也能避免很多基礎實現錯誤。

但危險在於「用了庫就安全」的錯覺。權限組合、升級模式、參數設置、外部調用和經濟設計仍然可能出問題。

一個常見例子：你可以用 OpenZeppelin 的 ERC-20 實現 token，但仍然要自己決定誰能 mint、是否能 pause、owner 是否可以轉移、升級權限是否有 timelock。這些不是庫自動幫你做出的產品決策。

**相關 topic**

```智能合約（Smart Contract）```：先理解合約狀態、ABI、事件和升級風險。
```OpenZeppelin Upgrades```：了解 proxy 升級流程和升級合約的風險邊界。

**viem / wagmi**

viem 是 TypeScript 以太坊接口庫，強調類型安全和底層調用能力。wagmi 則面向 React 應用，提供錢包連接、帳戶狀態、合約讀寫和 hooks。

前端接鏈時，最容易出問題的是狀態不一致：錢包網路、前端配置、合約地址、RPC 返回、交易 pending 狀態都可能不同步。

在前端裡，至少要把四類狀態分開：

* 錢包是否已連接。
* 用戶當前在哪條鏈。
* 合約讀取結果是否正在載入或已過期。
* 寫交易處於等待簽名、已廣播、等待確認、成功或失敗的哪一步。

#### 在 AI x Web3 中的位置

AI 可以顯著提升 Web3 開發效率：解釋 ABI、生成部署腳本、補測試、排查交易失敗、總結合約權限。但 AI 參與開發棧後，驗證流程反而要更明確。

如果 Agent 能運行 `forge test`、讀取部署配置、調用 `cast` 或生成前端合約調用代碼，它就必須受到 repo workflow、測試、權限和 secret 管理約束。鏈上開發不是普通代碼生成，高風險命令需要人工確認。

#### 最小實踐

搭一個最小 Web3 開發鏈路：

* 用 Remix 部署一個極簡計數器合約，包含 `count()`、`increment()` 和 `CountChanged` event。
* 用 Hardhat 或 Foundry 建一個本地工程，並寫測試覆蓋初始值和 `increment()` 後的狀態變化。
* 記錄合約地址、ABI、部署網路、部署帳號和交易雜湊。
* 用 viem 或 wagmi 從前端讀取 `count()`，再發起一次 `increment()` 交易。
* 在區塊瀏覽器或本地日誌裡確認 event 被正確發出。
* 寫下這條鏈路中哪些資訊必須進版本控制，哪些必須放在 `.env` 或金鑰管理裡。

#### 擴展閱讀
[Remix Documentation](https://remix-ide.readthedocs.io/)：適合從瀏覽器 IDE 入門 Solidity 編譯、部署和調試。
[Hardhat Documentation](https://hardhat.org/docs)：學習 TypeScript/JavaScript 合約開發、測試和部署流程。
[Foundry Book](https://book.getfoundry.sh/)：學習 forge、cast、anvil 和 Solidity-native 測試工作流。
[OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)：查看常見合約標準、安全組件和訪問控制模組。
[viem Documentation](https://viem.sh/)：學習 TypeScript 方式讀取鏈、發送交易和調用合約。
[wagmi Documentation](https://wagmi.sh/)：學習 React 應用中的錢包連接、帳戶狀態和合約交互。
