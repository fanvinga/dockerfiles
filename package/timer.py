import threading
import time
import api
import db

DATABASE = db.getDb("bot.db")


def getTimer(bot, logger):
    class Timer(threading.Thread):
        def __init__(self, threadName):
            super(Timer, self).__init__(name=threadName)

        def run(self):
            while True:
                for item in DATABASE.getAllPackages():
                    information = api.TrackerApi.getPackageInformation(item[0], item[3])
                    if information["data"] and information["data"][0]["time"] != item[4]:
                        logger.info("Found update: " + item[0])
                        bot.send_message(item[2], item[5] + "\n" + information["data"][0]["data"] + "\nStatus: " +
                                         api.getStatusFromCode(information["status"]))
                        DATABASE.update(item[2], item[0], information["status"], information["data"][0]["time"])
                logger.info("Timer sleeping.")
                time.sleep(60 * 10)

    return Timer
