from dotenv import load_dotenv
load_dotenv()
import os
from telegram.ext import ContextTypes, Updater, Application, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, filters
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from wallet import create_new_account, get_token_price
BOT_TOKEN = os.getenv('TOKEN')

BUY_TOKEN_NAME = 1
WITHDRAW = 2


class ELiteBot:
    message = 0
    def __init__(self) -> None:
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", self.start_cmd))
        application.add_handler(CommandHandler("buy", self.buy_cmd))
        application.add_handler(CallbackQueryHandler(self.button_clicked))
        application.add_handler(MessageHandler(filters.TEXT, self.user_reply))
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    
    async def start_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        address = create_new_account(update.effective_user.id)
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
                    InlineKeyboardButton(text='BUY', callback_data='buy'),
                    InlineKeyboardButton(text='SELL', callback_data='sell')
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
        
        await update.message.reply_text(text=text, reply_markup=inline_keyboard, parse_mode=ParseMode.HTML)
       
            
    
    async def buy_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
         token_name = update.message.text
         try:
            token_details = await get_token_price(token_name)
            if token_details:
                await update.message.reply_text(f"The price of {token_name} is ${token_details}.")
            else:
                await update.message.reply_text("Please enter a valid token symbol e.g BTC/USDT...", reply_markup=ForceReply())
         except Exception as e:
             print(e)
         
    async def button_clicked(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        if query.data == 'buy':
            context.user_data['state'] = BUY_TOKEN_NAME
            await query.message.reply_text(text='✏️ Enter the token to buy and base token e.g BTC/USDT : ', reply_markup=ForceReply())
            
        elif query.data == 'withdraw':
            context.user_data['state'] = WITHDRAW
            await query.message.reply_text(text='✏️ Enter the address you want to withdraw funds..?', reply_markup= ForceReply())
    
    async def user_reply(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if context.user_data.get('state') == BUY_TOKEN_NAME:
            try:
                await self.buy_cmd(update, context)
            except Exception as e:
                print(f'Error while trying to perform buy token operation.')
    
    async def help_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('Help command')