import streamlit as st
from nltk.tokenize import word_tokenize,sent_tokenize
import nltk

# nltk.download("punkt")
# nltk.download("punkt_tab")
st.title("Text Tokenizier app")
text=st.text_area("Enter your Text:")
if st.button("Analyze"):
    if text.strip():
      sentences=sent_tokenize(text)
      words=word_tokenize(text)
      
      #display the results
      st.write("$$$ Result")
      st.write("Sentence count:", len(sentences))
      st.write("First word:", words[0] if words else "")
      st.write("Last word:", words[-1] if words else "")
    
      st.write("### Sentences")
      for i, sent in enumerate(sentences,start=1):
          st.write(f"{i}.{sent}")
    else:
        st.warning("please enter some text to analyze.")        
      
      
     
    
    
     
