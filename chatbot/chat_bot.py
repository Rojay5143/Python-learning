from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Dictionary to store user data
user_data = {}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Information Bot! Use /setinfo to add information and /getinfo to retrieve it."
    )

# Set information command
async def setinfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id

    # Check if data is provided
    if len(context.args) < 3:
        await update.message.reply_text(
            "Usage: /setinfo <bank_ac_no> <address> <personal_pan>"
        )
        return

    # Parse data from arguments
    bank_ac_no = context.args[0]
    address = context.args[1]
    personal_pan = context.args[2]

    # Store in dictionary
    user_data[user_id] = {
        "bank_ac_no": bank_ac_no,
        "address": address,
        "personal_pan": personal_pan,
    }
    await update.message.reply_text("Information saved successfully!")

# Get information command
async def getinfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id

    if user_id in user_data:
        info = user_data[user_id]
        response = (
            f"Your Information:\n"
            f"Bank Account No: {info['bank_ac_no']}\n"
            f"Address: {info['address']}\n"
            f"Personal PAN: {info['personal_pan']}"
        )
    else:
        response = "No information found. Use /setinfo to add your information."

    await update.message.reply_text(response)

# Main function
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = "7382523020:AAEhW-1eDIi9bWQQW2M9lqXjriyjTZl6TkI"

    # Create the application
    application = ApplicationBuilder().token(bot_token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("setinfo", setinfo))
    application.add_handler(CommandHandler("getinfo", getinfo))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
