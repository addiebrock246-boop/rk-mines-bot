from flask import Flask, request, jsonify
import requests

BOT_TOKEN = "7129346547:AAE2lxZiPNMPTsmjOEQ001AKEp14JuZ1O0g"
GAME_URL = "https://cryptomines.vercel.app"
PHOTO_URL = "https://cryptomines.vercel.app/dia.jpeg"
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
                "✨ **RK | CryptoMines** ✨\n"
                "▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔\n"
                "🎰 *Premium Casino Experience*\n"
                "💎 `Mines Game` — Win Real USDT\n\n"
                "⛏️ Find gems, dodge bombs\n"
                "📈 Multiply your bet instantly\n"
                "🔹 Minimum Deposit: **10 USDT**\n"
                "🔹 Network: *BNB Smart Chain (BEP20)*\n"
                "🔹 Secure | Fair | Instant\n\n"
                "👇 Follow the steps below to play!"
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
                "🌟 **Ready to Start?** 🌟\n\n"
                "Tap the glowing button below to launch your personal casino table.\n"
                "▸ Instant gameplay\n"
                "▸ Real USDT rewards\n"
                "▸ No limits\n\n"
                "⚡ _Powered by RK | CryptoMines_"
            )
            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": premium_text,
                "parse_mode": "Markdown",
                "reply_markup": {
                    "inline_keyboard": [[{
                        "text": "🎮 LAUNCH GAME 🎮",
                        "web_app": {"url": GAME_URL}
                    }]]
                }
            })

        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel ke liye handler
def handler(request):
    return app(request.environ, start_response)
