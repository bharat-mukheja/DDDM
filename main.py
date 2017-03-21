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

if len(sys.argv) != 3:
    print("python main.py <file-to-parse> <Dictionary>")
    exit(1)

filename = sys.argv[1]
dictionary = sys.argv[2]
'''if dictionary not in os.listdir():
    print("Please correct dictionary name")
    print("python main.py <file-to-parse> <Dictionary>")
    exit(1)'''

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
    with open(dictionary,'r') as outfile:
        d = outfile.read().decode('utf-8')
        d = d.split('\n')
    wordsSelected = []
    for w in words:
        if w not in stopwords:
            wordsSelected.append(w)
    is_significant = parse(wordsSelected, d)
    #spread = FreqDist(wordsSelected)
    #print(spread.plot(50))
    print("Significant" if is_significant else "Not Significant")
    return


if __name__ == "__main__":
    main()