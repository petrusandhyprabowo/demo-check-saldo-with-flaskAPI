#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 07:54:15 2017

@author: teewoll
"""

import psycopg2
myConnection = None

def connect(hostname, username, password, database):
  global myConnection
  myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )

def insertQuery(table, columns, values):
  insertQ = "insert into " + table + "(" + columns + ") values(" + values + ");"
  global myConnection
  cur = myConnection.cursor()
  cur.execute(insertQ)
  myConnection.commit()

def selectQuery(table, uid):
  selectQ = "select * from public." + table + " where uid = %s"
  global myConnection
  cur = myConnection.cursor()
  cur.execute(selectQ,(uid,))
  return cur.fetchall()
  
def closeConnection():
  global myConnection
  myConnection.close()
  
def commitDb():
  global myConnection
  myConnection.commit()