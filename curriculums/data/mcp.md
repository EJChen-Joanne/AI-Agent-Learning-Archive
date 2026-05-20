### 模型上下文協議（MCP）

MCP 試圖把模型和外部工具、數據源、應用上下文之間的連接標準化。它解決的不是「模型會不會更聰明」，而是「模型如何以可描述、可復用、可管理的方式使用外部能力」。

#### 為什麼要學這個

AI 應用真正進入工作流後，模型不可能只靠 prompt 裡的文本完成任務。它需要讀取文件、查數據庫、訪問文檔、調用 API、操作工具、拿到用戶上下文。

如果每個應用都用自己的方式接工具，Agent 生態會非常碎：同一個工具要為不同客戶端寫很多適配層，權限、schema、錯誤處理和日誌也難統一。

MCP 的價值在於把這層連接抽象成協議。你可以把它理解成 AI 應用的「工具接口標準」：客戶端負責和模型交互，server 負責暴露資源、工具和 prompts。

#### 第一性原理

模型不應該直接擁有世界；它應該通過明確協議訪問被授權的上下文和工具。
MCP 的關鍵不是「能接更多工具」，而是讓工具接入變得可描述、可發現、可限制。一個 server 暴露了什麼能力，輸入 schema 是什麼，返回什麼結果，哪些動作有副作用，都應該被清楚表達。

* 工具要有 schema：沒有 schema，模型調用工具就會變成自然語言猜參數。
* 權限要在協議外也成立：協議能描述能力，但真正的授權、審計和隔離仍要由系統實現。
* 錯誤要可傳遞：工具失敗、超時、權限不足，必須明確返回，而不是讓模型猜。

#### 知識節點

**Server**

MCP Server 是提供能力的一側。它可以暴露 resources、tools、prompts 等，讓 AI 客戶端讀取資訊或調用動作。

Server 的設計重點是邊界：

* 暴露哪些資源。
* 哪些工具只讀，哪些有副作用。
* 參數 schema 是否清楚。
* 錯誤如何返回。
* 是否需要用戶授權。
* 日誌和審計在哪裡記錄。

一個不加限制的 MCP server，很容易把本地文件、內部 API 或高風險動作暴露給模型。

**Client**

MCP Client 是連接模型和 MCP server 的一側，比如桌面應用、IDE、Agent runtime 或聊天客戶端。

Client 負責發現 server 能力，把工具資訊交給模型，並把模型生成的調用請求轉回協議消息。它也應該負責用戶確認、權限提示、會話隔離和工具調用展示。

判斷一個 client 是否可靠，重點看它是否讓用戶知道：當前連接了哪些 server，模型能調用哪些工具，調用前是否需要確認。

**Tool Schema**

Tool Schema 描述工具名字、用途、參數、返回值和約束。它是模型正確調用工具的關鍵。

好的 schema 不只是字段類型，還要說明：

* 這個工具什麼時候用。
* 參數代表什麼。
* 哪些字段必填。
* 是否會修改外部狀態。
* 失敗時返回什麼。

Tool schema 寫得模糊，模型就會用錯誤參數填空。

**相關 topic**

```提示詞（Prompt）```：工具描述本質上也是 prompt 的一部分。
```智能體（Agent）```：Agent 的工具調用能力必須和狀態、權限、停止條件一起設計。

**Permission**

Permission 是 MCP 真正進入產品時最容易被低估的問題。

MCP 讓工具連接更方便，但方便不等於安全。讀一個文檔、查一個 issue、創建一個 PR、發一筆支付、刪除一個文件，這些動作風險完全不同。

Permission 至少要區分：

* 只讀還是寫入。
* 當前會話授權還是長期授權。
* 是否需要用戶確認。
* 是否能訪問敏感資訊。
* 是否會產生外部副作用。
* 是否可撤銷和審計。

MCP server 暴露能力之前，應該先定義權限模型。

#### 在 AI x Web3 中的位置

MCP 在 AI x Web3 中可以作為 Agent 連接鏈上工具和開發工具的接口層。例如讀取區塊瀏覽器、查詢合約文檔、調用 RPC、生成交易草稿、讀取項目 issue。

但 MCP 本身不是錢包安全方案。它可以標準化工具入口，不能替代帳戶權限、交易模擬、簽名確認、session key 和審計日誌。

比較穩的設計是：MCP 負責工具發現和調用格式；Web3 帳戶系統負責最終權限和執行邊界。

#### 最小實踐

做一個只讀 MCP server。

它只暴露兩個工具：

* `search_docs(query)`：搜索本地項目文檔。
* `get_file(path)`：讀取白名單目錄裡的文件。

要求：

* 不能讀取白名單外路徑。
* 返回結果必須帶來源路徑。
* 工具調用要寫日誌。
* 錯誤要明確返回，而不是靜默失敗。

完成後，再設計一個「寫入工具」的權限升級方案：什麼時候需要用戶確認，如何撤銷授權，如何審計每次調用。

#### 擴展閱讀
[Model Context Protocol Architecture](https://modelcontextprotocol.io/docs/concepts/architecture)：官方架構說明，適合理解 client、server、tools、resources 的分工。
[Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)：協議原文，適合查看消息格式和 JSON-RPC 基礎。
[OpenAI MCP Overview](https://platform.openai.com/docs/guides/tools-mcp)：了解 OpenAI API / ChatGPT 生態如何接入 MCP server。
[Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp)：看 MCP 在本地開發工具中的使用方式。
[GitHub: modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)：官方文檔倉庫，適合跟蹤文檔和規範變化。
