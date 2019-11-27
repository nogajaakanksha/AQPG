import nltk
File = open("keywords.txt") #open file
lines = File.read()
File2 = open("typeofquestions.txt") #open file
qlines = File2.read()
lines=unicode(lines, errors='ignore')
sentences = lines.split('\n')
qlines=unicode(qlines, errors='ignore')
qsentences = qlines.split('\n')
file3 = open("genratedQuestions.txt","w")
stree=[]
for sentence in sentences:
    categories= sentence.split('->')
    sents=categories[0]
    sen=categories[1].split('=>')
    i=0 
    while i < len(sen):
        for qsentence in qsentences:
            data=qsentence.split('->')
            qs=data[0]
            keys=data[1].split('=>')
            j=0
            while j < len(keys):
                if((sents.find(keys[j])>=0 or keys[j]=='all' )and len(keys[j])>=1):
                    print(keys[j])
                    print(sents.find(keys[j]))
                    s=str(qs)+""+str(sents.replace("/","").replace("=>",""))+"?\n"
                    if s not in stree: 
                        file3.write(str(qs)+""+str(sents.replace("/","").replace("=>",""))+"?\n")
                        stree.append(str(qs)+""+str(sents.replace("/","").replace("=>",""))+"?\n")
                j+=1
        i += 1
#file3.write(str(qs)+""+str(sents.replace("/","").replace("=>",""))+"?\n")
file3.close()