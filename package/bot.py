# -*- coding: utf-8 -*-
from markupsafe import Markup, escape
import telebot
import api
import sys
import db

reload(sys)
sys.setdefaultencoding('utf8')
DATABASE = db.getDb("bot.db")


def getTracker(bot, logger):
    """
    Get the tracker
    
    :type bot: telebot.TeleBot
    :param bot: The TeleBot
    :return: the Package Tracker 
    """

    class PackagerTracker(object):
        def __init__(self):
            pass

        @staticmethod
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            logger.info(str(message.chat.id) + " is start")
            bot.reply_to(message, "Hi")

        @staticmethod
        @bot.message_handler(commands=['new'])
        def create_query(message):
            message.text = " ".join(filter(lambda x: x != "", str(message.text).split(' ')))
            if len(str(str(message.text).encode("utf-8")).split(" ")[1:]) == 0:
                bot.send_message(message.chat.id, u"错误: 请输入单号")
                return

            packageID = str(escape(str(message.text).split(" ")[1]))
            packageProvider = ""
            packageName = u"包裹 %s" % str(packageID)[:4]
            packageStatus = 0

            if len(str(message.text).split(" ")[1:]) >= 2:
                packageName = str(escape(str(message.text).encode("utf-8").split(" ")[2]))

            if len(str(message.text).split(" ")[1:]) == 3:
                packageProvider = str(escape(str(message.text).split(" ")[3]))

            try:
                packageProvider = api.TrackerApi.getPackageProvider(packageID)
            except ValueError:
                if packageProvider == "" or ():
                    bot.send_message(message.chat.id, u"错误: 包裹未找到, 请检查或者强制添加.")
                    return

            lastDate = ""
            try:
                data = api.TrackerApi.getPackageInformation(packageID, packageProvider)
                if data["data"]:
                    lastDate = data["data"][0]["time"]
                    packageStatus = data["status"]
            except ValueError:
                pass

            if int(packageStatus) == 0 and packageProvider == "":
                bot.send_message(message.chat.id, u"错误: 包裹未找到, 请检查或者强制添加.")
                return

            try:
                DATABASE.newPackage(message.chat.id, packageID, packageProvider, lastDate, packageName, packageStatus)
            except ValueError:
                bot.send_message(message.chat.id, u"请不要添加相同的快递!")
                return
            try:
                api.getProvider(packageProvider)
            except KeyError:
                packageProvider = api.getProviderFromString(packageProvider)
            logger.info("Starting a new package: " + packageID)
            bot.send_message(message.chat.id, u"你的快递 \'%s[%s]\' 已被保存" % (packageName,
                                                                         api.getProvider(packageProvider)))

        @staticmethod
        @bot.message_handler(commands=['list'])
        def list_package(message):
            message.text = " ".join(filter(lambda x: x != "", str(message.text).split(' ')))
            messages = ""
            for package in DATABASE.getUserAll(message.chat.id):
                messages += "\n" + package[5] + " - " + package[0] + " - " + api.getStatusFromCode(package[1]) + \
                            " - " + api.TrackerApi.getLastMessage(package[0], package[3])
            bot.send_message(message.chat.id, u"你的快递:" + messages)

        @staticmethod
        @bot.message_handler(commands=['remove'])
        def remove_package(message):
            message.text = " ".join(filter(lambda x: x != "", str(message.text).split(' ')))
            if len(str(message.text).split(" ")[1:]) == 0:
                bot.send_message(message.chat.id, u"错误: 请输入单号")
                return

            packageID = str(escape(str(message.text).split(" ")[1]))

            DATABASE.removePackage(message.chat.id, packageID)

            logger.info(u"删除了快递: " + packageID)

            bot.send_message(message.chat.id, u"删除了快递: " + packageID)

        @staticmethod
        @bot.message_handler(commands=['fetch'])
        def fetch_package(message):
            message.text = " ".join(filter(lambda x: x != "", str(message.text).split(' ')))
            if len(str(message.text).split(" ")[1:]) == 0:
                bot.send_message(message.chat.id, u"错误: 请输入单号")
                return

            packageID = str(escape(str(message.text).split(" ")[1]))

            logger.info(u"查找快递: " + packageID)
            info = api.TrackerApi.getPackageInformation(packageID)
            messages = u"\n包裹状态: " + api.getStatusFromCode(info["status"])
            if info["data"]:
                for item in info["data"]:
                    messages += ("\n" + item["data"] + " - " + item["time"])
            else:
                bot.send_message(message.chat.id, u"错误: 包裹未找到")
                return
            bot.send_message(message.chat.id, u"查找快递: " + packageID + messages)

    return PackagerTracker
