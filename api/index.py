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

            # ── 3. DETAILED GAME INFO (NEW) ──
            detailed_info = (
                "🔥 **RK | CASH MINES** – A premium crypto casino game that turns your luck into real USDT rewards.\n\n"
                "---\n\n"
                "### 💰 Why Play Cash Mines?\n"
                "- **💵 Real USDT Wins:** Every win is instantly added to your gaming balance as USDT – no fake points, just real earnings.  \n"
                "- **⚡️ Instant Rewards:** Cash out anytime and your winnings are immediately credited to your balance, ready for withdrawal.  \n"
                "- **🎯 Simple & Addictive:** The rules are easy – find gems, avoid bombs. A perfect mix of skill and luck.  \n"
                "- **🔒 Secure & Transparent:** The game logic (multiplier) is fully transparent. No scams, just pure math.  \n"
                "- **💎 Low Entry:** Start with as little as **10 USDT** and increase your bet to chase higher multipliers.  \n"
                "- **🌍 Multilingual:** Play in English, Hindi, Urdu, Spanish or French.  \n"
                "- **🎨 Unique Country Layouts:** Choose your country and experience a custom-designed theme – built specially for the world’s biggest gambling nations.  \n"
                "- **💰 Withdraw Anytime:** Cash out your earnings directly to your BSC (BEP20) USDT wallet address (minimum withdrawal: **200 USDT**).\n\n"
                "---\n\n"
                "### 🌍 Supported Countries & Custom Designs\n"
                "The game now features **8 dedicated country layouts**, crafted for the most passionate gambling communities on the planet:  \n"
                "🇺🇸 United States · 🇬🇧 United Kingdom · 🇦🇺 Australia · 🇮🇳 India · 🇵🇰 Pakistan · 🇲🇨 Monaco · 🇪🇸 Spain · 🇫🇷 France  \n\n"
                "**💡 Don't see your flag yet?**  \n"
                "The more you play and the higher your volume, the faster we add new countries. Keep grinding, invite your friends, and your country could be next!  \n\n"
                "**🔹 One Currency, One Balance:** No matter which country you select, everything runs on **USDT**. Your balance is shared across all regions – deposit once, play anywhere.\n\n"
                "---\n\n"
                "### 📖 How to Play Cash Mines – Step by Step\n\n"
                "**1. Deposit Funds**  \n"
                "- Tap the **\"Add Funds\"** button.  \n"
                "- Enter the amount of USDT you wish to deposit (minimum **10 USDT**).  \n"
                "- You’ll be taken to a secure crypto checkout page where you pay with USDT on the **BNB Smart Chain (BEP20)**.  \n"
                "- Your deposit will be instantly credited to your balance – visible in **USDT** no matter which country you’re viewing.\n\n"
                "**2. Set Your Bet & Bombs**  \n"
                "- **Amount Bet (USDT):** Choose how much USDT you want to wager (minimum 10 USDT).  \n"
                "- **Bombs:** Pick between **1 and 15** bombs. More bombs mean a higher multiplier, but also a higher risk of hitting one.\n\n"
                "**3. Start the Game**  \n"
                "- Hit the **\"🔥 START BET\"** button. A 5×5 grid of 25 hidden tiles will appear.  \n"
                "- Some tiles hide gleaming gems 💎, others hide deadly bombs 💣.\n\n"
                "**4. Click Tiles**  \n"
                "- Tap any tile to reveal it.  \n"
                "- **If it’s a gem:** Your potential win multiplies! The multiplier increases with each gem found.  \n"
                "- **If it’s a bomb:** Game over – you lose your bet.\n\n"
                "**5. Cash Out**  \n"
                "- At any point, press the **\"💰 Cashout\"** button to collect your winnings (bet × current multiplier).  \n"
                "- Or keep finding gems to raise the multiplier – but don’t get greedy, or a bomb might end it all!\n\n"
                "**6. Withdraw Your Winnings**  \n"
                "- Go to the **Withdrawal** section, enter your **BSC (BEP20) USDT wallet address** and the amount you want to withdraw (**minimum 200 USDT**).  \n"
                "- Submit the request and your funds will be transferred.\n\n"
                "---\n\n"
                "Good luck, and may the gems be with you! 💎"
            )
            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": detailed_info,
                "parse_mode": "Markdown"
            })

            # ── 4. GAME BUTTON ──
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
