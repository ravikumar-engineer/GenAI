from sklearn.feature_extraction.text import CountVectorizer
corpous=["I love biryani","I love jalebi"]
vector=CountVectorizer()
X=vector.fit_transform(corpous)
print(X) # it gives sparse matrix
print(X.toarray()) 
print(vector.get_feature_names_out())