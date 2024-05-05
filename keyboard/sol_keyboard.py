from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Sol_Keyboard:


    @staticmethod
    def solana_menu_keyboard():
        solana_menu_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='Buy', callback_data='buy'),
                    InlineKeyboardButton(text='Sell', callback_data='sell')
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
                    InlineKeyboardButton(text='Ethereum', callback_data='ethereum'),
                    InlineKeyboardButton(text='✅Solana', callback_data='solana')
                ],
                [
                    InlineKeyboardButton(text='Help', callback_data='help'),
                    InlineKeyboardButton(text='Refresh', callback_data='refresh')
                ]
            ]
        )
        return solana_menu_keyboard
    
    @staticmethod
    def buy_sol():
        buy_sol = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='← Back', callback_data=''),
                    InlineKeyboardButton(text='Refresh', callback_data='')
                ],
                [
                    InlineKeyboardButton(text='Swap', callback_data=''),
                    InlineKeyboardButton(text='Limit', callback_data=''),
                    InlineKeyboardButton(text='DCA', callback_data='')
                ],
                [
                    InlineKeyboardButton(text='0.5 SOL', callback_data=''),
                    InlineKeyboardButton(text='1 SOL', callback_data=''),
                    InlineKeyboardButton(text='3 SOL', callback_data='')
                ],
                [
                    InlineKeyboardButton(text='5 SOL', callback_data=''),
                    InlineKeyboardButton(text='10 SOL', callback_data=''),
                    InlineKeyboardButton(text='x SOL', callback_data='')
                ],
                [
                    InlineKeyboardButton(text='15% Slippage', callback_data=''),
                    InlineKeyboardButton(text='X Slippage', callback_data=''),
                ],
                [
                    InlineKeyboardButton(text='Buy', callback_data='')
                ]
            ]
        )
