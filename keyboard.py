from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:
    
    @staticmethod
    def menu_keyboard():
        menu_keyboard = InlineKeyboardMarkup(
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
                    InlineKeyboardButton(text='💰 Referrals', callback_data='referrals'),
                    InlineKeyboardButton(text='⚙️ Settings', callback_data='settings')
                ],
                [
                    InlineKeyboardButton(text='Bride', callback_data='bride'),
                    InlineKeyboardButton(text='Withdraw', callback_data='withdraw')
                ],
                [
                    InlineKeyboardButton(text='ℹ️ Help', callback_data='help'),
                    InlineKeyboardButton(text='↻ Refresh', callback_data='refresh')
                ]
            ]
        )
        return menu_keyboard
