from flask import Flask, render_template, request, jsonify
import json, random, os

app = Flask(__name__)

# Load responses from JSON
RESPONSES_FILE = os.path.join(os.path.dirname(__file__), "responses.json")
with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
    RESPONSES = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = (data.get("message") or "").lower()

    for entry in RESPONSES:
        for keyword in entry.get("keywords", []):
            if keyword in message:
                return jsonify({"reply": entry["reply"]})
    fallback = random.choice([r["reply"] for r in RESPONSES if r.get("fallback", False)])
    return jsonify({"reply": fallback})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
