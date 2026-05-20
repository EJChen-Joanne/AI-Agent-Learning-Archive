### 智能合約（Smart Contract）

智能合約不是「自動執行的法律合同」，而是部署在鏈上的程式。它把規則、資產和狀態放到公開可驗證的執行環境裡，也把錯誤、權限和升級風險暴露給所有人。

#### 為什麼要學這個

Web3 產品的很多核心邏輯都在智能合約裡：token、NFT、DEX、借貸、治理、質押、空投、帳戶抽象。前端可以換，後端可以重構，但合約一旦部署，修改成本和風險通常遠高於普通應用代碼。

學習智能合約，不是為了立刻寫複雜協議，而是先建立判斷力：哪些規則適合上鏈，合約如何保存狀態，調用如何改變狀態，接口如何被其他應用組合，為什麼測試和審計不能省。

智能合約把規則變成公共基礎設施，也把 bug 變成公共風險。

可以先用一個很小的例子理解：一個計數器合約只保存一個 count。任何人調用 `increment()`，count 就加一。這個例子雖然簡單，但已經包含合約最核心的幾件事：狀態變量、外部調用、交易執行、gas 成本、事件記錄和區塊瀏覽器可查。

真實協議只是把這個模型放大了：餘額、抵押品、借款、訂單、投票、權限和升級資訊，都是更複雜的鏈上狀態。

#### 第一性原理

合約的價值來自可驗證執行，不來自「代碼看起來很聰明」。
智能合約能讓任何人檢查規則、調用接口、驗證狀態變化。這個開放性帶來了可組合性，也帶來了攻擊面。你寫的不是普通函數，而是會管理真實資產和公共狀態的程式。

* 狀態公開可查：鏈上狀態不是私有數據庫字段，很多資訊會被所有人看到。
* 調用有成本和順序：每次執行都受 gas、區塊順序和外部狀態影響。
* 權限必須顯式：誰能 mint、pause、upgrade、withdraw，不能靠默認信任。

#### 知識節點

**Solidity**

Solidity 是 EVM 生態最常見的合約語言，先用它理解鏈上程式的寫法和限制。

Solidity 看起來像普通程式語言，但它運行在完全不同的環境裡。合約狀態會寫入鏈上，函數調用可能消耗 gas，錯誤權限可能直接影響資產安全。

學習 Solidity 時，不要只看語法。更重要的是理解 storage、msg.sender、modifier、event、external call、revert 和權限控制這些鏈上特有概念。

一個最小合約大概長這樣：

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Counter {
    uint256 public count;

    event CountChanged(uint256 newCount);

    function increment() external {
        count += 1;
        emit CountChanged(count);
    }
}
```

這裡的 `count` 是鏈上狀態，`increment()` 是會改變狀態的寫操作，event 是外部系統可以索引的日誌。前端讀取 `count()` 不需要用戶簽名，但調用 `increment()` 通常需要錢包簽名並支付 gas。

**相關 topic**

```Solidity Documentation```：官方語言文檔，適合系統學習合約結構、類型、函數、事件、錯誤處理和安全注意事項。

**EVM**

EVM（Ethereum Virtual Machine）可以理解成運行智能合約的虛擬機。Solidity 代碼會被編譯成 EVM 字節碼，部署到鏈上後由節點執行。

理解 EVM 有助於解釋很多現象：為什麼要 gas，為什麼 storage 貴，為什麼外部調用有風險，為什麼同一套合約可以部署到多個 EVM 兼容鏈。

**相關 topic**

```網路（Network）```：繼續看交易如何被網路打包、共識和確認。

**ABI**

ABI（Application Binary Interface）描述合約有哪些函數、參數、返回值和事件。前端 SDK、腳本、區塊瀏覽器和 AI 工具都可以通過 ABI 理解如何編碼調用數據、解碼返回結果。

對 AI x Web3 來說，ABI 也是 Agent 理解合約能力的重要上下文。但 ABI 只告訴你「能調用什麼」，不保證「調用是否安全」。

例如合約裡有一個 `transfer(address to, uint256 amount)`，ABI 會告訴工具這個函數需要一個地址和一個數字。它不會自動告訴你：

* `to` 是不是惡意地址。
* `amount` 的單位是不是 token decimals 後的整數。
* 這次調用會不會觸發外部合約。
* 當前帳戶是否有足夠餘額或 allowance。
* 這個函數是否被暫停或受權限限制。

所以 ABI 是機器可讀接口，不是安全說明書。

**Event**

Event 是合約向外部系統留下的可索引日誌，是前端、索引器和分析工具的重要數據來源。

合約執行時可以 emit event。事件不會像 storage 那樣直接成為合約可讀取狀態，但很適合讓外部系統追蹤發生過什麼，例如轉帳、訂單創建、參數更新、權限變更。

很多產品頁面並不是每次都直接掃鏈上 storage，而是通過事件索引構建更適合查詢的數據層。

**相關 topic**

```索引（Indexing）```：繼續看事件如何進入 subgraph、數據庫和產品查詢層。

**Upgrade**

合約升級是安全、治理和產品迭代之間的權衡，不能只當成「方便以後改 bug」的開關。

有些合約部署後不可升級，有些通過 proxy、治理或多簽保留升級能力。不可升級更接近「規則固定」，但 bug 修復困難；可升級更靈活，但也引入管理員權限、治理攻擊和用戶信任問題。

判斷升級風險時，可以直接問四個問題：

* 升級權限在誰手裡：單個 EOA、多簽、DAO，還是 timelock 合約？
* 用戶是否能提前看到升級提案和新實現地址？
* 升級能不能改變資產轉移、提款、暫停或權限邏輯？
* 如果管理員金鑰洩漏，最壞結果是什麼？

如果一個協議說「合約已審計」，但沒有說清楚升級權限，這個安全說明仍然是不完整的。

#### 在 AI x Web3 中的位置

AI Agent 進入鏈上執行時，智能合約應該承擔最終規則和約束，而不是把所有判斷交給模型。模型可以幫用戶理解 ABI、生成調用參數、解釋交易結果、寫測試用例，但合約負責執行邊界。

一個穩妥的設計通常是：AI 做建議和編排，錢包做授權確認，合約做可驗證執行，監控系統記錄結果。這樣即使 AI 輸出不穩定，鏈上規則仍然有明確邊界。

#### 最小實踐

做一個最小合約閱讀練習：

* 找一個已驗證源碼的簡單 ERC-20 或 NFT 合約。
* 在區塊瀏覽器裡查看源碼、ABI、事件和最近交易。
* 找出哪些函數會改變狀態，哪些只是讀取狀態。
* 找出合約的權限函數，例如 owner、admin、pause、mint、burn、upgrade。
* 找出最重要的 event，並解釋它對應哪類用戶動作。
* 用一句話解釋：這個合約最重要的風險邊界是什麼。

#### 擴展閱讀
[Solidity Documentation](https://docs.soliditylang.org/)：學習 Solidity 語言、類型、合約結構和安全注意事項。
[Ethereum Smart Contracts](https://ethereum.org/en/developers/docs/smart-contracts/)：從以太坊開發者文檔理解智能合約的基本概念。
[Ethereum Virtual Machine](https://ethereum.org/en/developers/docs/evm/)：理解 EVM 如何執行合約代碼。
[OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)：學習常用安全合約庫和標準實現。
[OpenZeppelin Upgrades](https://docs.openzeppelin.com/upgrades-plugins/)：了解 proxy 升級模式和相關風險。
