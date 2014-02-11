train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.","We can see the shining sun, the bright sun.")
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
print vectorizer
vectorizer.fit_transform(train_set)
print vectorizer.vocabulary

smatrix = vectorizer.transform(test_set)

freq_term_matrix=smatrix.todense()
print freq_term_matrix

from sklearn.feature_extraction.text import TfidfTransformer

tfidf = TfidfTransformer(norm="l2")
tfidf.fit(smatrix)

print "IDF:"
tf_idf_matrix = tfidf.transform(freq_term_matrix)
print tf_idf_matrix.todense()
