import sklearn_crfsuite
from sklearn_crfsuite import metrics

# Sample training data (Word, POS, NER)
train_data = [
    [('John','NNP','B-PER'),('lives','VBZ','O'),('in','IN','O'),('India','NNP','B-LOC')],
    [('Mary','NNP','B-PER'),('works','VBZ','O'),('at','IN','O'),('Google','NNP','B-ORG')]
]

def word2features(sent, i):
    word, pos, _ = sent[i]
    return {
        'word': word,
        'pos': pos,
        'is_upper': word.isupper(),
        'is_title': word.istitle(),
    }

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for _,_,label in sent]

X_train = [sent2features(s) for s in train_data]
y_train = [sent2labels(s) for s in train_data]

crf = sklearn_crfsuite.CRF()
crf.fit(X_train, y_train)

# Test sentence
test = [[('Alice','NNP','O'),('is','VBZ','O'),('from','IN','O'),('London','NNP','O')]]
X_test = [sent2features(s) for s in test]

print(crf.predict(X_test))