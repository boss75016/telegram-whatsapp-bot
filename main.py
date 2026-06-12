import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

actif = True
contacts_count = 0
message_modele = ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot actif")

async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global actif
    actif = False
    await update.message.reply_text("⏸️ Bot en pause")

async def reprendre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global actif
    actif = True
    await update.message.reply_text("▶️ Bot redémarré")

async def statut(update: Update, context: ContextTypes.DEFAULT_TYPE):
    etat = "Actif" if actif else "En pause"
    await update.message.reply_text(
        f"📊 Statut\n\nÉtat : {etat}\nContacts : {contacts_count}\nMessage configuré : {'Oui' if message_modele else 'Non'}"
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global message_modele

    if not context.args:
        await update.message.reply_text("Utilisation : /message Bonjour {Name}")
        return

    message_modele = " ".join(context.args)
    await update.message.reply_text("📝 Message enregistré")

async def recevoir_fichier(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global contacts_count

    doc = update.message.document

    if not doc.file_name.endswith(".xlsx"):
        await update.message.reply_text("❌ Envoyez un fichier .xlsx")
        return

    fichier = await doc.get_file()
    await fichier.download_to_drive("contacts.xlsx")

    contacts_count = 1
    await update.message.reply_text("📁 Fichier XLSX importé")

TOKEN = os.getenv("8989807032:AAFur7RhUPXcEegF6Jpu09rJzFgN09kzMOM")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pause", pause))
app.add_handler(CommandHandler("reprendre", reprendre))
app.add_handler(CommandHandler("statut", statut))
app.add_handler(CommandHandler("message", message))

app.add_handler(
    MessageHandler(filters.Document.ALL, recevoir_fichier)
)

print("Bot démarré")
app.run_polling()
