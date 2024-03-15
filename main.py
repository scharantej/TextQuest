
# main.py
from flask import Flask, render_template, request, redirect, url_for
import PyPDF2
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdf_reader', methods=['POST'])
def pdf_reader():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page in range(pdf_reader.numPages):
            page_object = pdf_reader.getPage(page)
            text += page_object.extractText()

        return render_template('pdf_reader.html', text=text)

@app.route('/question_answering', methods=['POST'])
def question_answering():
    if request.method == 'POST':
        text = request.form['text']
        question = request.form['question']
        nlp = pipeline("question-answering")
        result = nlp(question=question, context=text)
        return render_template('results.html', question=question, answer=result['answer'])

if __name__ == '__main__':
    app.run(debug=True)
