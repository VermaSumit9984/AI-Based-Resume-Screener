import os
from flask import Flask, render_template, request, redirect, url_for
from utils.extractor import extract_text_from_file
from utils.embedder import rank_resumes

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global storage for temporary data (can use DB later)
JOB_DESCRIPTION = ""
RESUME_DATA = []  # [(filename, text), ...]

@app.route('/')
def home():
    """Home page to upload or enter Job Description"""
    return render_template('index.html')

@app.route('/upload_jd', methods=['POST'])
def upload_jd():
    """Handle JD upload and redirect to resume upload page"""
    global JOB_DESCRIPTION
    JOB_DESCRIPTION = request.form['job_description']
    return redirect(url_for('upload_resumes'))

@app.route('/upload_resumes')
def upload_resumes():
    """Render resume upload page"""
    return render_template('upload.html')

@app.route('/upload_resumes', methods=['POST'])
def handle_resumes():
    """Handle multiple resume uploads"""
    global RESUME_DATA
    files = request.files.getlist('resumes')
    RESUME_DATA = []

    for file in files:
        if not file.filename:
            continue
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        text = extract_text_from_file(filepath)
        RESUME_DATA.append((file.filename, text))

    return redirect(url_for('results'))

@app.route('/results')
def results():
    """Rank resumes by similarity to JD"""
    global JOB_DESCRIPTION, RESUME_DATA
    if not JOB_DESCRIPTION or not RESUME_DATA:
        return redirect(url_for('home'))
    ranked = rank_resumes(JOB_DESCRIPTION, RESUME_DATA)
    return render_template('results.html', results=ranked, jd=JOB_DESCRIPTION)

@app.route('/change_jd', methods=['POST'])
def change_jd():
    """Allow user to change JD and re-run ranking"""
    global JOB_DESCRIPTION
    JOB_DESCRIPTION = request.form['new_job_description']
    return redirect(url_for('results'))

if __name__ == '__main__':
    app.run(debug=True)
