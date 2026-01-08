import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import string

st.title("  🛑 stopwords removals")
text=st.text_area("Enter text area")
if st.button("Remove Stopwords"):
   tokens=word_tokenize(text)
   stop_words=set(stopwords.words('english'))
   punctuation = set(string.punctuation)
   
   
   filtered = [
    word for word in tokens
    if word.lower() not in stop_words and word not in punctuation
   ]

   removed_count=len(tokens)-len(filtered)
   removed_punc = sum(1 for word in tokens if word in punctuation)
   
   st.write("remove stopwords:",removed_count)
   st.write("remove punctuation:",removed_punc)

   
   
