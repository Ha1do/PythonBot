from telegram import *
from telegram.ext import *
import Commands

API_TOKEN = '1256415211:AAGQfWloyT0H91OrMlmfsM17IUFS7YVmDWg'
BOT_USERNAME = "@Ha1do_bot"

#Response
def handle_response (text: str) -> str:
    processed: str = text.lower()
    if 'hi' in processed:
        return "hi"
    if "hello" in processed:
        return 'hi, bitch'
    return "Нормально напиши шо ты хочешь, нихуя не понял"

async def handle_message (update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    if message_type == "supergroup":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot", response)
    await update.message.reply_text(response)

async def error (update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} привел к ошибке {context.error}")

if __name__ == "__main__":
    print("bot started")
    app = Application.builder().token(API_TOKEN).build()

    #Commands
    app.add_handler(CommandHandler("start", Commands.start_command))
    app.add_handler(CommandHandler("help", Commands.help_command))
    app.add_handler(CommandHandler("pin", Commands.pin_command))
    app.add_handler(CommandHandler("sendmedia", Commands.sendmedia_command))
    app.add_handler(CommandHandler("warn", Commands.warn_command))
    app.add_handler(CommandHandler("kick", Commands.kick_command))
    app.add_handler(CommandHandler("ban", Commands.ban_command))
    app.add_handler(CommandHandler("setrules", Commands.setrules_command))
    app.add_handler(CommandHandler("report", Commands.report_command))
    app.add_handler(CommandHandler("blacklistadd", Commands.blacklistadd_command))
    app.add_handler(CommandHandler("blacklistremove", Commands.blacklistremove_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    # app.add_handler(error)

    print("Polling (checking for updates in chat)")
    app.run_polling(poll_interval=1)