from dotenv import load_dotenv
load_dotenv()
import os
from telegram.ext import ContextTypes, Updater, Application, CommandHandler
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from wallet import create_new_account
BOT_TOKEN = os.getenv('TOKEN')




class ELiteBot:
    def __init__(self) -> None:
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", self.start_cmd))
        application.add_handler(CommandHandler("buy", self.buy_cmd))
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    
    
    async def start_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        address = await create_new_account(update.effective_user.id)
        text = f'''\n******** <b>Welcome to EliteBot</b> ********\n
Introducing a cutting-edge bot crafted exclusively for easy execution & surveillance of crypto trading.

Your Ethereum Wallet:
<code>{address}</code> (Tap to copy)
Balance: <code>0.0 ETH ($0)</code>

Fund your wallet and start trading
            '''
        inline_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='BUY', callback_data='buy_token'),
                    InlineKeyboardButton(text='SELL', callback_data='sell_token')
                ],
                 [
                    InlineKeyboardButton(text='Positions', callback_data='position'),
                    InlineKeyboardButton(text=' Limit Orders', callback_data='limit_order'),
                    InlineKeyboardButton(text='DCA Orders', callback_data='dca_order')
                ],
                [
                    InlineKeyboardButton(text='Copy Trade', callback_data='copy_trade'),
                ],
                [
                    InlineKeyboardButton(text='New Pairs', callback_data='new_pairs'),
                    InlineKeyboardButton(text='Referrals', callback_data='referrals'),
                    InlineKeyboardButton(text='⚙️ Settings', callback_data='settings')
                ],
                [
                    InlineKeyboardButton(text='Bride', callback_data='bride'),
                    InlineKeyboardButton(text='Withdraw', callback_data='withdraw')
                ],
                [
                    InlineKeyboardButton(text='Help', callback_data='help'),
                    InlineKeyboardButton(text='Refresh', callback_data='refresh')
                ]
            ]
        )
        
        reply = await update.message.reply_text(text=text, reply_markup=inline_keyboard, parse_mode=ParseMode.HTML)
        if reply:
            print(f'massage sent successfully: {reply.to_dict()}')
    
    async def buy_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
         answer = await update.message.reply_text(text="✏️ Enter the token address you want to buy: ")
         print(answer)