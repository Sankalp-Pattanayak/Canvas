from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
from flask_cors import CORS  # Add this for handling CORS issues

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

model = load_model('mnist_model.h5')

@app.route('/')
def home():
    return render_template('index.html')  # This serves your HTML page

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    image = np.array(data['image'])
    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)
    image = tf.image.resize(image, (28, 28))
    # image = image / 255.0  # Normalize the image

    prediction = model.predict(image)
    predicted_class = int(np.argmax(prediction))

    return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
