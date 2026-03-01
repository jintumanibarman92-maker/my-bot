import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This is the message for BOTH /start and /client commands
    photo_path = "photo.jpg"
    
    # We use ** to make text BOLD
    caption_text = (
        "**Niche Wale Button Pe Click Karke Channel Join Kro Aur Number Shot Se Paisa Kamao Guyss Click Noww !!!** 👇🚀💰"
    )
    
    # Button with Emoji
    keyboard = [[InlineKeyboardButton("✅ JOIN NOW ✅", url="https://t.me/+lRsgf2FFf4s0Mzc1")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        with open(photo_path, 'rb') as photo_file:
            await update.message.reply_photo(
                photo=photo_file,
                caption=caption_text,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
    except Exception as e:
        # If photo fails, send text with emojis and bold
        await update.message.reply_text(
            f"**Welcome! Please join here:** https://t.me/+QKLXn92Z_sY1Yjk1 🚀💰",
            parse_mode='Markdown'
        )

if __name__ == '__main__':
    # Your token is already added here
    app = ApplicationBuilder().token("6834091453:AAEU6j2n59MnvWfOQQK9HgfF14ERccJoorM").build()

    # These lines make BOTH commands work
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("client", start))

    print("Bot is starting... No errors!")
    app.run_polling()
