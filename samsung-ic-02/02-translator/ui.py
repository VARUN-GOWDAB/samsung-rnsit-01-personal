# translator_ui.py
# Streamlit app for Hugging Face MarianMT translation
# Imports the translate_text function from translator.py

import streamlit as st
from translator import translate_text

# Page setup
st.set_page_config(page_title="Language Translator", page_icon="🌐")

# Custom background color (light yellow)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff9c4; /* Light yellow */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🌐 Language Translator")

# Input text
src_text = st.text_area("✍️ Enter text to translate:", "")

# Translate button
if st.button("🔄 Translate"):
    if src_text.strip():
        result = translate_text(src_text)
        st.success("✅ Translated Text:")
        st.write(result)
    else:
        st.warning("⚠️ Please enter some text before translating.")
