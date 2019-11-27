from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.tokenize import WhitespaceTokenizer
import nltk
File = open("pdftotextconvertedfile.txt") #open file
lines = File.read()
lines=unicode(lines, errors='ignore')
sentences =lines.split('\n')
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
file = open("ner-type-question.txt","w") 
File2 = open("nertypequestionkeywords.txt") #open file
WordsList = File2.read()
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
                    file.write(str(WordsData[1])+" "+str(aux_word)+" "+str(next_sentence)+" "+str(first_sentence)+"?\n")
file.close()   