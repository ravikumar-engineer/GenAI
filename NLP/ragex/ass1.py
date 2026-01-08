import streamlit as st
import re

st.title("🔗 URl and 📧 Email cleaner")
text=st.text_area("enter text with URLs or emails")

remove_URL=st.checkbox("remove url")
remove_email=st.checkbox("remove emails")

if st.button("Clean Text"):
  result=text
  if remove_URL:
      result=re.sub(r"http\S+/www\S+","",result)
  
  if remove_email:
      result=re.sub(r"\S+@\S+","",result)

  st.subheader("Cleaned Text:")
  st.write(result)          