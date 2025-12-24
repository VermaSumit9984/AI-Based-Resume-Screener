import pdfplumber
import pytesseract
from PIL import Image
import fitz  # PyMuPDF for OCR fallback
import docx

def extract_text_from_file(file_path):
    """Detect and extract text from PDF or DOCX."""
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        return ""

def extract_text_from_pdf(file_path):
    """Extract text from PDF, with OCR fallback."""
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
        if len(text.strip()) == 0:
            # OCR fallback
            pdf = fitz.open(file_path)
            for page in pdf:
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text += pytesseract.image_to_string(img)
    except Exception as e:
        print(f"[ERROR] PDF extraction failed: {e}")
    return text

def extract_text_from_docx(file_path):
    """Extract text from Word documents."""
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"[ERROR] DOCX extraction failed: {e}")
    return text
