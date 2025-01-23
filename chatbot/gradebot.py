from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store student data
students = {
    "1011": "C",
    "202302": "B+",
    "202303": "B",
    "202304": "C",
    "202305": "A+"
}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the Grade Checker Bot!\nEnter your symbol number to check your grade.")

def check_grade(update: Update, context: CallbackContext):
    symbol_number = update.message.text.strip()
    grade = students.get(symbol_number)
    
    if grade:
        update.message.reply_text(f"The grade for symbol number {symbol_number} is: {grade}")
    else:
        update.message.reply_text("Symbol number not found. Please try again.")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = "7382523020:AAEhW-1eDIi9bWQQW2M9lqXjriyjTZl6TkI"

    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Message handler for symbol number input
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_grade))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
