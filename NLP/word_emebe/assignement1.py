import gensim.downloader as api
import numpy as np
model = api.load("word2vec-google-news-300")
text ="machine learning is great"
words = [
    word for word in text.lower().split()
    if word in model.key_to_index
]  