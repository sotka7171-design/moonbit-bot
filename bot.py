import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8919187732:AAFcf03zyqFUr5vI4ysP-aCe4kxRvv3IU3I"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ref_id = context.args[0] if context.args else None
    
    ref_link = f"https://t.me/{context.bot.username}?start={user.id}"
    
    keyboard = [[
        InlineKeyboardButton("🎮 Играть", web_app={"url": "https://moonbit.vercel.app"}),
    ],[
        InlineKeyboardButton("👥 Пригласить друга", switch_inline_query=f"Играй в MOONBIT! {ref_link}"),
    ],[
        InlineKeyboardButton("🛒 Магазин", callback_data="shop"),
    ]]
    
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\n\n"
        f"⚡ *MOONBIT* — тапай и зарабатывай монеты!\n\n"
        f"🎮 Нажми кнопку чтобы начать игру\n"
        f"👥 Приглашай друзей и получай бонусы",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = [[
        InlineKeyboardButton("⚡ 10,000 монет — 50 Stars", callback_data="buy_10k"),
    ],[
        InlineKeyboardButton("💎 50,000 монет — 200 Stars", callback_data="buy_50k"),
    ],[
        InlineKeyboardButton("👑 200,000 монет — 500 Stars", callback_data="buy_200k"),
    ]]
    
    await query.edit_message_text(
        "🛒 *Магазин MOONBIT*\n\nКупи монеты и обгони всех!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(shop, pattern="shop"))
    app.run_polling()

if __name__ == "__main__":
    main()
