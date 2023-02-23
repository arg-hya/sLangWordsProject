import sqlite3
from sqlite3 import Error
import os

check_slang_exists_sql = """ SELECT COUNT(1)
                        FROM projects
                        WHERE slang = ? """

def sql_trace(stmt, bindings):
    #'Echoes all SQL executed'
    print("SQL:", stmt)
    if bindings:
        print("Bindings:", bindings)
    return True

class DBReader:
   __instance = None
   dbpath_write = '../data/database/slangs.db'
   @staticmethod
   def getInstance():
      """ Static access method. """
      if DBReader.__instance == None:
         DBReader()
      return DBReader.__instance

   def __init__(self, echo=False):
       """ Virtually private constructor. """
       if DBReader.__instance != None:
           raise Exception("This class is a singleton!")
       else:
           try:
               if  os.path.exists(self.dbpath_write):
                   self.conn = sqlite3.connect(self.dbpath_write)
                   self.cur = self.conn.cursor()
                   DBReader.__instance = self
                   print("Database created...")
                   if echo:
                       self.cur.setexectrace(sql_trace)
               else:
                   print('Database does not exists : ' + self.dbpath_write)
           except Error as details:
               print("Unable to open db file: ", self.dbpath_write, details)

   def __del__(self):
       print("Deleting Connection...")
       if self.conn:
           self.conn.close()
       DBReader._instance = None

   def clean(self):
        self.__del__()

   def select_all_records(self, display = False):
       print("Printing all rows...")
       self.cur.execute("SELECT * FROM projects")
       rows = self.cur.fetchall()
       if display:
           for row in rows:
               print(row)
       return rows

   def select_row_by_slang(self, slang, display = False):
       self.cur.execute("SELECT slang,definition,synonym FROM projects WHERE slang=?", (slang,))
       rows = self.cur.fetchall()
       if display:
           for row in rows:
               print(row)
       return rows

   def select_definition_by_slang(self, slang, display = False):
       self.cur.execute("SELECT definition FROM projects WHERE slang=?", (slang,))
       rows = self.cur.fetchall()
       if display:
           for row in rows:
               print(row)
       return rows

   def select_synonym_by_slang(self, slang, display = False):
       self.cur.execute("SELECT synonym FROM projects WHERE slang=?", (slang,))
       rows = self.cur.fetchall()
       if display:
           for row in rows:
               print(row)
       return rows

   def is_slang(self, slang):
       self.cur.execute(check_slang_exists_sql, (slang,))
       res = self.cur.fetchall()
       #print(res[0][0])
       if 1 == res[0][0]:
           return True
       return False

# DBReader.getInstance().select_all_tasks()
# print(DBReader.getInstance().is_slang('slang23'))
# DBReader.getInstance().select_row_by_slang('slang2', True)