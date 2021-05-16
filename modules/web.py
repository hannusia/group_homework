from flask import Flask, request, render_template
from diagram_builder import create_diagrams
import os
import shutil
from group_homework.modules.url_check import url_check
from twitter_api import TwitterAPIParser


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    
    text = request.form['input_text']
    if url_check(text):
        t = TwitterAPIParser(text)
        text = t.get_text()
    with open('text.txt', 'w') as file:
        file.write(text)
    img_1, img_2, suitable_age = create_diagrams('text.txt')
    return render_template('results.html', post=text, result=suitable_age, image_1 = img_1, image_2 = img_2)

if __name__ == '__main__':
    if os.path.exists('static'):
        shutil.rmtree('static')
    app.run()