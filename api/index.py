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
            payload = {
                "chat_id": chat_id,
                "photo": PHOTO_URL,
                "caption": (
                    "🎰 **RK | CryptoMines**\n"
                    "▔▔▔▔▔▔▔▔▔▔▔▔▔▔\n"
                    "💎 *Real Crypto Mines Game*\n"
                    "⛏️ Find diamonds, avoid bombs\n"
                    "💰 Win USDT by playing!\n"
                    "📌 Minimum Deposit: 10 USDT\n"
                    "🔗 BNB Smart Chain (BEP20)\n\n"
                    "👇 Tap the button below to play!"
                ),
                "parse_mode": "Markdown",
                "reply_markup": {
                    "inline_keyboard": [[{
                        "text": "🎮 Launch Game",
                        "web_app": {"url": GAME_URL}
                    }]]
                }
            }
            requests.post(f"{TELEGRAM_API}/sendPhoto", json=payload)

        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel ke liye handler (ye line zaroori hai)
def handler(request):
    return app(request.environ, start_response)
