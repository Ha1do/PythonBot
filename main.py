from telegram import *
from telegram.ext import *

API_TOKEN = '1256415211:AAGQfWloyT0H91OrMlmfsM17IUFS7YVmDWg'
BOT_USERNAME = "@Ha1do_bot"

#Commands
async def start_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello")

async def help_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("U called about help, so here i am"
                              "/start -> starts a bot"
                              "/help -> call this message"
                              "/pin -> pins a message"
                              "/sendmedia -> sends a social media post"
                              "/warn"
                              "/kick"
                              "/ban"
                              "/setrules"
                              "/report"
                              "/blacklistadd"
                              "/blacklistremove")

async def pin_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("pinned text XD")

async def sendmedia_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("i must send some social media but now i can't")

async def warn_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("let's think i waned u")

async def kick_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("i think now u can't be here, but if u already there - u can stay")

async def ban_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("BAN-HAMMER")

async def setrules_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("i gess, now u need to set rules but don't do this pls")

async def report_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("report LOL")

async def blacklistadd_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("suka will never be in black list")

async def blacklistremove_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Хайдо п*дор will never be removed from black list")

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
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("pin", pin_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    # app.add_handler(error)

    print("Polling (checking for updates in chat)")
    app.run_polling(poll_interval=1)