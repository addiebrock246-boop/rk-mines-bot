from flask import Flask, request, jsonify
import requests

BOT_TOKEN = "8949298635:AAEY8_h8CWXv5Xrcls5_OLGUIpfXKYB3gd8"
GAME_URL = "https://cryptomines.vercel.app"
PHOTO_URL = "https://rk-mines-bot.vercel.app/bomber.jpeg"
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
            # ── 1. PREMIUM PHOTO ──
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

            # ── 2. COUNTRY INFO ──
            country_info = (
                "🌍 **Default = Everyone Plays!** 🌍\n\n"
                "The **Default** section is your universal entry — no matter where you are "
                "in the world, you can jump in, deposit USDT, and start mining gems. 💎\n\n"
                "🎨 **Custom Layouts for 8 Countries**\n"
                "We built stunning, dedicated designs for 8 gambling powerhouses:\n"
                "🇺🇸 United States\n"
                "🇬🇧 United Kingdom\n"
                "🇦🇺 Australia\n"
                "🇮🇳 India\n"
                "🇵🇰 Pakistan\n"
                "🇲🇨 Monaco\n"
                "🇪🇸 Spain\n"
                "🇫🇷 France\n\n"
                "These nations live & breathe gambling — that's why they've earned their "
                "own premium look inside the game. 🏆\n\n"
                "💡 *Want your country's flag in the game?*\n"
                "Play more, invite your squad, and show us your volume. "
                "The more you grind, the faster your country gets its own design. 🚀\n\n"
                "⚡ _RK | CASH MINES — Built for Winners_"
            )
            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": country_info,
                "parse_mode": "Markdown"
            })

            # ── 3. GAME BUTTON ──
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

        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel ke liye handler
def handler(request):
    return app(request.environ, start_response)
