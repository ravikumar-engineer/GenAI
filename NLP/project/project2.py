import streamlit as st
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import spacy
from gensim.models import Word2Vec

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Page config
st.set_page_config(
    page_title="NLP Feature Extraction using Regex",
    layout="wide"
)

st.title("NLP Feature Extraction App")
st.write("Tokenization | Text Cleaning | TF-IDF | Word2Vec")

# Text input
text = st.text_area(
    "Enter text for NLP preprocessing",
    height=150,
    placeholder="Example:\nRavi is the HOD of HIT.\nHe loves NLP."
)

# Sidebar options
option = st.sidebar.radio(
    "Select NLP Technique",
    ["Tokenization", "Text cleaning", "TF-IDF", "Word2Vec"]
)

# Process button
if st.button("Process Text"):

    if text.strip() == "":
        st.warning("Please enter some text")

    # ---------------- TOKENIZATION ----------------
    elif option == "Tokenization":
        st.subheader("Tokenization Output")
        words = word_tokenize(text)
        st.write(words)

    # ---------------- TEXT CLEANING ----------------
    elif option == "Text cleaning":
        st.subheader("Text Cleaning Output")

        text_lower = text.lower()
        text_no_emails = re.sub(
             r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',
             '',
             text_lower
        )

       # 3. Remove URLs
        text_no_urls = re.sub(
            r'(https?://\S+|www\.\S+)',
            '',
            text_no_emails
        )
        
        text_no_digits = re.sub(r'\d+', '', text_no_urls)
        text_no_punct = re.sub(r'[^\w\s]', '', text_no_digits)
        cleaned_text = re.sub(r'\s+', ' ', text_no_punct).strip()

        # Stopword removal using SpaCy
        doc = nlp(cleaned_text)
        final_words = [token.text for token in doc if not token.is_stop]

        st.markdown("### Original Text")
        st.write(text)

        st.markdown("### Cleaned Text")
        st.write(" ".join(final_words))

    # ---------------- TF-IDF ----------------
    elif option == "TF-IDF":
        st.subheader("TF-IDF Output")

        vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words='english'
        )
        X = vectorizer.fit_transform([text])

        df = pd.DataFrame(
            X.toarray(),
            columns=vectorizer.get_feature_names_out()
        )

        st.dataframe(df, use_container_width=True)

    # ---------------- WORD2VEC ----------------
    elif option == "Word2Vec":
        st.subheader("Word2Vec Output")

        texts = [line for line in text.split("\n") if line.strip() != ""]

        if len(texts) < 2:
            st.warning("Please enter at least 2 sentences (one per line)")
        else:
            tokenized_sentences = [
                word_tokenize(sentence.lower())
                for sentence in texts
            ]

            model = Word2Vec(
                sentences=tokenized_sentences,
                vector_size=10,
                window=5,
                min_count=1,
                workers=4
            )

            vocab = list(model.wv.index_to_key)

            word_vectors = pd.DataFrame(
                [model.wv[word] for word in vocab],
                index=vocab
            )

            st.markdown("### Word Embeddings (Word Vectors)")
            st.dataframe(word_vectors, use_container_width=True)
