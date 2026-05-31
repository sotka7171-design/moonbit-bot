import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8919187732:AAFcf03zyqFUr5vI4ysP-aCe4kxRvv3IU3I"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [[
        InlineKeyboardButton("🎮 Играть", url="https://t.me/crypto_clicker_moonbit_bot"),
    ],[
        InlineKeyboardButton("👥 Пригласить друга", url="https://t.me/share/url?url=https://t.me/crypto_clicker_moonbit_bot"),
    ],[
        InlineKeyboardButton("🛒 Магазин", callback_data="shop"),
    ]]
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\n\n"
        f"⚡ *MOONBIT* — тапай и зарабатывай!\n\n"
        f"🎮 Нажми играть и начни добывать монеты",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def shop_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [[
        InlineKeyboardButton("⚡ 10,000 монет — 50 Stars", callback_data="buy_10k"),
    ],[
        InlineKeyboardButton("💎 50,000 монет — 200 Stars", callback_data="buy_50k"),
    ]]
    await query.edit_message_text(
        "🛒 *Магазин MOONBIT*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(shop_handler, pattern="shop"))
    app.run_polling()

if __name__ == "__main__":
    main()
