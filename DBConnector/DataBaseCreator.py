import sqlite3
from sqlite3 import Error
import os

create_table_sql = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        slang text NOT NULL,
                                        definition text NOT NULL,
                                        synonym text
                                    ); """

insert_row_sql = ''' INSERT INTO projects(slang,definition,synonym)
          VALUES(?,?,"NULL") '''

insert_row_all_sql = ''' INSERT INTO projects(slang,definition,synonym)
          VALUES(?,?,?) '''

update_row_sql = ''' UPDATE projects
          SET synonym = ? 
          WHERE slang = ?'''

delete_row_sql = 'DELETE FROM projects WHERE slang=?'

def sql_trace(stmt, bindings):
    #'Echoes all SQL executed'
    print("SQL:", stmt)
    if bindings:
        print("Bindings:", bindings)
    return True

class DBCreator:
   __instance = None
   dbpath_write = '../data/database/slangs.db'
   @staticmethod
   def getInstance():
      """ Static access method. """
      if DBCreator.__instance == None:
         DBCreator()
      return DBCreator.__instance

   def __init__(self, echo=False):
       """ Virtually private constructor. """
       if DBCreator.__instance != None:
           raise Exception("This class is a singleton!")
       else:
           try:
               # if not os.path.exists(self.dbpath_write):
                   self.conn = sqlite3.connect(self.dbpath_write)
                   self.cur = self.conn.cursor()
                   DBCreator.__instance = self
                   print("Database created...")
                   self.create_table()
                   print("Table created...")
                   if echo:
                       self.cur.setexectrace(sql_trace)
               # else:
               #     print('Database already exists : ' + self.dbpath_write)
           except Error as details:
               print("Unable to open db file: ", self.dbpath_write, details)

   def __del__(self):
       print("Deleting Connection...")
       if self.conn:
           self.conn.close()
       DBCreator._instance = None

   def clean(self):
        self.__del__()

   def create_table(self):
       print("Creating Table...")
       try:
           self.cur.execute(create_table_sql)
       except Error as e:
           print(e)

   def insert_SlangAndDef(self, slang, definition):
       self.cur.execute(insert_row_sql, (slang, definition))
       self.conn.commit()
       return self.cur.lastrowid

   def insert_SlangAndDefAndSyn(self, slang, definition, syn):
       self.cur.execute(insert_row_all_sql, (slang, definition, syn))
       self.conn.commit()
       return self.cur.lastrowid


   def update_synonym(self, slang, synonym):
        self.cur.execute(update_row_sql, (synonym,slang))
        self.conn.commit()

   def delete_task(self, slang):
    self.cur.execute(delete_row_sql, (slang,))
    self.conn.commit()

# DBCreator.getInstance().create_table()
# DBCreator.getInstance().insert_SlangAndDef("slang1", "def1")
# DBCreator.getInstance().insert_SlangAndDef("slang2", "def2")
# DBCreator.getInstance().insert_SlangAndDef("slang3", "def3")
# DBCreator.getInstance().update_synonym("slang1", "syn1")
# DBCreator.getInstance().update_synonym("slang2", "syn2")
# DBCreator.getInstance().update_synonym("slang3", "syn3")