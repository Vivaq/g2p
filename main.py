#-*- coding: utf-8 -*-
import json
import time
from contextlib import contextmanager
import os
import sqlite3


@contextmanager
def timeBlock(label):
    start = time.clock()
    try:
        yield
    finally:
        end = time.clock()
        print label, end-start

def myGreatFun(curr, rules_for_lex, text):
    for one_rule in rules_for_lex:
        start_before_, start_after_, end_before_, end_after_ = \
            [fun(len(x) for x in one_rule[i]) for fun in [min, max] for i in [0, 1]]
        prev_multiple_seq = [''.join(text[i:curr]) for i in xrange(curr-start_before_, curr-end_before_+1)]
        next_multiple_seq = [''.join(text[curr+1:i+1]) for i in xrange(curr+start_after_, curr+end_after_+1)]
        if any(x in prev_multiple_seq for x in one_rule[0]) and any(x in next_multiple_seq for x in one_rule[1]):
            return True
    return False

if __name__ == "__main__":
    text = list(' '+raw_input().decode('utf-8'))
    with timeBlock('czas'):
        text_copy = text[:]
        db = sqlite3.connect(os.getcwd()+'\g2p_project\database.sqlite3')
        c = db.cursor()
        db.commit()
        all_rules = eval(c.execute('select * from g2p_document').next()[1])
        print all_rules
        for curr, lex in enumerate(text):
            if lex in all_rules.keys():
                rules_for_letter = all_rules[lex]
                for phoneme, rules_for_lex in rules_for_letter.items():
                    if myGreatFun(curr, rules_for_lex, text):
                        text_copy[curr] = phoneme
        print ''.join(text_copy)