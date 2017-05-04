
# coding: utf-8

# In[103]:

import newspaper
cnn = newspaper.build('http://cnn.com')
fox = newspaper.build('http://fox.com')
bbc = newspaper.build('http://bbc.com')
reu = newspaper.build('http://reuters.com')
sky = newspaper.build('http://news.sky.com')
papers = [cnn, fox, bbc, reu, sky]


# In[104]:

i = 0
try:
    for paper in papers:
        for article in paper.articles:
            article.download()
            article.parse()
            filename = 'C:\\Users\\Alex\\Desktop\\CSC495\\'
            filename += str(i)
            filename += '.txt'
            with open(filename, 'a') as out:
                out.write(article.text + '\n')
            i += 1
except Exception:
    pass

