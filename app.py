from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
from model_pipeline import FoodDetector
from calorie_estimator import CalorieEstimator
from chatbot import NutritionChatbot

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load models ONCE
detector = FoodDetector()
estimator = CalorieEstimator()
chatbot = NutritionChatbot()

# Store session data (simple version)
context_data = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = Image.open(filepath)

    results = detector.detect_food(image)

    if not results:
        return jsonify({"error": "No food detected"})

    top = results[0]
    label = top["label"]
    confidence = float(top["score"])

    nutrition = estimator.estimate_calories(label)

    global context_data
    context_data = nutrition

    return jsonify({
        "label": label,
        "confidence": confidence,
        "nutrition": nutrition,
        "image": filepath
    })


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    response = chatbot.generate_response(user_msg, context_data)

    return jsonify({"response": response})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render uses this
    app.run(host="0.0.0.0", port=port)
