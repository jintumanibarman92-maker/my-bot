import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    
    # This checks for the word 'client' in the link
    if args and args[0].lower() == "client":
        photo_path = "photo.jpg"
        caption_text = "Niche Wale Button Pe Click Karke Channel Join Kro Aur Number Shot Se Paisa Kamao Guyss Click Noww !!!"
        
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
        # This is the message for a regular /start or /client command
        photo_path = "photo.jpg"
        caption_text = "Niche Wale Button Pe Click Karke Channel Join Kro Aur Number Shot Se Paisa Kamao Guyss Click Noww !!!"
        
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
            await update.message.reply_text(f"Welcome! Please use the client's invite link to join.")

if __name__ == '__main__':
    # REPLACE THE TOKEN BELOW WITH YOUR ACTUAL BOT TOKEN
    app = ApplicationBuilder().token("6834091453:AAEU6j2n59MnvWfOQQK9HgfF14ERccJoorM").build()

    # These two lines make BOTH commands work
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("client", start))

    print("Client Bot is starting... No errors!")
    app.run_polling()
