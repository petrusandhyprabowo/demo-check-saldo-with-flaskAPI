#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:07:20 2017

@author: teewoll
"""

from flask import request
from flask_api import FlaskAPI
import checksaldo

app = FlaskAPI(__name__)

@app.route("/checksaldo", methods=['GET'])
def notes_list():

    uid = request.args.get('uid')
    saldo = checksaldo.getSaldo(uid)
    
    return {
                "data" : {
                            "status" : 200,
                            "message" : saldo
                        }
            }
                
if __name__ == "__main__":
    app.run(debug=True,port=12345)
