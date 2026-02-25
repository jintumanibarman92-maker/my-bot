import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    # This checks for the word 'client' in the link
    if args and args[0].lower() == "client":
        photo_path = r"c:\Users\hp\Music\photo_6122880209129246050_y.jpg"
        caption_text = "Niche Wale BUtton Pe Click Karke Channel Join Kro Aur Number Shot Se Paisa Kamao Guyss Click NOWW !!! 👇"
        
        # Client's Specific Button and Link
        keyboard = [[InlineKeyboardButton("JOIN NOW", url="https://t.me/+QKLXn92Z_sY1Yjk1")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        try:
            with open(photo_path, 'rb') as photo_file:
                await update.message.reply_photo(
                    photo=photo_file,
                    caption=caption_text,
                    reply_markup=reply_markup
                )
        except Exception as e:
            await update.message.reply_text(f"Error opening photo: {e}")
    else:
        await update.message.reply_text("Welcome! Please use the client's invite link to join.")

if __name__ == '__main__':
    # YOUR NEW CLIENT API TOKEN
    TOKEN = "6834091453:AAETYz-uUfCk33TthWfX-ftN79mRfL_ylmY"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Client Bot is starting... No errors!")
    app.run_polling()
