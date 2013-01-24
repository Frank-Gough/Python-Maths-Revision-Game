# -- Basic Database - sqlite ---------  #
# -- High Scores db                     #
#                                       #
# Author: Jon Spavin                    #
#---------------------------------------#

import sqlite3

db = sqlite3.connect('/Users/jonspavin/Documents/test1.db')
cursor = db.cursor()

def createDB():
          print('create DB')
#create database
#db = sqlite3.connect('/Users/jonspavin/Documents/test3.db')
#cursor = db.cursor()

def createTable():
          print("create table?")
          #ask if we want to recreate an existing table
          cursor.execute("select name from sqlite_master where name='cust1'")
          result = cursor.fetchall()
          # do we create or not!
          createTable = False
          if len(result) == 1:
                    response = input("The table 'test1' already exists, recreate it? (y/n)'")
                    if response =='y':
                              print("true")
                              createTable = True
                              print("the test table will be recreated - All data will be lost!")
                              #delete existing data
                              cursor.execute("drop table if exists test1")
                              db.commit()
                    else:
                              print("existing test1 table was kept")
          else:
                    print("yes create table!")
                    createTable = True
                    if createTable:
                              cursor.execute('''CREATE TABLE cust1
                                       (id interger,
                                       f_name text,
                                       l_name text,
                                       score interger)''')
                              #save the changes to the dayabase
                              db.commit()
                              
def addData():
          #Insert data
          cursor.execute("INSERT INTO cust1 VALUES ('1', 'jon', 'spavin', '1234')")
          db.commit()
          
def query1():
          #query data
          print ("query data")
          sql = "SELECT * from cust1"
          cursor.execute(sql)
          result = cursor.fetchall()
          print (result)

          #save the changes to the database
          #db.commit()
          #close the connection
          #cursor.close()

def main():
          createTable()
          query1()
          #addData()
          cursor.close()
          
