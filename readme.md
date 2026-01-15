# 📘 Study Buddy

Study Buddy is a platform developed during my **ASAP AI/ML Internship**.  
It helps students make learning easier by allowing them to upload their notes (PDF or text) and automatically generate:

- ✨ Summaries  
- 📌 Key Points  
- ❓ Q&A for practice  

This project leverages **Python**, **T5-small** for summarization, **Gemini API** for student-friendly outputs, and **Streamlit** for an interactive frontend.

---

## 🚀 Features
- Upload notes in **PDF** or **Text** format.  
- Generate concise **summaries** using the T5-small model.  
- Convert summaries into **student-friendly formats** (simplified summaries, key points, Q&A) via Gemini API.  
- Interactive **Streamlit frontend** for easy use by students.  

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Model**: T5-small (Text Summarization)  
- **API**: Gemini API (for enhanced summaries, key points, and Q&A generation)  
- **Frontend**: Streamlit (for user interface)  
- **Frameworks/Libraries**:  
  - PyTorch / Transformers (for T5 model)  
  - Streamlit (UI)  
  - PDF/Text parsing libraries  

---

## ⚙️ Workflow
1. **Upload Notes** → Students upload notes in PDF or text format via Streamlit.  
2. **Summarization** → T5-small model generates a concise summary.  
3. **Enhancement** → Gemini API converts the summary into:  
   - Student-friendly summary  
   - Key points  
   - Q&A for revision  
4. **Output** → Results are displayed in the Streamlit app.  

---

## 🔧 Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/study-buddy.git
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Run the app:
    ```bash
    streamlit run main.py



- Upload notes and start summarizing!

## 📈 Future Improvements
- Add support for multi-language summarization.
- Enhance Q&A generation with difficulty levels.
- Deploy as a cloud-hosted web app for wider accessibility.

## 🙌 Acknowledgements
- Developed as part of ASAP AI/ML Internship.
- Inspired by the need to make studying more efficient and interactive.
- Thanks to T5-small, Gemini API, and Streamlit for powering the summarization and enhancement pipeline.

## 📜 License
This project is licensed under the MIT License. Feel free to use and improve it!

---
