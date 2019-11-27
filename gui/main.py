from Tkinter import *
import sys
import tkMessageBox
from tkFileDialog import *
from textblob import TextBlob
from collections import Counter
import os, sys
import collections
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.tokenize import WhitespaceTokenizer
import nltk
import similarity as similaritys
import string
sys.path.append("D:\\work\\project\\QuestionPaperGeneratorPython\\pdfminer-master\\tools")
import pdf2txt
import random
from fpdf import FPDF
def list_random(contextwisedata,nerwisedata,nounwisedata):
    random.shuffle(contextwisedata)
    random.shuffle(nerwisedata)
    random.shuffle(nounwisedata)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    conlen=len(contextwisedata)
    nerlen=len(nerwisedata)
    nounlen=len(nounwisedata)
    pdf.set_font('arial', 'B', 13.0)
   
    newpaperdata=[]
    newpaperdata.append(".................Context Based Generated Questions.................")
    i=0
    if(conlen>15):
        for i in range(1,15):
           newpaperdata.append("Q"+str(i)+". "+str(contextwisedata[i]))
    else:
        for sent in contextwisedata:
            newpaperdata.append("Q"+str(i)+". "+str(sent))
    newpaperdata.append(".................NER Based Generated Questions.................")
    for i in range(1,15):
        newpaperdata.append("Q"+str(i)+". "+str(nerwisedata[i]))
    newpaperdata.append(".................Noun Based Generated Questions.................")
    for i in range(1,15):
        newpaperdata.append("Q"+str(i)+". "+str(nounwisedata[i]))
    p=1    
    for sent in newpaperdata:
       pdf.cell(ln=p, h=5.0, align='L', w=0, txt="Q"+str(p)+". "+str(sent), border=0)
       p=p+1        
    pdf.output('Question_Paper_New_15.pdf', 'F')
def pdfgenerator():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    i=1
    for sent in contextwisedata:
        pdf.cell(ln=i, h=5.0, align='L', w=0, txt="Q"+str(i)+". "+str(sent), border=0)
        i=i+1
    for sent in nerwisedata:
        pdf.cell(ln=i, h=5.0, align='L', w=0, txt="Q"+str(i)+". "+str(sent), border=0)
        i=i+1
    for sent in nounwisedata:
        pdf.cell(ln=i, h=5.0, align='L', w=0, txt="Q"+str(i)+". "+str(sent), border=0)
        i=i+1    
    pdf.output('Question_Paper.pdf', 'F')
    list_random(contextwisedata,nerwisedata,nounwisedata)
def get_imp_keywords(keyword):
    f = open("keywords.txt","r") 
    data=f.read()
    data=unicode(data, errors='ignore')
    keywords=data.split("\n")
    impkeywords=[]
    for keyword in keywords:
        d=similaritys.similarity("computer", keyword.split("->")[0], True)
        if(d!=0.0):
           impkeywords.append(str(keyword.split("->")[0])+"");
    return impkeywords
def choosefile():
    file = askopenfilename()
    if(file.find(".pdf")==-1):
         message("Error? Plaese choose .pdf files only..")
    else:
        message("You Choose "+str(file)+ " File...")
        global name
        lbl1 = Label(window, text="Choose File Path :", font=("Arial Bold", 10))
        lbl1.pack(side = TOP)
        btn = Button(window, text="Convert File",bg="pink", fg="black",command=pdftotextcovert)
        btn.pack(side = TOP)
        btn1 = Button(window, text="Generate Context Wise Question",bg="pink", fg="black",command=generateQuestion)
        btn1.pack(side = TOP)
        btn3 = Button(window, text="Generate NER based Question",bg="pink", fg="black",command=nerquestiongenerator)
        btn3.pack(side = TOP)
        btn2 = Button(window, text="Generate noun phrases wise Question",bg="pink", fg="black",command=qagenerator)
        btn2.pack(side = TOP)
        btn4 = Button(window, text="Generate Question Paper",bg="pink", fg="black",command=pdfgenerator)
        btn4.pack(side = TOP)
        lbl1.configure(text="Input File Path :"+file)  
        name=file
def pdftotextcovert():
    print "***File Path :"+name
    arr = ['arguments', '-o', 'pdftotextconvertedfile.txt',name]
    pdf2txt.main(arr)
    f = open("pdftotextconvertedfile.txt","r") 
    data=f.read()
    data=unicode(data, errors='ignore')
    loadfiledata()
def message(msg):
    tkMessageBox.showinfo("Alert", str(msg))
def readfile(path):
    f = open(path,"r") 
    data=f.read()
    data=unicode(data, errors='ignore')
    return data
def loadfiledata():
    filedata=readfile("pdftotextconvertedfile.txt")
    s = Scrollbar(window)
    T = Text(window)
    T.insert(END,filedata)
    T.focus_set()
    s.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    s.config(command=T.yview)
    T.config(yscrollcommand=s.set)
    #label.pack()
def postag(firstline):
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(firstline))):
        if(pos=='VBZ' or pos=='MD'):
            return word
    return ""
def nerdetetcion(doc):
    tokenized_doc = nltk.word_tokenize(doc)
    tagged_sentences = nltk.pos_tag(tokenized_doc)
    ne_chunked_sents = nltk.ne_chunk(tagged_sentences)
    named_entities = []
    for tagged_tree in ne_chunked_sents:
        if hasattr(tagged_tree, 'label'):
            entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) #
            entity_type = tagged_tree.label() # get NE category
            named_entities.append(str(entity_name)+"=>"+str(entity_type))
    return named_entities
contextwisedata=[]
nerwisedata=[]
nounwisedata=[]
def nerquestiongenerator():
    File = open("pdftotextconvertedfile.txt") #open file
    lines = File.read()
    lines=unicode(lines, errors='ignore')
    sentences =lines.split('\n')
    file = open("ner-type-question.txt","w") 
    File2 = open("nertypequestionkeywords.txt") #open file
    WordsList = File2.read()
    scrollbar = Scrollbar(window)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(window,width=50, height=20, yscrollcommand = scrollbar.set)
    WordsList=unicode(WordsList, errors='ignore')
    WordsListDatas =WordsList.split('\n')     
    for sentence in sentences:
        sents=sentence.split('.')
        for sent in sents:
            tokenized_doc = nltk.word_tokenize(sent)
            aux_word=postag(sent)
            tagged_trees= nerdetetcion(sent)
            remain_sent=sent.replace(aux_word,"")
            for tagged_tree in tagged_trees:
                word=tagged_tree.split("=>")[0]
                nertype=tagged_tree.split("=>")[1]
                for WordsListData in WordsListDatas:
                    WordsData =WordsListData.split('=>')
                    if (nertype==WordsData[0]):
                        first_sentence=remain_sent[0:remain_sent.find(word)]
                        next_sentence=remain_sent[remain_sent.find(word)+len(word):]
                        question=str(WordsData[1])+" "+str(aux_word)+" "+str(next_sentence)+" "+str(first_sentence)+"?";
                        qlength=len(question)
                        if(qlength>30):
                           mylist.insert(END,str(WordsData[1])+" "+str(aux_word)+" "+str(next_sentence)+" "+str(first_sentence)+"?\n")
                           nerwisedata.append(str(question)+"\n")
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )  
    file.close()  
   
def qagenerator():
    File = open("keywords.txt") #open file
    lines = File.read()
    scrollbar = Scrollbar(window)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(window,width=100, height=20, yscrollcommand = scrollbar.set)
    File2 = open("typeofquestions.txt") #open file
    qlines = File2.read()
    lines=unicode(lines, errors='ignore')
    sentences = lines.split('\n')
    qlines=unicode(qlines, errors='ignore')
    qsentences = qlines.split('\n')
    stree=[]
    for sentence in sentences:
        categories= sentence.split('->')
        sents=categories[0]
        sen=categories[1].split('=>')
        d=similaritys.similarity("computer",sents, True)
        if(d!=0.0):
            i=0 
            while i < len(sen):
                for qsentence in qsentences:
                    data=qsentence.split('->')
                    qs=data[0]
                    keys=data[1].split('=>')
                    j=0
                    while j < len(keys):
                        if((sents.find(keys[j])>=0 or keys[j]=='all' )and len(keys[j])>=1):
                            s=str(qs)+""+str(sents.replace("/","").replace("=>",""))+"?"
                            if s not in stree: 
                                mylist.insert(END,str(s)+"\n")
                                nounwisedata.append(str(s)+"\n")
                                stree.append(str(s))
                        j+=1
                i += 1
    
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
    
def keywordwisegenerateQuestion():
    file3 = open("typeofquestions.txt")
    questionkeywordsdata = file3.read().split('\n')
    File = open("pdftotextconvertedfile.txt") #open file
    lines = File.read() #read all lines
    lines=unicode(lines, errors='ignore')
    sentences = nltk.sent_tokenize(lines) #tokenize sentences
    file2 = open("keywords.txt","w") 
    tokenizer = WhitespaceTokenizer()
    output=[]
    for sentence in sentences:
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
            j=0
            strdata="";
            while j<len(questionkeywordsdata):
                datad=questionkeywordsdata[j]
                datad1=datad.split('->')
                question=datad1[0]
                questionKeys=datad1[1].split('=>')
                i=0
                while i < len(questionKeys):
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
    file2.close()
    qagenerator()
def generateQuestion():
    File2 = open("DiscourseWordsList.txt") #open file
    WordsList = File2.read()
    WordsList=unicode(WordsList, errors='ignore')
    WordsListDatas =WordsList.split('\n')
    filedata=readfile("pdftotextconvertedfile.txt")
    sentences =filedata.split('\n')
    #s = Scrollbar(window)
    #T = Text(window)
    scrollbar = Scrollbar(window)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(window,width=50, height=20, yscrollcommand = scrollbar.set )
    for sentence in sentences:
        sents=sentence.split('.')
        for sent in sents:
            tokenized_doc = nltk.word_tokenize(sent)
            for WordsListData in WordsListDatas:
                WordsData =WordsListData.split('=>')
                lastindex=sent.lower().find(str(WordsData[0].lower()))
                if(lastindex==-1):
                    lastindex=0
                firstline=sent[0:lastindex]
                auxiwordpos=postag(firstline)
                if(firstline!='' and auxiwordpos!=''):
                    firstline=firstline.replace(str(auxiwordpos),'')
                    qtypes=WordsData[1].split(',')
                    for qtype in qtypes:
                        question=str(qtype)+" "+str(auxiwordpos)+" "+str(firstline)+"?"
                        qlength=len(question)
                        if(qlength>30):
                           # T.insert(END,str(qtype)+" "+str(auxiwordpos)+" "+str(firstline)+"?\n")
                            contextwisedata.append(str(qtype)+" "+str(auxiwordpos)+" "+str(firstline)+"?")
                            mylist.insert(END,str(qtype)+" "+str(auxiwordpos)+" "+str(firstline)+"?\n")
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )                        
def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def gui():
    global window
    window = Tk()
    window.geometry('800x600')

    window.configure(background='pink')
    window.title("Welcome to  Question Paper Generator Python")
    # menu creation
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=choosefile)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)



    lbl = Label(window, background = "pink",text="Question Paper Generator", font=("Arial Bold", 20))
    lbl.pack( side = TOP)


    #btn.grid(column=0, row=4)
    #btn1 = Button(window, text="Choose File",bg="orange", fg="red")
     
    #btn1.grid(column=0, row=2)
    window.mainloop()
gui()