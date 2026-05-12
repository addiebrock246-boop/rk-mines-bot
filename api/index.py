import json
from http import HTTPStatus
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# ========== TERI DETAILS ==========
BOT_TOKEN = "7129346547:AAE2lxZiPNMPTsmjOEQ001AKEp14JuZ1O0g"   # naya token
GAME_URL = "https://cryptomines.vercel.app"                # tera game (Vercel)
PHOTO_URL = "https://cryptomines.vercel.app/dia.jpeg"      # photo

application = Application.builder().token(BOT_TOKEN).build()
initialized = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=PHOTO_URL,
        caption=(
            "🎰 **RK | CryptoMines**\n"
            "▔▔▔▔▔▔▔▔▔▔▔▔▔▔\n"
            "💎 *Real Crypto Mines Game*\n"
            "⛏️ Find diamonds, avoid bombs\n"
            "💰 Win USDT by playing!\n"
            "📌 Minimum Deposit: 10 USDT\n"
            "🔗 BNB Smart Chain (BEP20)\n\n"
            "👇 Tap the button below to play!"
        ),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🎮 Launch Game", web_app=WebAppInfo(url=GAME_URL))
        ]])
    )

application.add_handler(CommandHandler("start", start))

async def handler(request):
    global initialized
    # Vercel Python runtime ke liye handler
    if not initialized:
        await application.initialize()
        initialized = True

    if request.method == "POST":
        try:
            body = await request.json()
            update = Update.de_json(body, application.bot)
            await application.process_update(update)
            return {
                "statusCode": HTTPStatus.OK,
                "body": json.dumps({"ok": True})
            }
        except Exception as e:
            return {
                "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
                "body": json.dumps({"error": str(e)})
            }
    else:
        return {
            "statusCode": HTTPStatus.METHOD_NOT_ALLOWED,
            "body": "Use POST method"
        }
