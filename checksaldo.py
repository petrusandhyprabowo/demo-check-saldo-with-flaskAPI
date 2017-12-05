#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:27:48 2017

@author: teewoll
"""

import dbconnection

dbconnection.connect('localhost','username','password','saldodb')

def getSaldo(uid):
    row = dbconnection.selectQuery("usersaldo", uid)
    saldo = None

    if 0 != len(row):
        saldo = row[0][3]
    else:
        saldo = 'Not Found'
    
    return saldo

#print(getSaldo("65647"))
