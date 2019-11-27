from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.tokenize import WhitespaceTokenizer
import nltk
sentence="That should help."
def postag(firstline):
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(firstline))):
		print(str(word)+":"+str(pos))

postag(sentence)