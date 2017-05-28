import os
import nltk
from nltk.sem import relextract
from nltk.corpus import ieer
from nltk.sem import relextract
from nltk.tree import Tree


BASE_DIR = "15_docs"
#
class doc():
    pass

def extract_relations(text):
    relations = []
    doc.text = text
    sentences = nltk.sent_tokenize(doc.text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    i = 1
    for sent in tagged_sentences:
        sent = nltk.ne_chunk(sent)
        # print (sent)
        pairs = relextract.tree2semi_rel(sent)
        reldicts = relextract.semi_rel2reldict(pairs)

        for r in reldicts:
            lfilter = r['filler'].split("/")[0]
            relations.append("Relation{}: {} ({})".format(i,lfilter,r['subjtext']))
            i = i + 1

    return relations

if __name__ == '__main__':
    files = [f for f in os.listdir(BASE_DIR) if f.endswith('.txt')]
    for f in files:
        extract_relations(f)
