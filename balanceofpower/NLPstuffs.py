
# coding: utf-8

# In[163]:

from bs4 import BeautifulSoup
import requests
import re
import nltk
import os
import csv
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import math
import numpy as np
import pandas as pd


# In[140]:

def clean(token):
    token = re.sub('[<(,.:\';%$)>]', '', token)
    return token


# In[141]:

def clean2(token):
    token = re.sub('\n', ' ', token)
    return token


# In[142]:

def clean3(token):
    token = re.sub('[\[\'\]]', '', token)
    return token


# In[143]:

corpus = ''
for f in os.listdir('C:\\Users\\Alex\\Desktop\\495Docs'):
    file = open('C:\\Users\\Alex\\Desktop\\495Docs\\' + f, 'r', encoding='utf-8')
    corpus += file.read()
docs = []
docs = re.split('\d+\sof\s\d+\sDOCUMENTS', corpus)


# In[ ]:




# In[144]:

dates = re.compile('(?:January|February|March|April|May|June|July|August|September|October|November|December)(?:\s\d+,\s)(\d+)')
yr = re.compile('(\d{4})')
years = []
i = 0
year = 2000
for doc in docs:
    date = dates.search(doc)
    if date != None:
        year = yr.search(date.group(0)).group(0)
    if year != None:
        years.append(int(year))
    else:
        years.append(2000)
    i += 1
years = [x - 1908 for x in years]


# date range 1909 2017

# In[145]:

docs = [clean(d) for d in docs]
countries = ['Afghanistan', 'Bahrain', 'Cyprus', 'Egypt', 'Iran', 'Iraq', 'Israel', 'Kuwait', 
             'Lebanon', 'Libya', 'Oman', 'Pakistan', 'Qatar', 'Russia', 'Saudi Arabia', 'Sudan', 
             'Syria', 'Turkey', 'United Arab Emirates', 'United States', 'Yemen']
cc  = ['af', 'ba', 'cy', 'eg', 'ir', 'iz', 'is', 'jo', 'ku', 'le', 'ly', 'mu', 
                'pk', 'qa', 'rs', 'sa', 'su', 'sy', 'tu', 'ae', 'us', 'ym']


# In[146]:

lstf = open('C:\\Users\\Alex\\Desktop\\lists.csv', 'r')
reader = csv.reader(lstf)
lists = []
for r in reader:
    lists.append(r)


# In[156]:

instability = ['terrorism', 'terrorists','instability', 'anarchy', 'failure', 'uncertainty', 'instability', 'killing', 'extremists', 'division']
instidx = [0]*21
nridx = [0]*21
indidx = [0]*21

cr = str.join('|', countries)
cnt = re.compile(cr)

ib = str.join('|', instability)
ibt = re.compile(ib)

lists = [[str.join('|', clean3(e).split(',')) for e in l] for l in lists]

for d in docs:
    allc = cnt.findall(d)
    cnts = []
    for c in Counter(allc).most_common(5):
        if c[1]/len(allc) > .2:
            cnts.append(c[0])
    alli = ibt.findall(d)
    for c in cnts:
        if len(alli) > 10:
            instidx[countries.index(c)] += 1
            
        nrt = re.compile(lists[countries.index(c)][1])
        allnr = nrt.findall(d)
        nridx[countries.index(c)] += len(allnr)
        nrht = re.compile(lists[countries.index(c)][2])
        allnrh = nrht.findall(d)
        nridx[countries.index(c)] -= len(allnrh)
        
        indt = re.compile(lists[countries.index(c)][3])
        allind = indt.findall(d)
        if len(allind) > 1:
            indidx[countries.index(c)] += 1

nnr = [float(i)/sum(nridx) for i in nridx]
ninst = [float(i)/sum(instidx) for i in instidx]
nind = [float(i)/sum(indidx) for i in indidx]



# In[176]:

nlpf = open('C:\\Users\\Alex\\Desktop\\nlp.csv', 'w', newline='')
nlpw = csv.writer(nlpf)
nlpw.writerow(['Country Code', 'Natural Resource Index', 'Industrial Index', 'Instability Index'])
for i in range(0,len(cc) - 1):
    nlpw.writerow([cc[i], nridx[i], indidx[i], instidx[i]])
nlpf.close()


# In[167]:

a = pd.read_csv('C:\\Users\\Alex\\Desktop\\nlp.csv')
b = pd.read_csv('C:\\Users\\Alex\\Desktop\\infrastructure.csv')
c = a.merge(b, on='Country Code')
c.to_csv('C:\\Users\\Alex\\Desktop\\infrastructure.csv', index=False)


# In[175]:




# In[ ]:



