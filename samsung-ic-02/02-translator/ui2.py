# translator_ui.py
# Streamlit app for Hugging Face MarianMT translation
# Imports translate_text from translator.py

import streamlit as st
from translator import translate_text

# Mapping of target languages to MarianMT models
LANGUAGE_MODELS = {
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Italian": "Helsinki-NLP/opus-mt-en-it",
    "Portuguese": "Helsinki-NLP/opus-mt-en-pt",
}

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

# Dropdown for target language
target_lang = st.selectbox("🌍 Select target language:", list(LANGUAGE_MODELS.keys()))

# Translate button
if st.button("🔄 Translate"):
    if src_text.strip():
        model_name = LANGUAGE_MODELS[target_lang]
        result = translate_text(src_text, model_name=model_name)
        st.success(f"✅ Translation to {target_lang}:")
        st.write(result)
    else:
        st.warning("⚠️ Please enter some text before translating.")
