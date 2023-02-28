#import libraries
import pickle
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
from flask import Flask, request, render_template, jsonify

# Create an instance of Flask
app = Flask(__name__)

# Load pretrained TF model
model = pickle.load(open('model.pickle', 'rb'))

# Define the route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image passed in
    image = request.files['image']
    # Convert the image to an array
    image_array = img_to_array(Image.open(image))
    # Reshape the image according to model
    image_array = image_array.reshape((1, image_array.shape[0], image_array.shape[1], image_array.shape[2]))
    # Make the prediction
    prediction = model.predict(image_array)
    # Get the predicted class label
    prediction_class = np.argmax(prediction)
    # Return the results
    return render_template('index.html', prediction_class=prediction_class,
                           image=image)

# Run the app
if __name__ == '__main__':
    app.run()