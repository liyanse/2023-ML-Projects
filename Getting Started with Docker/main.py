from flask import Flask, request, jsonify
from tensorflow import keras
import numpy as np
import base64
import cv2

# Load the Keras model
model = keras.models.load_model('myModel.h5')

# Create a Flask app
app = Flask(__name__)

# Define a route to handle image classification
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image data from the request
    image_data = request.json['image']

    # Convert the base64 image data to a numpy array
    image_bytes = base64.b64decode(image_data)
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Preprocess the image
    image = cv2.resize(image, (224, 224))
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)

    # Make a prediction
    prediction = model.predict(image)[0]
    label = np.argmax(prediction)
    confidence = prediction[label]

    # Return the prediction results as JSON
    response = {
        'label': str(label),
        'confidence': str(confidence)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
