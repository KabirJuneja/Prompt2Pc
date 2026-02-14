from executor import execute_action
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import TELEGRAM_BOT_TOKEN, AUTHORIZED_USER_ID
from ai_parser import parse_prompt

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return

    message = update.message.text
    print("Received:", message)

    parsed = parse_prompt(message)
    print("PARSED:", parsed)

    if isinstance(parsed, list):
        for action in parsed:
            execute_action(action)
    else:
        execute_action(parsed)

    await update.message.reply_text("Task executed.")


def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
