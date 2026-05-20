"""
AIxWeb3 School — 每日學習推播 Bot
- /notes  → 混合所有課綱，依今日規劃目標隨機生成今日重點
- /goal   → 今日學習目標
- /test   → 5 題知識問答測驗（從 terms.json 隨機抽取，每天盡量不重複）
"""

import os
import json
import random
import anthropic
import time
import requests
from datetime import date, timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

CLAUDE_API_KEY = os.environ["CLAUDE_API_KEY"]
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID        = os.environ["CHAT_ID"]

CURRICULUM_DIR = Path(__file__).parent.parent / "curriculums"
QUIZ_HISTORY   = Path(__file__).parent / "quiz_history.json"
client         = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

# 進行中的測驗 {chat_id: {"questions": [...], "current": int, "score": int}}
quiz_sessions: dict = {}


def load_all_materials() -> dict:
    """讀取 curriculums/ 下所有 .md 檔案，回傳 {檔名: 內容} dict"""
    materials = {}
    for md_file in sorted(CURRICULUM_DIR.glob("*.md")):
        try:
            materials[md_file.stem] = md_file.read_text(encoding="utf-8")
        except Exception:
            pass
    return materials


def get_today_plan() -> str:
    """從 week1.md 中擷取今日規劃段落"""
    try:
        content = (CURRICULUM_DIR / "week1.md").read_text(encoding="utf-8")
        today = date.today()
        today_tag = f"{today.month}/{today.day}"
        lines = content.splitlines()
        start = None
        for i, line in enumerate(lines):
            if line.startswith("### ") and today_tag in line:
                start = i
                break
        if start is None:
            # fallback: 取前 2000 字的本週目標區塊
            return content[:2000]
        section = []
        for line in lines[start:]:
            if section and line.startswith("### "):
                break
            section.append(line)
        return "\n".join(section)[:2000]
    except FileNotFoundError:
        return ""


def sample_sections(materials: dict, n: int = 4) -> str:
    """從所有課綱的 ## 段落中隨機抽取 n 個，回傳合併文字"""
    all_sections = []
    for name, content in materials.items():
        lines = content.splitlines()
        buf = []
        for line in lines:
            if line.startswith("## ") and buf:
                all_sections.append((name, "\n".join(buf)))
                buf = [line]
            elif line.startswith("## "):
                buf = [line]
            else:
                buf.append(line)
        if buf:
            all_sections.append((name, "\n".join(buf)))

    picked = random.sample(all_sections, min(n, len(all_sections)))
    parts = []
    for name, text in picked:
        parts.append(f"【{name}】\n{text[:700]}")
    return "\n\n---\n\n".join(parts)


def ask_claude(prompt: str, max_tokens: int = 700) -> str:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=max_tokens,
        system="你是一個 AIxWeb3 學習助手，用繁體中文，語氣親切簡潔，適合 Telegram 手機閱讀。",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def generate_notes() -> str:
    materials  = load_all_materials()
    today_plan = get_today_plan()
    sampled    = sample_sections(materials, n=4)

    return ask_claude(f"""今天是 {date.today()}。

【今日學習規劃】
{today_plan}

【隨機抽取的課綱片段】
{sampled}

請根據今日規劃目標，從上述課綱片段中挑選最相關的概念，生成今日學習重點。\
每次執行結果應有所不同（因為課綱片段是隨機的）。格式如下（嚴格遵守）：

📝 *今日重點*

1️⃣ [重點一標題]
[一句話說明]

2️⃣ [重點二標題]
[一句話說明]

3️⃣ [重點三標題]
[一句話說明]

---
_AIxWeb3 School · {date.today()}_""")


def generate_goal() -> str:
    today_plan = get_today_plan()
    return ask_claude(f"""根據以下今日學習計畫：

{today_plan}

請列出今日的學習目標，格式如下：

🎯 *今日學習目標*

本週目標：[一句話總結本週大方向]

今日任務：
• [具體任務一]
• [具體任務二]
• [具體任務三]

完成標準：[怎樣算達成今日目標，一句話]

---
_AIxWeb3 School · {date.today()}_""")


def load_terms() -> list[dict]:
    """從 terms.json 載入所有術語，回傳 [{term, definition, category}, ...]"""
    data = json.loads((CURRICULUM_DIR / "terms.json").read_text(encoding="utf-8"))
    terms = []
    for cat in data["categories"]:
        for item in cat["terms"]:
            terms.append({
                "term": item["term"],
                "definition": item["definition"],
                "category": cat["name"],
            })
    return terms


def pick_daily_terms(all_terms: list[dict], n: int = 5) -> list[dict]:
    """挑選 n 個術語，優先選今日尚未出現過的；若不夠才重複使用。"""
    today = str(date.today())
    cutoff = str(date.today() - timedelta(days=6))

    try:
        history: dict = json.loads(QUIZ_HISTORY.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        history = {}

    # 只保留最近 7 天紀錄
    history = {k: v for k, v in history.items() if k >= cutoff}

    used_today = set(history.get(today, []))
    fresh = [t for t in all_terms if t["term"] not in used_today]
    pool = fresh if len(fresh) >= n else all_terms
    selected = random.sample(pool, min(n, len(pool)))

    history.setdefault(today, [])
    history[today] = list(set(history[today]) | {t["term"] for t in selected})
    QUIZ_HISTORY.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")

    return selected


def build_question(term_item: dict, all_terms: list[dict], q_num: int, total: int) -> tuple[str, str]:
    """產生單題選擇題文字，回傳 (題目文字, 正確選項字母 A/B/C/D)。"""
    distractors = random.sample([t for t in all_terms if t["term"] != term_item["term"]], 3)
    choices = [term_item] + distractors
    random.shuffle(choices)

    letters = ["A", "B", "C", "D"]
    correct_letter = letters[choices.index(term_item)]

    lines = [f"❓ *第 {q_num}/{total} 題*\n"]
    lines.append(f"_{term_item['definition']}_\n")
    lines.append("請問這是哪個術語？\n")
    for i, c in enumerate(choices):
        lines.append(f"{letters[i]}. {c['term']}")
    return "\n".join(lines), correct_letter


def start_test(chat_id: str) -> str:
    """初始化測驗 session，回傳第一題文字。"""
    all_terms = load_terms()
    selected  = pick_daily_terms(all_terms, n=5)

    questions = []
    for i, term_item in enumerate(selected, 1):
        q_text, correct = build_question(term_item, all_terms, i, 5)
        questions.append({"text": q_text, "correct": correct, "term": term_item["term"]})

    quiz_sessions[chat_id] = {"questions": questions, "current": 0, "score": 0}
    intro = "🧠 *知識測驗開始！共 5 題，請回覆 A / B / C / D*\n\n"
    return intro + questions[0]["text"]


def handle_quiz_answer(chat_id: str, answer: str) -> str:
    """處理答題，回傳評分結果與下一題（或最終成績）。"""
    session  = quiz_sessions[chat_id]
    idx      = session["current"]
    question = session["questions"][idx]
    correct  = question["correct"]

    if answer == correct:
        session["score"] += 1
        feedback = f"✅ 正確！答案是 *{question['term']}*"
    else:
        feedback = f"❌ 答錯了！正確答案是 {correct}. *{question['term']}*"

    session["current"] += 1

    if session["current"] >= len(session["questions"]):
        score = session["score"]
        total = len(session["questions"])
        del quiz_sessions[chat_id]
        stars = "⭐" * score + "☆" * (total - score)
        return (
            f"{feedback}\n\n"
            f"🏁 *測驗結束！*\n"
            f"得分：{score}/{total}  {stars}\n\n"
            f"{'太棒了，全部答對！🎉' if score == total else '繼續加油，用 /test 再練一次！'}"
        )

    next_q = session["questions"][session["current"]]
    return f"{feedback}\n\n{next_q['text']}"


def send_telegram(chat_id: str, text: str) -> bool:
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    resp = requests.post(url, json={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }, timeout=10)
    return resp.ok


# ── 指令 Polling ─────────────────────────────────────────

COMMANDS = {
    "/notes": generate_notes,
    "/goal":  generate_goal,
}


def poll_commands():
    """長輪詢監聽 Telegram 訊息，處理 /notes、/goal、/test 指令及測驗答題"""
    offset = 0
    print("👂 開始監聽指令（/notes、/goal、/test）...")

    while True:
        try:
            url  = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
            resp = requests.get(url, params={"offset": offset, "timeout": 30}, timeout=35)
            updates = resp.json().get("result", [])

            for update in updates:
                offset = update["update_id"] + 1
                msg     = update.get("message", {})
                text    = msg.get("text", "").strip()
                chat_id = str(msg.get("chat", {}).get("id", ""))

                if not text or not chat_id:
                    continue

                command = text.split()[0].lower()

                # 測驗中：優先處理答題（/test 可重新開始）
                if chat_id in quiz_sessions and command != "/test":
                    ans = text.upper()
                    if ans in ("A", "B", "C", "D"):
                        try:
                            reply = handle_quiz_answer(chat_id, ans)
                            send_telegram(chat_id, reply)
                        except Exception as e:
                            send_telegram(chat_id, f"❌ 發生錯誤：{e}")
                    else:
                        send_telegram(chat_id, "請回覆 A、B、C 或 D 作答，或用 /test 重新開始測驗。")
                    continue

                if command == "/test":
                    print(f"📩 收到指令：/test（chat_id={chat_id}）")
                    try:
                        reply = start_test(chat_id)
                        send_telegram(chat_id, reply)
                    except Exception as e:
                        send_telegram(chat_id, f"❌ 發生錯誤：{e}")

                elif command in COMMANDS:
                    print(f"📩 收到指令：{command}")
                    try:
                        reply = COMMANDS[command]()
                        send_telegram(chat_id, reply)
                    except Exception as e:
                        send_telegram(chat_id, f"❌ 發生錯誤：{e}")

        except Exception as e:
            print(f"⚠️  Polling 錯誤：{e}，5 秒後重試")
            time.sleep(5)


# ── 主程式 ───────────────────────────────────────────────

if __name__ == "__main__":
    print("🤖 AIxWeb3 學習 Bot 啟動")
    print(f"   每日定時推送：已停用")
    print(f"   指令：/notes（今日重點）、/goal（今日學習目標）、/test（知識測驗）")
    print(f"   課綱來源：{CURRICULUM_DIR}")
    print(f"   術語庫：{CURRICULUM_DIR / 'terms.json'}（{len(load_terms())} 個術語）")
    print(f"   載入課綱：{[f.stem for f in sorted(CURRICULUM_DIR.glob('*.md'))]}\n")

    poll_commands()
