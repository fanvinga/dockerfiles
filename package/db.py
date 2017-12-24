# -*- coding: utf-8 -*-
import sqlite3

DB_TABEL = "packages"


def getDb(path):
    def getCursor(func):
        def __call(*args, **kwargs):
            conn = sqlite3.connect(path)
            ret = func(conn, *args, **kwargs)
            conn.commit()
            conn.close()
            return ret
        return __call

    def getCs(func):
        def __call(*args, **kwargs):
            conn = sqlite3.connect(path)
            cs = conn.cursor()
            ret = func(cs, *args, **kwargs)
            conn.commit()

            cs.close()
            conn.close()
            return ret
        return __call

    class TrackerDb(object):
        def __init__(self):
            pass

        @staticmethod
        @getCursor
        def init(conn):
            conn.execute(
                "CREATE TABLE IF NOT EXISTS " + DB_TABEL + "(num char, status int, user char, pType char, lastDate "
                                                           "char, packageName char) "
            )

        @staticmethod
        @getCs
        def getAllPackages(cs):
            cs.execute(
                "SELECT * FROM " + DB_TABEL
            )
            return cs.fetchall()

        @staticmethod
        @getCs
        def getUnfinishAll(cs):
            cs.execute(
                "SELECT * FROM " + DB_TABEL + " WHERE status=1 AND  status=0"
            )
            return cs.fetchall()

        @staticmethod
        @getCs
        def getUserAll(cs, user):
            cs.execute(
                "SELECT * FROM " + DB_TABEL + " WHERE user='" + str(user) + "'"
            )
            return cs.fetchall()

        @staticmethod
        @getCs
        def checkDump(cs, user, num, pType):
            cs.execute(
                "SELECT * FROM " + DB_TABEL + " WHERE num='" + str(num) + "' AND user='" + str(user)
                + "' AND pType='" + pType + "\'"
            )
            return len(cs.fetchall()) == 0

        @staticmethod
        @getCs
        def newPackage(cs, user, num, pType, lastDate, packageName, status):
            if not TrackerDb.checkDump(user, num, pType):
                raise ValueError("Dump")
            cs.execute(
                "INSERT INTO " + DB_TABEL + " values (?,?,?,?,?,?)", (num, status, user, pType, lastDate, unicode(
                    packageName))
            )

        @staticmethod
        @getCs
        def removePackage(cs, user, num):
            cs.execute(
                "DELETE FROM " + DB_TABEL + " WHERE num='" + str(num) + "' AND user='" + str(user) + "'"
            )

        @staticmethod
        @getCs
        def update(cs, user, num, status, lastDate):
            cs.execute(
                "UPDATE " + DB_TABEL + " SET status='" + str(status) + "', lastDate='" +
                str(lastDate) + "' WHERE user='" + str(user) + "' AND num='" + str(num) + "'"
            )

    obj = TrackerDb()
    obj.init()
    return obj
