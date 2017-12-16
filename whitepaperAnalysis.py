# TUTORIAL https://www.kernix.com/blog/similarity-measure-of-textual-documents_p12
# GITHUB LIST https://github.com/masonicGIT/ico-whitepapers
# https://stackoverflow.com/questions/44786888/will-word2vec-be-more-efficient-in-text-based-plagiarism-detection-than-wordnet
# from sklearn.datasets import fetch_20newsgroups

from nltk import word_tokenize
from nltk import download
from nltk.corpus import stopwords

import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

import numpy as np
from gensim import corpora
from gensim.models import TfidfModel
from gensim.models import LsiModel
from gensim.similarities import MatrixSimilarity

download('punkt')
download('stopwords')

corpusdir = './txts' # Directory of corpus.
all_files = PlaintextCorpusReader(corpusdir, '.*')
fileids = all_files.fileids()
print fileids
print len(fileids)
texts = []
fileindex = []
i = 0;
for fileid in fileids:
	texts.append(all_files.raw(fileids=fileid))
	fileindex.append(fileid)
	i += 1

stop_words = stopwords.words('english')

def preprocess(text):
    text = text.lower()
    doc = word_tokenize(text)
    doc = [word for word in doc if word not in stop_words]
    doc = [word for word in doc if word.isalpha()]
    return doc
texts_og = texts
corpus = [preprocess(text) for text in texts]

number_of_docs = len(corpus)
print number_of_docs


def filter_docs(corpus, texts, labels, condition_on_doc):
    """
    Filter corpus, texts and labels given the function condition_on_doc which takes
    a doc.
    The document doc is kept if condition_on_doc(doc) is true.
    """
    number_of_docs = len(corpus)

    if texts is not None:
        texts = [text for (text, doc) in zip(texts, corpus)
                 if condition_on_doc(doc)]

    labels = [i for (i, doc) in zip(labels, corpus) if condition_on_doc(doc)]
    corpus = [doc for doc in corpus if condition_on_doc(doc)]

    print("{} docs removed".format(number_of_docs - len(corpus)))

    return (corpus, texts, labels)

corpus, texts, texts_og = filter_docs(corpus, texts, texts_og, lambda doc: (len(doc) != 0))
# print corpus
sims = {'texts': {}}
# This module implements the concept of Dictionary- a mapping between words and their integer ids, created from corpus.
dictionary = corpora.Dictionary(corpus)
print dictionary #prints unique tokens (words) in corpus
corpus_gensim = [dictionary.doc2bow(doc) for doc in corpus] ## converts to B.O.W model- {word, frequency}
# print corpus_gensim
tfidf = TfidfModel(corpus_gensim) #Runs TFID on bag of words model
corpus_tfidf = tfidf[corpus_gensim]
lsi = LsiModel(corpus_tfidf, id2word=dictionary, num_topics=200)
lsi_index = MatrixSimilarity(lsi[corpus_tfidf])
sims['texts']['LSI'] = np.array([lsi_index[lsi[corpus_tfidf[i]]]
                                for i in range(len(corpus))])
# FIND WAY TO
def most_similar(i, X_sims, topn=None):
    """return the indices of the topn most similar documents with document i
    given the similarity matrix X_sims"""

    r = np.argsort(X_sims[i])[::-1]
    if r is None:
        return r
    else:
        return r[:topn]

# print sims['texts']['LSI']
results = most_similar(36, sims['texts']['LSI'], 5)
print "\nMost similar papers to ", fileindex[36], "\n"
for idx, val in enumerate(results):
	print fileindex[val]
print(most_similar(36, sims['texts']['LSI'], 5))
# Returns the most similar whitepapers to yours


