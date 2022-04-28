import sqlite3
import logging, os, sys
print("current directory: %s" % os.getcwd())
import socket
from datetime import date

class DB():
    
    def __init__(self):
        self.con = sqlite3.connect('wordleLog.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS logs 
                (id text primary key, gamedate date, ipaddress text, playedword text, userword text, success real)''')
        
        self.cur.execute('pragma foreign_keys=ON')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS winCount 
                (commonid text, gamedateInWin date, gamesPlayed text, winCount text)''')
        
        self.cur.execute('''CREATE TABLE IF NOT EXISTS errors 
                (gamedateError date, errorMsg text)''')
    
    
    # con.set_trace_callback(print)
    # con.set_trace_callback(logging.debug)
    
    def insertData(self, id, inPlayed, inUserWord, inSuccess):
        try:
            self.con = sqlite3.connect('wordleLog.db')
            self.cur = self.con.cursor()
            with self.con:
                self.cur.execute("INSERT INTO logs VALUES (:id ,:gamedate, :ipaddress, :playedword, :userword, :success)", {'id':id, 'gamedate': date.today(), 'ipaddress': socket.gethostbyname(socket.gethostname()), 'playedword': inPlayed, 'userword': inUserWord, 'success': inSuccess})
            self.cur.execute("SELECT * FROM logs")
            print("insertDate values")
            print(self.cur.fetchall())
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in insertdata method, DB Module, occurred.".__str__())
        finally:
            self.con.close()
            
    def insertDataWinCount(self, commonid, gamesPlayed, winCount):
        try:
            self.con = sqlite3.connect('wordleLog.db')
            self.cur = self.con.cursor()
            with self.con:
                self.cur.execute("INSERT INTO winCount VALUES (:commonid, :gamedateInWin, :gamesPlayed, :winCount)", {'commonid': commonid, 'gamedateInWin': date.today(), 'gamesPlayed': gamesPlayed, 'winCount': winCount})
            self.cur.execute("SELECT * FROM winCount")
            print("insertDataWinCount values")
            print(self.cur.fetchall())
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in insertDataWinCount method, DB Module, occurred.".__str__())
        finally:
            self.con.close()
                   
 
    def getData(self, startDate, endDate):
        try:
            self.con = sqlite3.connect('wordleLog.db')
            self.cur = self.con.cursor()
            
            print("Get data function")
            for i in self.cur.execute('''SELECT *
                FROM winCount wc join logs ls ON wc.commonid = ls.id 
                WHERE gamedateInWin>=? AND gamedateInWin<=?
                ''',[startDate, endDate]):
                print("Get data for dates")
                print(i)
            
        except:
                print(sys.exc_info())
                print("Error:", sys.exc_info()[0], " in getdata method, DB Module, occurred.".__str__())
        finally:
            self.con.close()
            
    def insertError(self, inErrorMsg):
        try:
            self.con = sqlite3.connect('wordleLog.db')
            self.cur = self.con.cursor()
            with self.con:
                self.cur.execute("INSERT INTO errors VALUES (:gamedateError, :errorMsg)", {'gamedateError': date.today(), 'errorMsg': inErrorMsg})
            self.cur.execute("SELECT * FROM errors")
            print("insertError values")
            print(self.cur.fetchall())
        except:
            print(sys.exc_info())
            print("Error:", sys.exc_info()[0], " in inserterror method, DB Module, occurred.".__str__())
        finally:
            self.con.close()
            
        
    # self.con.commit()

# if __name__ == '__main__':
#     db = DB()
#     db.getData('2022-04-27','2022-04-28')


# conn = sqlite3.connect('wordleLog.db')
# curr = conn.cursor()
# curr.execute("INSERT INTO logs VALUES ('2022-04-27', '127:0:0:1', 'bench', 'bench', '     ')")


# curr.execute("SELECT * FROM logs")
# print(curr.fetchall())