# AI Chatbot — Flask + Groq

A simple Flask web app wrapping a Groq-powered Llama 3.1 chatbot into a polished landing page with a floating chat popup.

## Project Structure

```
chatbot-flask/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── README.md
└── templates/
    └── index.html       # Landing page + chat popup UI
```

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key
Open `app.py` and replace the placeholder:
```python
API_KEY = "YOUR_API_KEY_HERE"
```
Get a free key at https://console.groq.com

### 3. Run the app
```bash
python app.py
```

### 4. Open in browser
Visit http://127.0.0.1:5000

## Features
- Landing page with feature cards and how-it-works section
- Floating chat bubble (bottom-right corner)
- Animated pop-up chat window
- Conversation history preserved per session
- Clear chat button to reset history
- Typing indicator while waiting for a response
- Keyboard shortcut: Enter to send, Shift+Enter for newline
