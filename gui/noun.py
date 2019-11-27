import nltk
from textblob import TextBlob
from collections import Counter
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.tokenize import WhitespaceTokenizer
File = open("pdftotextconvertedfile.txt") #open file
lines = File.read() #read all lines
lines=unicode(lines, errors='ignore')
sentences = nltk.sent_tokenize(lines) #tokenize sentences
 #empty to array to hold all nouns
#if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
file = open("noundata.txt","w") 
file2 = open("keywords.txt","w") 
tokenizer = WhitespaceTokenizer()
file3 = open("typeofquestions.txt")
questionkeywordsdata = file3.read().split('\n')
output=[]
for sentence in sentences:
     #print(nltk.pos_tag(sentence)) 
     nouncount=0
     prpcount=0
     nouns = []
     prp = []
     blob = TextBlob(sentence)
     b=blob.noun_phrases
     
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouncount=nouncount+1
             nouns.append(word)
         if (pos == 'PRP' or pos == 'PRP$'):
             prpcount=prpcount+1
             prp.append(word)
     if(nouncount<10 and prpcount<3):
        cp=0
        xa=0;
        print(questionkeywordsdata)
        file.write(str(str(sentence).translate(None, string.whitespace))+"#"+str(b)+"\n") 
        j=0
        strdata="";
        while j<len(questionkeywordsdata):
            datad=questionkeywordsdata[j]
            datad1=datad.split('->')
            question=datad1[0]
            questionKeys=datad1[1].split('=>')
            i=0
            while i < len(questionKeys):
                print(i)
                if(sentence.find(questionKeys[i])>=0 or questionKeys[i]=='all'):
                    if(i==0):
                        strdata=str(strdata)+""+str(questionKeys[i]);
                    else:
                        strdata=str(strdata)+"=>"+str(questionKeys[i]);
                i+=1
            j+=1
        for x in set(b):
                output.append(x)
                aa=x.find('//')
                if(aa!=0):
                    file2.write(str(x)+"->"+str(strdata)+"\n");
file.close()
file2.close()
def questiongenerator():
    f = open("nounphrasesfile.txt","r") 
    data=f.read()
    sentences=data.split("\n")
    for i in range(len(sentences)):
        sentence=sentences[i]
        wordandcount=sentence.split("=>")
        word=wordandcount[0]
        wordcount=wordandcount[1]
#print(nouns)