import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update as needed

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

def extract_text_from_pdf(pdf_path):
    text = ""
    images = convert_from_path(pdf_path, dpi=300,poppler_path=r'C:\\poppler-24.08.0\\Library\\bin')
    for img in images:
        text += pytesseract.image_to_string(img)
        text += "\n"
    return text.strip()

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']:
        return extract_text_from_image(file_path)
    elif ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file type."