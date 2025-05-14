from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model
model = joblib.load("cybersecurity_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[data["packet_size"], data["failed_logins"], data["request_frequency"]]])
    prediction = model.predict(features)
    return jsonify({"Threat_Detected": bool(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
