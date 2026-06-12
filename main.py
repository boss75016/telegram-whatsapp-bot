from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

actif = True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot actif ✅")

async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global actif
    actif = False
    await update.message.reply_text("Bot en pause ⏸️")

async def reprendre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global actif
    actif = True
    await update.message.reply_text("Bot redémarré ▶️")

TOKEN = "8989807032:AAFur7RhUPXcEegF6Jpu09rJzFgN09kzMOM"

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pause", pause))
app.add_handler(CommandHandler("reprendre", reprendre))

print("Bot démarré")
app.run_polling()
