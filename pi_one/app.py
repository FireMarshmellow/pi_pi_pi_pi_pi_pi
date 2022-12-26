from flask import render_template
from flask import Flask, request
import io
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def display_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def save_text():
    text = request.form['text']
    if not os.path.exists('text.txt'):
        open('text.txt', 'w').close()
    with io.open('text.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    return "Text saved successfully!"

@app.route('/display')
def display_text():
    with io.open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0')
