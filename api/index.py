from flask import Flask, request, jsonify
import requests

BOT_TOKEN = "8949298635:AAEY8_h8CWXv5Xrcls5_OLGUIpfXKYB3gd8"   # ⬅️ नया टोकन
GAME_URL = "https://cryptomines.vercel.app"
PHOTO_URL = "https://cryptomines.vercel.app/bomber.jpeg"       # ⬅️ bomber.jpeg इमेज
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def webhook():
    try:
        body = request.get_json()
        msg = body.get("message", {})
        chat_id = msg.get("chat", {}).get("id")
        text = (msg.get("text") or "").strip()

        if text == "/start" and chat_id:
            # ═══════════════════════════════════════
            # 1. PREMIUM PHOTO with stylish caption
            # ═══════════════════════════════════════
            photo_caption = (
                "💥 **RK | CASH MINES** 💥\n"
                "▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔\n"
                "🎰 *Premium Casino Game*\n"
                "💎 **Mines Game** — Win Real USDT\n\n"
                "⛏️ Find gems, dodge bombs\n"
                "📈 Multiply your bet instantly\n"
                "🔹 Minimum Deposit: **10 USDT**\n"
                "🔹 Network: *BNB Smart Chain (BEP20)*\n"
                "🔹 Secure | Fair | Instant Withdrawals\n\n"
                "👇 Tap the glowing button to enter the game!"
            )
            requests.post(f"{TELEGRAM_API}/sendPhoto", json={
                "chat_id": chat_id,
                "photo": PHOTO_URL,
                "caption": photo_caption,
                "parse_mode": "Markdown"
            })

            # ═══════════════════════════════════════
            # 2. SEPARATE MESSAGE with Game Button
            # ═══════════════════════════════════════
            premium_text = (
                "🌟 **Ready to Play?** 🌟\n\n"
                "Tap the glowing button below to launch **Cash Mines**.\n"
                "▸ Instant gameplay\n"
                "▸ Real USDT rewards\n"
                "▸ No limits – just pure luck\n\n"
                "⚡ _Powered by RK | CASH MINES_"
            )
            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": premium_text,
                "parse_mode": "Markdown",
                "reply_markup": {
                    "inline_keyboard": [[{
                        "text": "🔥 LAUNCH CASH MINES 🔥",
                        "web_app": {"url": GAME_URL}
                    }]]
                }
            })

            # ═══════════════════════════════════════
            # 3. CURRENCY AVAILABILITY STATUS
            # ═══════════════════════════════════════
            currency_info = (
                "⚠️ **Filhaal (Currently) Only USDT (Default) Works!**\n\n"
                "Baaki currencies jald aayengi (Coming Soon):\n"
                "🇺🇸 USD — Coming Soon\n"
                "🇬🇧 GBP — Coming Soon\n"
                "🇦🇺 AUD — Coming Soon\n"
                "🇮🇳 INR — Coming Soon\n"
                "🇵🇰 PKR — Coming Soon\n"
                "🇲🇨 EUR (Monaco) — Coming Soon\n"
                "🇪🇸 EUR (Spain) — Coming Soon\n\n"
                "💡 *Deposit sirf **Default (USDT)** select karein.*"
            )
            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": currency_info,
                "parse_mode": "Markdown"
            })

        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel ke liye handler (optional, agar Vercel pe deploy karna ho to)
def handler(request):
    return app(request.environ, start_response)
