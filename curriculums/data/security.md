### 安全（Security）

Web3 安全不是上線前找人審一次代碼，而是從合約設計、權限、測試、交易模擬、監控、應急暫停到權限撤銷的一整套工程流程。

#### 為什麼要學這個

鏈上系統的錯誤成本比普通應用高。合約一旦部署，資產可能已經進入協議，攻擊者可以直接和公開接口交互，交易執行結果也通常不能隨意回滾。

安全不是只屬於 auditor 的工作。產品、前端、後端、合約、運營和 AI Agent 都會影響安全邊界：一個錯誤授權按鈕、一個無限 approve、一個不受限的 Agent tool、一條沒模擬的交易，都可能變成事故入口。

Web3 安全的核心不是「沒有 bug」，而是把可預見風險盡量擋在執行前，並在執行後能快速發現和止損。

#### 第一性原理

鏈上系統默認暴露在公開對抗環境裡，任何可調用路徑都要按攻擊面看待。
普通後端可以靠權限、網路隔離、人工回滾和數據庫修復兜底。合約不同：代碼公開，狀態公開，資金公開，攻擊者可以反覆模擬和搶跑。

* 權限必須最小化：owner、admin、upgrade、pause、withdraw 都要有清楚邊界。
* 執行前要模擬：交易能不能成功、會改什麼資產、會調用哪些合約，都要盡量提前看見。
* 上線後要監控：安全不是部署那一刻結束，異常轉帳、參數變更、失敗交易和價格波動都要持續觀察。

#### 知識節點

**Reentrancy**

Reentrancy 是合約在外部調用未完成前被再次調用，導致狀態被重複利用的經典漏洞。

最常見的模式是：合約先向外部地址轉帳或調用外部合約，然後才更新內部餘額。惡意合約可以在回調中再次進入原函數，在餘額歸零前重複提款。

防護思路包括：

* 使用 Checks-Effects-Interactions：先檢查，再更新狀態，最後外部調用。
* 對高風險函數使用 reentrancy guard。
* 避免在狀態未更新前調用不可信合約。
* 測試多合約交互，而不是只測單個函數。

**相關 topic**

```Solidity Security Considerations```：官方安全注意事項，包含 reentrancy、gas、隨機數和合約交互風險。
```OpenZeppelin Utils```：查看 ReentrancyGuard、Pausable 等常用安全工具。

**Access Control**

Access Control 決定誰能執行敏感動作，是合約安全裡最常見也最容易被低估的部分。

敏感動作包括 mint、burn、pause、upgrade、withdraw、setOracle、setFee、setRouter、changeOwner。任何一個權限過寬，都可能讓協議規則被管理員或攻擊者改寫。

檢查權限時，不要只問「有沒有 onlyOwner」。更要問：

* owner 是 EOA、多簽還是治理合約？
* 是否有 timelock？
* 角色能否相互授予？
* 權限變更是否發出 event？
* 緊急暫停和恢復由誰控制？
* 私鑰洩漏時最壞結果是什麼？

**Audit**

Audit 是外部安全審查，不是安全保證書。

審計可以發現設計、實現和測試中的問題，但它不能保證協議永遠安全。審計範圍、代碼版本、依賴版本、部署參數、升級權限、上線後的改動，都會影響結論。

閱讀 audit report 時至少看：

* 審計覆蓋了哪些 commit 和合約。
* 哪些問題已修復，哪些被項目方接受風險。
* 是否覆蓋經濟機制和外部依賴。
* 是否包含測試建議和部署注意事項。
* 上線代碼是否和審計代碼一致。

**Simulation**

Simulation 是交易發出前的預演，用來發現執行失敗、資產變化異常和權限越界。

在用戶或 Agent 簽名前，系統可以模擬交易：調用哪個合約、會轉出哪些 token、會得到什麼、gas 大概多少、是否 revert、是否觸發授權變化。

Simulation 不能替代安全審計，因為真實鏈狀態可能在交易打包前變化。但它能擋住很多明顯錯誤：鏈 ID 錯、合約地址錯、授權額度異常、滑點過大、餘額不足、調用方法不符合預期。

**相關 topic**

```Tenderly Simulations```：了解交易模擬、資產變化和執行 trace 如何用於調試和風控。

**Monitoring**

Monitoring 是上線後的安全感知層，用來發現異常並觸發響應。

鏈上監控可以關注：

* 大額轉帳或提款。
* 管理員權限變更。
* 合約升級。
* 預言機價格異常。
* 大量失敗交易。
* TVL 快速流出。
* 未預期的 event。
* Agent 連續觸發高風險工具。

監控本身還不夠。真正有效的是「監控 + 響應」：誰收到告警，誰能 pause，誰確認誤報，恢復流程是什麼。

#### 在 AI x Web3 中的位置

AI 會讓安全邊界更複雜。Agent 可以解釋合約、生成交易、調用工具、執行策略，但它也可能讀錯上下文、被 prompt injection 影響、調用錯誤工具或生成危險交易。

所以 AI x Web3 的安全設計要把模型輸出和鏈上執行分開：模型可以建議，工具返回事實，policy 限制權限，simulation 預演結果，human check 確認高風險動作，monitoring 記錄執行後果。

#### 最小實踐

做一個交易安全檢查表：

* 選擇一筆公開的合約調用交易。
* 查看 from、to、method、value、token transfers、logs 和 gas used。
* 判斷這筆交易是否改變權限、資產或關鍵協議參數。
* 寫出如果這筆交易由 Agent 發起，執行前要做哪些 simulation 和 human check。
* 寫出上線後應該監控哪些 event 或異常指標。

#### 擴展閱讀
[Solidity Security Considerations](https://docs.soliditylang.org/en/latest/security-considerations.html)：官方安全注意事項，適合建立合約安全基礎。
[OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)：學習常用安全組件、訪問控制和標準合約實現。
[OpenZeppelin Utils](https://docs.openzeppelin.com/contracts/api/utils)：查看 ReentrancyGuard、Pausable、Nonces 等工具。
[Ethereum Smart Contract Security](https://ethereum.org/en/developers/docs/smart-contracts/security/)：從以太坊開發者文檔理解常見安全實踐。
[Tenderly Simulations](https://docs.tenderly.co/simulations/)：學習交易模擬和執行 trace 如何幫助排查風險。
