from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.tokenize import WhitespaceTokenizer
import nltk
File = open("pdftotextconvertedfile.txt") #open file
lines = File.read()
lines=unicode(lines, errors='ignore')
sentences =lines.split('\n')
File2 = open("DiscourseWordsList.txt") #open file
WordsList = File2.read()
WordsList=unicode(WordsList, errors='ignore')
WordsListDatas =WordsList.split('\n')

def nerdetetcion(tagged_sentences):
    ne_chunked_sents = nltk.ne_chunk(tagged_sentences)
    named_entities = []
    for tagged_tree in ne_chunked_sents:
        if hasattr(tagged_tree, 'label'):
            entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) #
            entity_type = tagged_tree.label() # get NE category
            named_entities.append((entity_name, entity_type))
    return named_entities
def postag(firstline):
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(firstline))):
		#print(str(word)+":"+str(pos))
		if(pos=='VBZ' or pos=='MD'):
			return word
    return ""
file = open("DiscourseWiseQuestions.txt","w")      
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
                    file.write(str(qtype)+" "+str(auxiwordpos)+" "+str(firstline)+"?\n")
file.close()   
    
       
