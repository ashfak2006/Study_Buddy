from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name) 

text = "SQL is a computer language that is used for storing, manipulating, and retrieving data in a structured format. This language was invented by IBM. Here SQL stands for Structured Query Language. Interacting databases with SQL queries, we can handle a large amount of data. There are several SQL-supported database servers such as MySQL, PostgreSQL, sqlite3 and so on. Data can be stored in a secured and structured format through these database servers. SQL queries are often used for data manipulation and business insights better"
input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=200, truncation=True)
summary_ids = model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(summary)