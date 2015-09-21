#-*- coding: utf-8 -*-
import json
import time
from itertools import product
from contextlib import contextmanager


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
        prev_multiple_seq = [''.join(text[i:curr]) for i in xrange(curr-start_before_,curr-end_before_+1)]
        next_multiple_seq = [''.join(text[curr+1:i+1]) for i in xrange(curr+start_after_, curr+end_after_+1)]
        print prev_multiple_seq, next_multiple_seq
        if any(x in prev_multiple_seq for x in one_rule[0]) and any(x in next_multiple_seq for x in one_rule[1]):
            return True
    return False


if __name__ == "__main__":
    text = list(' '+raw_input().decode('utf-8'))
    with timeBlock('czas'):
        text_copy = text[:]
        with open('C:\data.txt', 'r') as f:
            all_rules = json.load(f)
        for curr, lex in enumerate(text):
            if lex in all_rules.keys():
                rules_for_letter = all_rules[lex]
                for phoneme, rules_for_lex in rules_for_letter.items():
                    if myGreatFun(curr, rules_for_lex, text):
                        text_copy[curr] = phoneme
        print ''.join(text_copy)