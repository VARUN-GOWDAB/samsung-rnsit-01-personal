from flask import Flask, render_template, request, jsonify, session
from groq import Groq
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ── Groq config ──────────────────────────────────────────────────────────────
API_KEY = ""   # Replace with your actual Groq API key
MODEL   = "llama-3.1-8b-instant"
client  = Groq(api_key=API_KEY)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data       = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    # Persist conversation history in the Flask session
    if "messages" not in session:
        session["messages"] = []

    session["messages"].append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=session["messages"]
        )
        reply = response.choices[0].message.content
        session["messages"].append({"role": "assistant", "content": reply})
        session.modified = True
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset():
    session.pop("messages", None)
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)
