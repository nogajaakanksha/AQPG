from textblob import TextBlob
from collections import Counter
import os, sys
import collections

reload(sys)  
sys.setdefaultencoding('utf8')
#job_titles = line.decode('utf-8').strip() for line in file.readlines()
text = "What is Artificial Intelligence?this is Artificial Intelligence?"

'''txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
actions between computers and human (natural) languages."""'''

def choosefile(value):
    blob = TextBlob(value)
    b=blob.noun_phrases
    print(b)

choosefile(text)
'''counts = Counter(b)
print(counts)'''

#c = collections.Counter(b)

'''for x in set(b):
    print '%s : %d' % (x, c[x])'''