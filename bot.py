import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Используй команду /signal <актив>, например /signal eurusd')

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text('Пожалуйста, укажи актив. Пример: /signal eurusd')
        return
    asset = context.args[0].lower()
    if asset in ['eurusd', 'audcad', 'nzdusd']:
        await update.message.reply_text(f'Сигнал для {asset.upper()}: CALL, экспирация 3 минуты')
    else:
        await update.message.reply_text('Неизвестный актив. Попробуй eurusd, audcad или nzdusd.')

if __name__ == '__main__':
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('signal', signal))

    app.run_polling()
