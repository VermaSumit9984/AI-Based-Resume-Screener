**AI Based Resume Screener**

An AI-powered Resume Screener Web Application that automatically ranks resumes based on their relevance to a given Job Description (JD) using Natural Language Processing (NLP) and semantic similarity.
This helps recruiters save time by quickly identifying the most suitable candidates.

**🚀 Features**

Upload or paste a Job Description

Upload multiple resumes (PDF, DOCX, image-based resumes)

Extracts text from resumes automatically

Uses AI embeddings to compare resumes with JD

Ranks resumes based on semantic similarity

Simple and clean Flask-based web interface

Ability to change JD and re-rank resumes instantly

**🧠 How It Works (High-Level Flow)**

Job Description Input

User enters or uploads the job description.

Resume Upload

Multiple resumes are uploaded at once.

Text Extraction

PDFs →  pdfplumber, PyMuPDF

DOCX → python-docx

Image-based resumes → pytesseract (OCR)

Embedding & Similarity

Job description and resumes are converted into embeddings.

Cosine similarity is calculated.

Resumes are ranked from most relevant to least relevant.

Results Display

Ranked resumes are shown on the results page.

**🛠️ Tech Stack**
Backend

Python 3.11+

Flask

AI / NLP

Sentence Transformers

HuggingFace Transformers

PyTorch

Cosine Similarity

File Parsing

PDF: pdfplumber, PyMuPDF

DOCX: python-docx

Images: pytesseract, Pillow

Frontend

HTML

Jinja2 Templates

**📁 Project Structure**
ai-based-resume-screening/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (API keys)
│
├── uploads/                # Uploaded resumes
│
├── utils/
│   ├── extractor.py        # Resume text extraction logic
│   └── embedder.py         # Embedding & ranking logic
│
├── templates/
│   ├── index.html          # Job description page
│   ├── upload.html         # Resume upload page
│   └── results.html        # Ranked results page
│
└── README.md

**⚙️ Installation & Setup**

1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-based-resume-screening.git
cd ai-based-resume-screening

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

**Create a .env file:**

GROQ_API_KEY=your_api_key_here


**(Used if integrating LLM-based enhancements later)**

▶️ Run the Application
python app.py


**🔐 Notes & Limitations**

Currently uses in-memory storage (can be upgraded to DB).

OCR accuracy depends on resume image quality.

Designed for screening support, not final hiring decisions.

**🌱 Future Enhancements**

Add authentication (HR login)

Resume skill extraction

Experience & education weighting

Database integration

Downloadable reports (CSV / Excel)

LLM-based resume summarization

**👨‍💻 Author**

    SUmit Verma
ML Developer / Python Developer
