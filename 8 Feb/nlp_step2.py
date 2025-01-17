

from sklearn.feature_extraction.text import CountVectorizer


corpus = [
    'i love the book',
    'this book was not so great',
    'the fit was great',
    'i love the shoes'
]

books = 'Books'
clothing = 'Clothing'

categories = [books, books, clothing, clothing]

vectorizer = CountVectorizer(ngram_range= (1,2))

vectors = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(vectors.toarray())


