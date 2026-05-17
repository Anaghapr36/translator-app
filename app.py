from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def home():
    translated_text = ""

    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['lang']

        result = translator.translate(text, dest=lang)
        translated_text = result.text

    return render_template('index.html', translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)