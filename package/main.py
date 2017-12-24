import logging
import telebot
import timer
import bot
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("Begin start server.")
tgBot = telebot.TeleBot(os.getenv("BOT_ID", ""))

bot.getTracker(tgBot, logging)()

timer.getTimer(tgBot, logging)("Timer").start()

logging.info("Start polling")
def _pull():
    try:
        tgBot.polling(none_stop=True, interval=1)
    except Exception as e:
        _pull()

_pull()
