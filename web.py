from flask import Flask, request, render_template
from read import CleanText
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    text = CleanText(request.form['input_text'])
    return text.clean()

if __name__ == '__main__':
    app.run()