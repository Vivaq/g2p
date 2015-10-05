#-*- coding: utf-8 -*-
import sqlite3
import os
import json

db = sqlite3.connect(os.getcwd()+'\g2p_project\database.sqlite3')
c = db.cursor()
db.commit()
eval(c.execute('select * from g2p_document').next()[1])
