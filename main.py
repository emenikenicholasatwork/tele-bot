
from helper_functions import set_up_DB
from bot import ELiteBot

def start_bot():
    set_up_DB()
    ELiteBot()
    

if __name__ == '__main__':
    start_bot()
