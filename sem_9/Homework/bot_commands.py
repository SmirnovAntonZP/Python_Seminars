from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n')


async def time_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y}={x+y}')