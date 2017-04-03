# coding=utf-8
import sys
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
import nltk
nltk.download("stopwords")
stopwords = set(nltk.corpus.stopwords.words('english'))
import string
from collections import Counter

dictionaries = ['Defence.txt','Demography.txt','Economy.txt']

if len(sys.argv) != 2:
    print("python main.py <file-to-parse>")
    exit(1)

filename = sys.argv[1]

def parse(text,dictionary):
    w = len(dictionary)
    counts = Counter(text)
    n = 0
    for word in dictionary:
        if word in counts:
            n+=1
    k = 0
    for word in counts:
        if word in dictionary:
            k+= counts[word]
    if k>=w*0.5 or n >= 0.15*w:
        return True
    else:
        return False

def main():
    with open(filename,'r') as outfile:
        f = outfile.read()
        f = f.translate(string.maketrans(string.punctuation, ' '*len(string.punctuation)))
        words = word_tokenize(f.decode('utf-8'))
    wordsSelected = []
    for w in words:
        if w not in stopwords:
            wordsSelected.append(w)
    score = 0
    for dictionary in dictionaries:
        with open(dictionary,'r') as outfile:
            d = outfile.read().decode('utf-8')
            d = d.split('\n')
        is_significant = parse(wordsSelected, d)
        if is_significant: score+=1
    #spread = FreqDist(wordsSelected)
    #print(spread.plot(50))
    print("Score = %d"%(score))
    return


if __name__ == "__main__":
    main()