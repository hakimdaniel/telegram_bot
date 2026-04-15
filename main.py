# represent semua data dari Telegram (message, command, user info)
from telegram import Update

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# ApplicationBuilder → “engine” utama bot
# CommandHandler → handle command macam /start
# ContextTypes → bantu akses context (data tambahan bot)

from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv("TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/getMe"
resp = requests.get(url)
data = resp.json()

# library moden wajib aynsc await tunggu response input output server side telegram
# function start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = await context.bot.get_me()
    await update.message.reply_text(f"Hello, saya {bot.first_name} bot telegram anda 🚀\n/help")

# function help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Takde apa saya boleh buat, hanya /start je")

# buat bot application dengan setup di atas
app = ApplicationBuilder().token(TOKEN).build()

# register command with function

# command /start akan call function start()
app.add_handler(CommandHandler("start", start))
# command /help akan call function help()
app.add_handler(CommandHandler("help", help_command))

# run bot
try:
    print("Bot is now running...")
    print(f"Access bot at https://t.me/{data["result"]["username"]}?start=start")
    app.run_polling()
except Exception as e:
    print(f"Error: {e}")