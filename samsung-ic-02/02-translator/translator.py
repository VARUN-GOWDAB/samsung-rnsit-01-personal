# translator_app.py
# A simple Hugging Face MarianMT translator for European languages

from transformers import MarianMTModel, MarianTokenizer

def translate_text(text: str, model_name: str = "Helsinki-NLP/opus-mt-en-fr") -> str:
    """
    Translate input text using a Hugging Face MarianMT model.
    
    Args:
        text (str): The source text to translate.
        model_name (str): Hugging Face model name (default: English → French).
    
    Returns:
        str: Translated text.
    """
    # Load tokenizer and model
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize and generate translation
    inputs = tokenizer([text], return_tensors="pt", padding=True)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)

    return translated_text[0]

def main():
    print("=== Hugging Face Translator ===")
    src_text = input("Enter text to translate: ")
    result = translate_text(src_text)
    print("\nSource:", src_text)
    print("Translation:", result)

if __name__ == "__main__":
    main()
