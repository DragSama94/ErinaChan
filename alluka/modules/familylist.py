from telegram import Update, Bot, ParseMode
from telegram.ext import run_async

from alluka.modules.disable import DisableAbleCommandHandler
from alluka import dispatcher

from requests import get

@run_async
def ud(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/familylist '):]
  
  sunnyimg = ""
  sunny = """[Sunny ZoldyckFamily」](https://telegram.dog/medevilofmelodies) as Hisoka Morow.\n To get more about him do `!info @medevilofmelodies`"""

  neelimg = ""
  neel = """[Neel ZoldyckFamily」](https://telegram.dog/spookyenvy) as Kite.\n To get more about him do `!info @spookyenvy`"""

  aniimg = ""
  anii = """[Anii「ZoldyckFamily」](https://telegram.dog/spookyanii) as Chrollo Lucilfer.\n To get more about him do `!info @spookyanii`"""
  
  saharshimg = ""
  saharsh = """[Saharsh DHMN! ZoldyckFamily」](https://telegram.dog/MedevilofMarvel) as Meruem.\n To get more about him do `!info @MedevilofMarvel`"""

  kanekiimg = ""
  kaneki = """[金木健 #UT #LazyAF_Geng #Toxic_Gang](https://telegram.dog/Top_Kekk) as Ging.\n To get more about him do `!info @Top_Kekk`"""


 

  message.reply_photo(sunnyimg,sunny, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(neelimg, neel, parse_mode=ParseMode.MARKDOWN)  
  message.reply_photo(aniimg, anii, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(saharshimg, saharsh, parse_mode=ParseMode.MARKDOWN)
  message.reply_photo(kanekiimg, kaneki, parse_mode=ParseMode.MARKDOWN)


  
ud_handle = DisableAbleCommandHandler("familylist", ud)

dispatcher.add_handler(ud_handle)
