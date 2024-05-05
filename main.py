
from dotenv import load_dotenv
load_dotenv()
import os
from telegram import Update, ForceReply
from telegram.constants import ParseMode
from telegram.ext import Application, Updater, ContextTypes, MessageHandler, CommandHandler, filters, CallbackQueryHandler, CallbackContext
from keyboard.eth_keyboard import Keyboard
from config import logger
from wallet.eth_wallet import Wallet

TOKEN  = os.getenv('TOKEN')
TOKEN_NAME = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = Keyboard.ethereum_menu_keyboard()
    private_key, eth_balance, balance_in_dollars = await Wallet.new_wallet()
    message_text = f"""
        <b>Welcome to Unibot on Ethereum</b>\n
        Introducing a cutting-edge bot crafted exclusively for Ethereum traders. Trade any token instantly right after launch.
        
        Here's your Ethereum wallet address linked to your Telegram Account. Simply fund your wallet and dive into trading.\n\n<b>Ethereum</b>\n<code>{private_key}</code> (Tap to copy) \nBalance: <b>{balance_in_dollars}</b> Eth (<b>${eth_balance}</b>)
        
Click on the Refresh button to update your balance.
    """
    await update.message.reply_text(
        text=message_text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )

async def sol_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = Keyboard.solana_menu_keyboard()
    query = update.callback_query
    await query.answer()
    message_text =f"""
        <b>Welcome to Unibot on Ethereum</b>\n
        Introducing a cutting-edge bot crafted exclusively for Ethereum traders. Trade any token instantly right after launch.
        
        Here's your Ethereum wallet address linked to your Telegram Account. Simply fund your wallet and dive into trading.\n\n<b>Ethereum</b>\n<code>private key</code> (Tap to copy) \nBalance: <b>balance in dollers</b> Eth (<b>$sol balance</b>)
        
Click on the Refresh button to update your balance.
    """
    await query.edit_message_text(
        text=message_text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Help command')
    
async def user_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('state') == TOKEN_NAME :
        update_or_symbol = update.message.text
        await Wallet.get_asset_price(update_or_symbol)
    
async def button_clicked(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'buy':
        context.user_data['state'] = TOKEN_NAME
        await query.message.reply_text(text='Enter the token name or symbol to buy ..', reply_markup=ForceReply())
    
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(sol_menu, pattern='solana'))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_clicked))
    application.add_handler(MessageHandler(filters.TEXT, user_reply))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

