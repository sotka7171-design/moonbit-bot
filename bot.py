import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8919187732:AAFcf03zyqFUr5vI4ysP-aCe4kxRvv3IU3I"
BOT_USERNAME = "cryptoclicker099_bot"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ref_link = f"https://t.me/{BOT_USERNAME}?start={user.id}"
    keyboard = [
        [InlineKeyboardButton("🎮 Играть", url=f"https://t.me/{BOT_USERNAME}")],
        [InlineKeyboardButton("👥 Пригласить +500 монет", url=f"https://t.me/share/url?url={ref_link}")],
        [InlineKeyboardButton("🛒 Магазин", callback_data="shop")],
    ]
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\n\n"
        f"⚡ *MOONBIT* — тапай и зарабатывай!\n\n"
        f"🪙 Тапай монету и копи монеты\n"
        f"🚀 Прокачивай улучшения\n"
        f"👥 Приглашай друзей — получай бонусы",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def shop_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("⚡ 10,000 монет — 50 Stars", callback_data="buy_10k")],
        [InlineKeyboardButton("💎 50,000 монет — 200 Stars", callback_data="buy_50k")],
        [InlineKeyboardButton("◀️ Назад", callback_data="back")],
    ]
    await query.edit_message_text(
        "🛒 *Магазин MOONBIT*\n\nКупи монеты и обгони всех!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def back_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    ref_link = f"https://t.me/{BOT_USERNAME}?start={user.id}"
    keyboard = [
        [InlineKeyboardButton("🎮 Играть", url=f"https://t.me/{BOT_USERNAME}")],
        [InlineKeyboardButton("👥 Пригласить +500 монет", url=f"https://t.me/share/url?url={ref_link}")],
        [InlineKeyboardButton("🛒 Магазин", callback_data="shop")],
    ]
    await query.edit_message_text(
        f"⚡ *MOONBIT* — тапай и зарабатывай!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(shop_handler, pattern="^shop$"))
    app.add_handler(CallbackQueryHandler(back_handler, pattern="^back$"))
    print("Бот запущен!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
