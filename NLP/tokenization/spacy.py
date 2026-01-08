import spacy
nlp=spacy.load("en_core_web_sm")
doc=nlp("spaCy is very powerful. . ")
tokens_text=[token.text for token in doc]
tokens_obj=[token for token in doc]
print(tokens_text) # return only the string
print(tokens_obj) # return the complete token