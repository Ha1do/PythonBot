from telegram import *
from telegram.ext import *

#Commands
async def start_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Helo, i am the Ha1do's testing chatbot")

async def help_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("U called about help, so here i am\n"
                              "/start -> starts a bot\n"
                              "/help -> call this message\n"
                              "/pin -> pins a message\n"
                              "/sendmedia -> sends a social media post\n"
                              "/warn -> to warn a user\n"
                              "/kick -> to kick a user\n"
                              "/ban -> to ban a user\n"
                              "/setrules -> set the chat rules\n"
                              "/report -> send report about bot or user\n"
                              "/blacklistadd -> add your word to blacklist\n"
                              "/blacklistremove -> remove word from blacklist\n")

async def pin_command (update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.startswith("/pin") and update.message.message_thread_id is None:
        # если сообщение пользователя на чинается командой "/pin" и он не ответил на другое сообщение...
        await update.message.reply_text("You need to answer on message you want me to pin")

    else:
        text_to_pin: str = update.message.reply_to_message.text
        await update.message.reply_to_message.pin()
        await update.message.reply_text("pinned✅")

async def sendmedia_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("idk what this command must do ¯\_(ツ)_/¯")

async def warn_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    warn_user: str = update.message.text.replace("/warn@Ha1do_bot ", '')
    print(update.message.contact)
    await update.message.reply_text(f"{warn_user} - gets warn 01")

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
