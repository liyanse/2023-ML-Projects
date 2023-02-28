import tensorflow as tf
from flask import Flask, request, jsonify

# Create Flask app
app = Flask(__name__)

# Load pretrained model
model = tf.keras.models.load_model('my_model.h5')

@app.route('/prediction', methods=['POST'])
def prediction():
    # Get the image data from the request
    data = request.files['image'].read()
    # Prepare the image
    image = tf.image.decode_jpeg(data, channels=3)
    image = tf.image.resize(image, [224, 224])
    # Make the prediction
    prediction = model.predict(image[None, ...])
    # Return the prediction
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run()