import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
#nltk.download('punkt')
text = "AI is amazing. It helps humans."
print("Word Tokens:")
print(word_tokenize(text))
print("\nSentence Tokens:")
print(sent_tokenize(text))
