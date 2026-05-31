import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8919187732:AAFcf03zyqFUr5vI4ysP-aCe4kxRvv3IU3I"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ref_link = f"https://t.me/cryptoclicker099_bot?start={user.id}"
    keyboard = [
        [InlineKeyboardButton("🎮 Играть", url="https://t.me/cryptoclicker099_bot")],
        [InlineKeyboardButton("👥 Пригласить +500 монет", url=f"https://t.me/share/url?url={ref_link}&text=Играй%20в%20MOONBIT%20и%20зарабатывай%20монеты!")],
        [InlineKeyboardButton("🛒 Магазин", callback_data="shop")],
        [InlineKeyboardButton("📊 Мой баланс", callback_data="balance")],
    ]
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\n\n"
        f"⚡ *MOONBIT* — тапай и зарабатывай!\n\n"
        f"🪙 Тапай монету и копи монеты\n"
        f"🚀 Прокачивай улучшения\n"
        f"👥 Приглашай друзей — получай бонусы\n"
        f"🏆 Стань топ игроком!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def shop_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("⚡ 10,000 монет — 50 Stars", callback_data="buy_10k")],
        [InlineKeyboardButton("💎 50,000 монет — 200 Stars", callback_data="buy_50k")],
        [InlineKeyboardButton("👑 200,000 монет — 500 Stars", callback_data="buy_200k")],
        [InlineKeyboardButton("◀️ Назад", callback_data="back")],
    ]
    await query.edit_message_text(
        "🛒 *Магазин MOONBIT*\n\n"
        "Купи монеты и обгони всех!\n\n"
        "⭐ Оплата через Telegram Stars",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def balance_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("🎮 Играть", url="https://t.me/cryptoclicker099_bot")],
        [InlineKeyboardButton("◀️ Назад", callback_data="back")],
    ]
    await query.edit_message_text(
        "📊 *Твой профиль*\n\n"
        "🪙 Монеты считаются в игре\n"
        "🎮 Открой игру чтобы увидеть баланс\n\n"
        "👆 Тапай быстрее чтобы подняться в топ!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def back_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    ref_link = f"https://t.me/cryptoclicker099_bot?start={user.id}"
    keyboard = [
        [InlineKeyboardButton("🎮 Играть", url="https://t.me/cryptoclicker099_bot")],
        [InlineKeyboardButton("👥 Пригласить +500 монет", url=f"https://t.me/share/url?url={ref_link}&text=Играй%20в%20MOONBIT!")],
        [InlineKeyboardButton("🛒 Магазин", callback_data="shop")],
        [InlineKeyboardButton("📊 Мой баланс", callback_data="balance")],
    ]
    await query.edit_message_text(
        f"👋 Привет, {user.first_name}!\n\n"
        f"⚡ *MOONBIT* — тапай и зарабатывай!\n\n"
        f"🪙 Тапай монету и копи монеты\n"
        f"🚀 Прокачивай улучшения\n"
        f"👥 Приглашай друзей — получай бонусы\n"
        f"🏆 Стань топ игроком!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(shop_handler, pattern="^shop$"))
    app.add_handler(CallbackQueryHandler(balance_handler, pattern="^balance$"))
    app.add_handler(CallbackQueryHandler(back_handler, pattern="^back$"))
    print("Бот запущен!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
