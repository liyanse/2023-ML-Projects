from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def get_random_user():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()['results'][0]

    # Extract the name information
    title = data['name']['title']
    first_name = data['name']['first']

    # Extract the country information using a for loop
    location = data['location']
    for key, value in location['country'].items():
        if key == 'name':
            country = value

    # Return the extracted information as a JSON response
    return jsonify({
        'title': title,
        'first_name': first_name,
        'country': country
    })

if __name__ == '__main__':
    app.run(debug=True)
