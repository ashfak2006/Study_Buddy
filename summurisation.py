from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
from pdfExtracture import PDFProcessor
import re
import nltk
from semantic_chunking import semantic_chunk
class TextSummarizer:
    def __init__(self, model_name="t5-small"):
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        nltk.download('punkt') 


    def summarize_text(self,text):
        text = self.preprocess_text(text)
        sentences = nltk.sent_tokenize(text)
        chucnks = semantic_chunk(sentences, threshold=0.75)  
        summaries = []
        if not sentences:
            return "" 
        for chunk in chucnks:
            input_ids = self.tokenizer.encode("summarize: " + chunk, return_tensors="pt", max_length=600, truncation=True)
            summary_ids = self.model.generate(input_ids, max_length=600, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            summaries.append(summary)

        final_summary = " ".join(summaries)
        return final_summary

    def preprocess_text(self,text):
        text = re.sub(r'\s+', ' ', text)
        text = text.replace("/n","")
        text = text.strip()

        return text