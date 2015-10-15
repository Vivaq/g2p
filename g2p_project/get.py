#-*- coding: utf-8 -*-
import sqlite3
import os
import json

db = sqlite3.connect(os.getcwd()+'\database.sqlite3')
c = db.cursor()
db.commit()
print eval(c.execute('select * from g2p_document').next()[1])