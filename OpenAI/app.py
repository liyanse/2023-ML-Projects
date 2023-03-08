from flask import Flask, render_template, request
import config
import os
import openai


#creating the 404 page (Optional)
def page_not_found(e):
  return render_template('404.html'), 404



##Initialising FLAK
app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)

### Initialise the OPENAI library with the key saved in the CONFIG file
openai.api_key = app.config['OPENAI_KEY']



#####----------START FUNCTIONS--------------------------------------------------------------------
def createImageFromPrompt(prompt):
    response = openai.Image.create(prompt=prompt, n=3, size="512x512")
    return response['data']


#####----------END FUNCTIONS--------------------------------------------------------------------




##View Functions
@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        images = []
        prompt = request.form['prompt']
        res = createImageFromPrompt(prompt)

        if len(res) > 0:
            for img in res:
                images.append(img['url'])

    return render_template('index.html', **locals())



#Run Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)