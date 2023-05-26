from flask import Flask, render_template, request
from model import summarize

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    raw_text = request.form['rawtext']
    summary, doc, len_original_txt, len_summary = summarize(raw_text)
    return render_template('index.html', summary=summary, len_original_txt=len_original_txt, len_summary=len_summary)

if __name__ == '__main__':
    app.run(debug=True)
