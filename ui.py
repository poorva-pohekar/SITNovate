from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Dummy function to simulate summarization
def summarize_document(text, method):
    if method == 'extractive':
        return "This is an extractive summary of the document."
    else:
        return "This is an abstractive summary of the document."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        method = request.form['summary_type']
        
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            
            summary = summarize_document(text, method)
            return render_template('index.html', summary=summary)
    
    return render_template('index.html', summary=None)

if __name__ == '__main__':
    app.run(debug=False)

