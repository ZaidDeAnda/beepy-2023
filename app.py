import streamlit as st

image = st.file_uploader(label="sube tu imagen")

if image:
    st.image(image)