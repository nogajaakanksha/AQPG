from nltk. corpus import stopwords 
from nltk.tokenize import word_tokenize 
import numpy as np 
import nltk 
def process(file):
    raw = open(file).read()
    raw=unicode(raw, errors='ignore')
    tokens = word_tokenize(raw) 
    words =[w.lower() for w in tokens] 
    porter =nltk.PorterStemmer()
    stemmed_tokens = [porter.stem(t) for t in words] 
    # Removing stop words 
    stop_words =set(stopwords.words('english')) 
    filtered_tokens =[w for w in stemmed_tokens if not w in stop_words] 
    # count words 
    count=nltk.defaultdict(int) 
    for word in filtered_tokens: 
        count[word]+1 
    return count; 
def cos_sim(a,b): 
    dot_product = np.dot(a,b) 
    norm_a=np.linalg.norm(a) 
    norm_b=np.linalg.norm(b) 
    return (dot_product/(norm_a * norm_b))
def getSimilarity(dictl, dict2) :  
    all_words_list= [] 
    for key in dictl: 
        all_words_list.append(key) 
    for key in dict2: 
        all_words_list.append(key) 
    all_words_list_size=len(all_words_list) 
    vl=np.zeros(all_words_list_size, dtype=np.int) 
    v2=np.zeros(all_words_list_size, dtype=np.int)  
    i=0
    for (key) in all_words_list: 
        vl[i]=dictl.get(key,0) 
        v2[i]=dict2.get(key,0) 
        i=i+1
    return cos_sim(vl,v2) 
_name_='_main_'
if _name_=='_main_':
    # python -c "import n[tk; nLtk.downLoad( 'punkt nLtk.downLoad( 'stopwords 
    dictl=process("D:/1.txt") 
    dict2=process("D:/2.txt") 
    dict3=process("D:/3.txt") 
    print(dictl)
    print("similarity between Bug and Bug is ",getSimilarity(dictl,dict2)) 
    print("similarity between Bug#599831 and Bug#1055525 is ",getSimilarity(dictl,dict3)) 
    print("similarity between Bug#599831 and Bug#1055525 is ",getSimilarity(dict2,dict3)) 
