import streamlit as st
from dotenv import load_dotenv
from summurisation import TextSummarizer
from pdfExtracture import PDFProcessor
from PIL import Image
import os
from google import genai

load_dotenv()
# --- Page Configuration ---
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
file_path=""
def generate_QA(text):
    print("generating Q&A")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents =  f"You are AI, a expert in transforming documents into effective study materials. Create high-quality study Q&A from the following text{text}",

    )
    return response.text
def generate_summary(text):
    print("generating summary")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents =  f"You are AI , a expert in transforming documents into effective study materials. Your purpose is to create comprehensive summaries. Create high-quality study summary from the following text{text}",

    )
    return response.text
def generate_keypoints(text):
    print("generating keypoints")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents =  f"You are AI study buddy,generate quality keypoints from the following text{text}",

    )
    return response.text
st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="wide")
text=""
# --- Initialize Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "study_mode" not in st.session_state:
    st.session_state.study_mode = "Summarize"
if "summury" not in st.session_state:
    st.session_state.summury = ""
if "QA" not in st.session_state:
    st.session_state.QA = ""
if "keypoints" not in st.session_state:
    st.session_state.keypoints = ""

# --- Sidebar: Uploads & Controls ---
with st.sidebar:
    st.title("📂 Study Materials")
    
    # 1. File Uploaders
    uploaded_pdf = st.file_uploader("Upload Study PDF", type="pdf")
    # uploaded_img = st.file_uploader("Upload Notes (Image)", type=["png", "jpg", "jpeg"])

    if uploaded_pdf:
        st.write(f"Uploaded PDF: {uploaded_pdf.name}")
        os.mkdir("tempDir", exist_ok=True)
        file_path = os.path.join("tempDir", uploaded_pdf.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_pdf.read())

      
        text=PDFProcessor().extract_text_pypdf2(pdf_path=file_path)
        st.session_state.summury=TextSummarizer().summarize_text(text)
        
    # if uploaded_img:
    #     st.image(uploaded_img, caption="Uploaded Note", use_container_width=True)
    #     file_path = os.path.join("tempDir", uploaded_img.name)
    #     with open(file_path, "wb") as f:
    #         f.write(uploaded_img.read())    
    #     text=PDFProcessor().extract_text_image(image_path=file_path)
    #     print("extracted text from image",text)
    #     st.session_state.summury=TextSummarizer().summarize_text(text)

    st.divider()
    
    # 2. Mode Selection
    st.subheader("Choose Action")
    st.session_state.study_mode = st.radio(
        "What should the bot do?",
        ["Summarize", "General Q&A", "keypoints"]
    )
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.summury=""
        st.session_state.QA=""
        st.session_state.flashcards=""
        if os.path.exists(file_path):
            os.remove(file_path)
        st.rerun()

# --- Main Chat UI ---
st.title("🤖 AI Study Companion")
st.caption(f"Current Mode: **{st.session_state.study_mode}**")
with st.chat_message("assistant"):
    st.markdown("Hello! I'm your AI Study Companion. Upload your study materials and choose an action from the sidebar to get started.")
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if uploaded_pdf or text:
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # Logic Switcher (Placeholders for your LLM integration)
        if st.session_state.study_mode == "Summarize":
            # response_placeholder.markdown("here is the summurised version of your study material")
            st.session_state.summury=generate_summary(st.session_state.summury)
            response_placeholder.write(st.session_state.summury)
            full_response=st.session_state.summury
            
        elif st.session_state.study_mode == "General Q&A":
            st.session_state.QA = generate_QA(st.session_state.summury)
            response_placeholder.markdown(st.session_state.QA)
            full_response=st.session_state.QA   
        else:
            st.session_state.keypoints = generate_keypoints(st.session_state.summury)
            response_placeholder.markdown(st.session_state.keypoints)
            full_response=st.session_state.keypoints

        st.session_state.messages.append({"role": "assistant", "content": full_response})
    

# --- Chat Logic ---
if prompt := st.chat_input("paste or upload the text to transform into a high-quality study materials"):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.summury=TextSummarizer().summarize_text(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot logic based on mode
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # Logic Switcher (Placeholders for your LLM integration)
        if st.session_state.study_mode == "Summarize":
            print("summarize mode")

            full_response = generate_summary(st.session_state.summury)
        elif st.session_state.study_mode == "General Q&A":
            full_response = generate_QA(st.session_state.summury)
        else:
            full_response = generate_keypoints(st.session_state.summury)
        response_placeholder.write(full_response)
        print(full_response,"full response")
        st.session_state.messages.append({"role": "assistant", "content": full_response})