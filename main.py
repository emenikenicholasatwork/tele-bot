
# from dotenv import load_dotenv
# load_dotenv()
# import os
# from telegram import Update, ForceReply
# from telegram.constants import ParseMode
# from telegram.ext import Application, Updater, ContextTypes, MessageHandler, CommandHandler, filters, CallbackQueryHandler, CallbackContext
# from keyboard import Eth_keyboard
# # from wallet import Eth_Wallet
from helper_functions import set_up_DB
from bot import ELiteBot

# TOKEN  = os.getenv('TOKEN')
# TOKEN_NAME = 1
# WITHDRAW = 2

def start_bot():
    set_up_DB()
    ELiteBot()
    
# async def user_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if context.user_data.get('state') == TOKEN_NAME :
#         update_or_symbol = update.message.text
#         await Eth_Wallet.get_asset_price(update_or_symbol)
    
# async def button_clicked(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     if query.data == 'buy':
#         context.user_data['state'] = TOKEN_NAME
#         await query.message.reply_text(text='✏️ Enter the symbol and base token symbol you which to make buy e.g BTC/USDT ..', reply_markup=ForceReply())
#     elif query.data =='withdraw':
#         context.user_data['state'] = WITHDRAW
#         await query.message.reply_text(text='✏️ Enter the address in other to make withdrawal...', reply_mark=ForceReply())
#     elif query.data == 'copy_trade':
#         keyboard = Eth_keyboard.ethereum_copy_trade_keyboard()
#         message_text="""
#                                       = <b>Copy Trade </b> =
# Add wallets to copy trade . Supports ETH
                                      
# <b>Copytrade Addresses: </b>
# no addresses added.
#                                       """
#         await query.edit_message_text(
#                 text=message_text,
#                 reply_markup=keyboard,
#                 parse_mode=ParseMode.HTML                             
#                                       )
#     elif query.data == 'copy_trade_address':
#         await query.message.reply_text(text='✏️ Enter mirror address to copy trade: ', reply_markup=ForceReply())
#     elif query.data == 'eth_menu':
#         keyboard = Eth_keyboard.ethereum_menu_keyboard()
#         await query.edit_message_text(text='Trading made easy with Elite bot',reply_markup=keyboard)
#     elif query.data == 'sell':
#         print(update.effective_user.id())
#         # reply = await Eth_Wallet.get_asset_price()
#         # await query.edit_message_text(text=reply)
    


if __name__ == '__main__':
    start_bot()
