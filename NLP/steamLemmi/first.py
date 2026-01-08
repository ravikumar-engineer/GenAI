from nltk.stem import PorterStemmer,LancasterStemmer
word='organization'
porter=PorterStemmer()
Lancaster=LancasterStemmer()
print(porter.stem(word))
print(Lancaster.stem(word))