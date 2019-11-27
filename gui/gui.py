from Tkinter import *
import sys


from tkMessageBox import *
from tkFileDialog import *
from textblob import TextBlob
from collections import Counter
import os, sys
import collections
sys.path.append("D:\\work\\project\\QuestionPaperGeneratorPython\\pdfminer-master\\tools")
import pdf2txt
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import wordnet as wn

lemmatizer = WordNetLemmatizer()

window = Tk()
window.geometry('700x500')
window.title("Welcome to  Question Paper Generator Python")

lbl = Label(window, text="Input File Path :", font=("Arial Bold", 10))

lbl.grid(column=0, row=0)

lbl1 = Label(window, text="File Data :", font=("Arial Bold", 10))

lbl1.grid(column=0, row=6)
def questiongenerator():
    f = open("nounphrasesfile.txt","r") 
    data=f.read()
    sentences=data.split("\n")
    for i in range(len(sentences)):
        sentence=sentences[i]
        wordandcount=sentence.split("=>")
        word=wordandcount[0]
        wordcount=wordandcount[1]
        
def choosefile():
    file = askopenfilename()
    print "Input File Path :"+file
    lbl.configure(text="Input File Path :"+file)    
    global name
    name=file
    

def nounphrases(value):
    reload(sys)  
    sys.setdefaultencoding('ascii')
    blob = TextBlob(value)
    b=blob.noun_phrases
    for sentence in blob.sentences:
        print(sentence.sentiment.polarity)
    c = collections.Counter(b)
    file = open("nounphrasesfile.txt","w") 
    file2 = open("scorewiseword.txt","w") 
    for x in set(b):
        #print '%s : %d' % (x, c[x])
        file.write(lemmatizer.lemmatize(str(x))+"=>"+str(c[x])+"\n")
    file.close()
    
def pdftotextcovert():
    print "***File Path :"+name
    arr = ['arguments', '-o', 'pdftotextconvertedfile.txt',name]
    pdf2txt.main(arr)
    f = open("pdftotextconvertedfile.txt","r") 
    data=f.read()
    data=unicode(data, errors='ignore')
    testdata=""
    wordList = re.sub("[^\w]", " ",  data).split()
    for i in range(len(wordList)):
        testdata=testdata+" "+lemmatizer.lemmatize(wordList[i])
    lbl1.configure(text="File Data :"+testdata)
    nounphrases(testdata)
def similarity(word1,word2):
    w1 = word1
    w2 = word2
    s1 = wn.synsets(w1)
    s2 = wn.synsets(w2) 
    ss1 = s1[0]
    ss2 = s2[0]
    return ss1.path_similarity(ss2)
btn = Button(window, text="Convert File",bg="pink", fg="black", command=pdftotextcovert)
 
btn.grid(column=0, row=4)
btn1 = Button(window, text="Choose File",bg="orange", fg="red", command=choosefile)
 
btn1.grid(column=0, row=2)

window.mainloop()
