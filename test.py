from gensim.models import doc2vec
import random
from collections import namedtuple
from gensim.models.doc2vec import LabeledSentence


# Load data

# doc1 = ["This is a sentence", "This is another sentence"]
doc1 = ["This is a sentence", "This is a sentence"]


# Transform data (you can add more data preprocessing steps)

docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(doc1):
    words = text.lower().split()
    tags = [i]
    docs.append(analyzedDocument(words, tags))

# Train model (set min_count = 1, if you want the model to work with the provided example data set)

model = doc2vec.Doc2Vec(docs, size = 100, window = 300, min_count = 1, workers = 4)

# Get the vectors

print model.docvecs[0]
print model.docvecs[1]