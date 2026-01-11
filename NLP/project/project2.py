import streamlit as st
import re
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import pandas as pd
from nltk.tokenize import word_tokenize
import spacy
from gensim.models import Word2Vec


nlp = spacy.load("en_core_web_sm")
st.set_page_config(
    page_title="NLP feature extraction using Regex",
    layout="wide"
)

st.write("Tokenization, Text Cleaning, TF-IDF,Word2Vec")

text = st.text_area(
    "Enter text for NLP preprocessing",
    height=150,
    placeholder="Example: Ravi is the HOD of HIT and loves NLP"
)

# Sidebar options
option = st.sidebar.radio(
    "Select NLP Technique",
    [
        "Tokenization",
        "Text cleaning",
        "TF-IDF",
        "Word2Vec"
    ]
)


# Process Button
if st.button("Process Text"):
    if text.strip() == "":
        st.warning("Please enter some text")
        
        # ---------------- TOKENIZATION ----------------
    
    elif option == "Tokenization":
         st.subheader("Tokenization Output")
         col1,= st.columns(1)
         
         
         with col1:
            st.markdown("### Word Tokenization")
            words = word_tokenize(text)
            st.write(words) 
    
    elif option =="Text cleaning":
         st.subheader("Text Cleaning Output")
         
         text_lower = text.lower()
         
         # Remove numbers
         text_no_digits = re.sub(r'\d+', '', text_lower)
         
           # Remove punctuation & special characters
         text_no_punct = re.sub(r'[^\w\s]', '', text_no_digits)
         
          #Remove extra spaces
         cleaned_text = re.sub(r'\s+', ' ', text_no_punct).strip()
         
            # 5. Stopword removal using SpaCy
         doc = nlp(cleaned_text)
         final_words = [
              token.text for token in doc
              if not token.is_stop
          ]

         st.markdown("### Original Text")
         st.write(text)

         st.markdown("### Cleaned Text (Using Regex)")
         st.write(" ".join(final_words))
         
         
    elif option =="TF-IDF":
           st.subheader("TF-IDF Output")
           vectorizer=TfidfVectorizer(lowercase=True,stop_words='english')
           X=vectorizer.fit_transform([text])
           df=pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names_out())
           st.dataframe(df, use_container_width=True)
           
    elif option == "Word2Vec":
          st.subheader("Word2Vec Output")

    # Multiple documents: one sentence per line
          texts = [line for line in text.split("\n") if line.strip() != ""]

          if len(texts) < 2:
              st.warning("Please enter at least 2 sentences (one per line)")
          else:
              # Tokenize each sentence
             tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in texts]

            # Train Word2Vec model
             model = Word2Vec(
               sentences=tokenized_sentences,
               vector_size=10,
               window=5,
               min_count=1,
               workers=4
            )

           # Vocabulary words
             vocab = list(model.wv.index_to_key)

           # Create DataFrame of word vectors
             word_vectors = pd.DataFrame(
                [model.wv[word] for word in vocab],
                index=vocab
             )

          st.markdown("### Word Embeddings (Word Vectors)")
          st.dataframe(word_vectors, use_container_width=True)

           
         
         
         
         
