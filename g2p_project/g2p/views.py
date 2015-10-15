#-*- coding: utf-8 -*-
import json
from itertools import product
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from g2p.forms import DocumentForm
import sqlite3
import os
from g2p.models import Document
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import unicodedata
from django.contrib.auth.decorators import login_required

class MyList(list):
    def __init__(self, *args):
        super(MyList, self).__init__(args)

    def __add__(self, other):
        new_kl = self[:]
        new_kl += other
        return self.__class__(*new_kl)

    def __radd__(self, other):
        new_kl = other
        new_kl += self[:]
        return self.__class__(*new_kl)

    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])

    def __mul__(self, other):
        return map(''.join, list(product(self, other)))

    def __rmul__(self, other):
        return map(''.join, list(product(other, self)))

def execSetsSplitStringsAndMakeProducts(x):
    A = MyList('a', u'ą', 'e', u'ę', 'i', 'o', u'ó', 'u', 'y')
    D = MyList('b', 'd', 'g', 'z', u'ź', u'ż')
    T = MyList('c', u'ć', 'f', 'h', 'k', 'p', 's', u'ś', 't')
    R = MyList('l', u'ł', 'r', 'w')
    M = MyList('m', 'n', u'ń', 'j')
    V = A+R+M
    O = MyList('.', '!', '?', ',', ';', ':', '-', '...', ')', '(', ' ', '#')
    O1 = MyList('.', '!', '?', ',', ';', ':', '-', '...', ')', '(', '#')
    X = A+D+T+R+M+O

    x = json.loads(x[0])
    for i, let_rules in enumerate(x.values()):
        for j, let_rule in enumerate(let_rules.values()):
            for k, phoneme_rules in enumerate(let_rule):
                rule = eval(''.join(phoneme_rules))
                rule = [value for values in rule for value in (values if isinstance(values, basestring) else [values])]
                before_, after_ = rule[:rule.index('_')], rule[rule.index('_')+1:]
                rule = [[''.join(res) for res in list(product(*before_))],
                        [''.join(res) for res in list(product(*after_))]]
                x.values()[i].values()[j][k] = rule
    return x

@login_required
def downloadData(request):
    if request.method == 'POST':
        '''with open('C:\data.txt', 'r') as f:
            try:
                jsn = json.load(f)
            except:
                jsn = {}
        with open('C:\data.txt', 'w') as f:
            jsn.update(execSetsSplitStringsAndMakeProducts(request.POST.get('docfile')))
            json.dump(jsn, f)'''
        db = sqlite3.connect(os.getcwd()+'\database.sqlite3')
        c = db.cursor()
        db.commit()
        request.POST = dict(request.POST)
        try:
            x = eval(c.execute('select * from g2p_document').next()[1])
            x.update(execSetsSplitStringsAndMakeProducts(request.POST.get('docfile')))
            request.POST['docfile'] = x
        except:
            request.POST['docfile'] = execSetsSplitStringsAndMakeProducts(request.POST.get('docfile'))
        Document.objects.all().delete()
        form = DocumentForm(request.POST)
        data = form.save(commit=False)
        data.save()
        return HttpResponseRedirect(reverse('g2p.views.downloadData'))
    else:
        form = DocumentForm()
    return render_to_response(
        'g2p/exp.html',
        {'form': form},
        context_instance=RequestContext(request)
    )