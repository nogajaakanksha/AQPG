import similarity as s

def getimpkeywords():
    f = open("keywords.txt","r") 
    file2 = open("impkeywords.txt","w") 
    data=f.read()
    data=unicode(data, errors='ignore')
    keywords=data.split("\n")
    impkeywords=[]
    for keyword in keywords:
        d=s.similarity("computer", keyword.split("->")[0], True)
        if(d!=0.0):
           impkeywords.append(str(keyword.split("->")[0])+"");
    return impkeywords
readfile()