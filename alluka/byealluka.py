from io import BytesIO
from time import sleep
from typing import List
import random
from telegram import Bot, Update, TelegramError
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, Filters, run_async
import alluka.modules.sql.users_sql as sql
from alluka.modules.helper_funcs.chat_status import sudo_plus, dev_plus
from alluka import dispatcher

CHAT_LIST = [-1001316929171,-1001316929171,-1001252390502,-1001480756193,-1001163001923,-1001153638337,-1001242271253,-1001337955406,-1001439068379,-1001337867954,1001409412638,-1001393990406, -1001272774251,-1001207870063,-1001488429872,-1001172519034,-1001266396370,-1001424468958 ,-1001414408275,-1001486706830,-1001408746093,-1001254311910,-1001407886725,-1001481713361,-373607119,-1001327711680,-1001197323574 ,-1001264386429,-409306776,-1001409489297,-1001316929171 ,-1001308851965,-1001252390502,-1001315533316,-1001432222736,-1001404020381]


@run_async
@dev_plus
def byalluka(bot: Bot, update: Update,args: List[str]):

    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))
    chat_id = random.choice(CHAT_LIST)
    bot.leave_chat(int(chat_id))	

            




 
ALLUKA_HANDLER = CommandHandler("byealluka", byalluka, pass_args = True)


dispatcher.add_handler(ALLUKA_HANDLER)