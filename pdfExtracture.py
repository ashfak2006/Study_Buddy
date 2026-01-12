import os
import io
import PyPDF2
import pdf2image
import pytesseract
from PIL import Image
import streamlit as st

class PDFProcessor:
    def __init__(self):
        pass
    
    def extract_text_pypdf2(self, pdf_path):
        """Extract text using PyPDF2"""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            st.error(f"PyPDF2 extraction error: {e}")
        return text
    
    def extract_text_with_ocr(self, pdf_path):
        
        """Extract text using OCR (for scanned PDFs)"""
        text = ""
        try:
            # Convert PDF to images
            images = pdf2image.convert_from_path(pdf_path)
            
            # Process each image with OCR
            for i, image in enumerate(images):
                # Convert PIL Image to bytes
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()
                
                # Perform OCR
                page_text = pytesseract.image_to_string(Image.open(io.BytesIO(img_byte_arr)))
                text += f"Page {i+1}:\n{page_text}\n\n"
                
        except Exception as e:
            st.error(f"OCR extraction error: {e}")
        return text
    
    def extract_text_image(self, image_path):
        """Extract text from an image using OCR"""
        text = ""
        try:
            image = Image.open(image_path)
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            text = pytesseract.image_to_string(Image.open(io.BytesIO(img_byte_arr)))
        except Exception as e:
            st.error(f"Image OCR extraction error: {e}")
        return text

    def extract_metadata(self, pdf_path):
        """Extract PDF metadata"""
        metadata = {}
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                metadata = {
                    'pages': len(reader.pages),
                    'title': reader.metadata.get('/Title', 'Unknown'),
                    'author': reader.metadata.get('/Author', 'Unknown'),
                    'created': reader.metadata.get('/CreationDate', 'Unknown'),
                    'file_size': f"{os.path.getsize(pdf_path) / 1024:.2f} KB"
                }
        except:
            metadata = {'pages': 'Unknown', 'title': 'Unknown', 'author': 'Unknown'}
        return metadata