import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
print(lem.lemmatize("cooking", pos='v'))
print(lem.lemmatize("dancing", pos='v'))
print(lem.lemmatize("better", pos='a')) #a--->adverb