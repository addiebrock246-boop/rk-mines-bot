import json
import requests

BOT_TOKEN = "7129346547:AAE2lxZiPNMPTsmjOEQ001AKEp14JuZ1O0g"
GAME_URL = "https://cryptomines.vercel.app"
PHOTO_URL = "https://cryptomines.vercel.app/dia.jpeg"

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def handler(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
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
                    "reply_markup": json.dumps({
                        "inline_keyboard": [[{
                            "text": "🎮 Launch Game",
                            "web_app": {"url": GAME_URL}
                        }]]
                    })
                }
                requests.post(f"{TELEGRAM_API}/sendPhoto", json=payload)
            return {"statusCode": 200, "body": json.dumps({"ok": True})}
        except Exception as e:
            return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
    else:
        return {"statusCode": 405, "body": "Method Not Allowed"}
