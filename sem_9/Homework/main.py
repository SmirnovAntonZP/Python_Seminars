from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("time", time_com))
app.add_handler(CommandHandler("help", help_com))
app.add_handler(CommandHandler("sum", sum_comm))

print('server on')
app.run_polling()