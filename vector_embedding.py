import gensim.downloader as api

model = api.load("word2vec-google-news-300")  # download the model and return as object ready for use

word_vectors=model

# Let us look how the vector embedding of a word looks like
# print(word_vectors['computer'])  # Example: Accessing the vector for the word 'computer'
# print(word_vectors['cat'].shape)  # Example: Accessing the vector for the word 'cat'

# Example of using most_similar
# print(word_vectors.most_similar(positive=['king', 'woman'], negative=['man'], topn=10))

# Example of calculating similarity
# print(word_vectors.similarity('woman', 'man'))
# print(word_vectors.similarity('king', 'queen'))
# print(word_vectors.similarity('uncle', 'aunt'))
# print(word_vectors.similarity('boy', 'girl'))
# print(word_vectors.similarity('nephew', 'niece'))
# print(word_vectors.similarity('paper', 'water'))

print(word_vectors.most_similar("tower", topn=5))