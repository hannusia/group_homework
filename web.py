from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    text = request.form['input_text']
    return text

if __name__ == '__main__':
    app.run()