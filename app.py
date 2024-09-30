import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini LLM for chat
def get_gemini_chat_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Function to get response from Gemini LLM for vision
def get_gemini_vision_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input_text:
        response = model.generate_content([input_text, image])
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Gemini Application", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Select Mode", ["Chat", "Vision"])

if app_mode == "Chat":
    # Chat Interface
    st.header("Gemini Chat Application")
    input_text = st.text_input("Input:", key="chat_input")
    submit = st.button("Ask the question")

    if submit:
        response = get_gemini_chat_response(input_text)
        st.subheader("The Response is")
        st.write(response)

elif app_mode == "Vision":
    # Vision Interface
    st.header("Gemini Vision Application")
    input_prompt = st.text_input("Input Prompt:", key="vision_input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    image = None

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.")

    submit = st.button("Tell me about the image")

    if submit and image is not None:
        response = get_gemini_vision_response(input_prompt, image)
        st.subheader("The Response is")
        st.write(response)
