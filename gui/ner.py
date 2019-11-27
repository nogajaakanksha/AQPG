import nltk

doc = '''Andrew Yan-Tak Ng is a Chinese American computer scientist.

He is the former chief scientist at Baidu, where he led the company's

Artificial Intelligence Group. He is an adjunct professor (formerly 

associate professor) at Stanford University. Ng is also the co-founder

and chairman at Coursera, an online education platform. Andrew was born

in the UK in 1976. His parents were both from Hong Kong.'''

# tokenize doc

tokenized_doc = nltk.word_tokenize(doc)

 

# tag sentences and use nltk's Named Entity Chunker

tagged_sentences = nltk.pos_tag(tokenized_doc)

ne_chunked_sents = nltk.ne_chunk(tagged_sentences)

 

# extract all named entities

named_entities = []

for tagged_tree in ne_chunked_sents:

    if hasattr(tagged_tree, 'label'):

        entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) #

        entity_type = tagged_tree.label() # get NE category

        named_entities.append((entity_name, entity_type))

print(named_entities)