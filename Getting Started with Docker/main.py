import pickle
import numpy as np
from PIL import Image

# Load the trained model from the pickle file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    

# Open the image
image = Image.open('image1.jpg')

# Preprocess the image
image = image.resize((224, 224))  # Resize the image to match the input size of the model
image = np.array(image)  # Convert the image to a numpy array
image = image / 255.0  # Normalize the pixel values

# Add a batch dimension to the image
image = np.expand_dims(image, axis=0)

# Use the loaded model to predict the class of the image
prediction = model.predict(image)

# Output the predicted class name
class_names = ['class1', 'class2', 'class3']  # Replace with your own class names
predicted_class_index = np.argmax(prediction)
predicted_class_name = class_names[predicted_class_index]
print(predicted_class_name)
