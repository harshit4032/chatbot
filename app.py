import streamlit as st
import os
from utils.transcribe_w_whisper import transcribe_audio
from utils.get_llm_response import (
    get_openai_llm_response,
    get_groq_llm_response,
    get_gemini_llm_response,
)
from utils.get_tts_response import generate_speech

# File path for storing uploaded audio
upload_audio_path = "audio/uploaded_audio.wav"
tts_audio_file_path = "audio/answer.mp3"

# Streamlit app layout
st.title("Multi-Input Chatbot (Text & Audio)")

# Sidebar for model selection
st.sidebar.title("Choose a Model:")
model_choice = st.sidebar.radio(
    "Select the LLM model:",
    ("OpenAI GPT-3.5-turbo", "Deepseek-r1-distill-llama-70b", "Gemini Pro 1.5")
)

# Function to get the LLM response based on model choice
def get_llm_response(user_text, model_choice):
    if model_choice == "OpenAI GPT-3.5-turbo":
        return get_openai_llm_response(user_text)
    elif model_choice == "Deepseek-r1-distill-llama-70b":
        return get_groq_llm_response(user_text)
    elif model_choice == "Gemini Pro 1.5":
        return get_gemini_llm_response(user_text)

# User input: text or audio upload
user_text = st.text_input("Enter your question:")
uploaded_audio = st.file_uploader("Or upload an audio file:", type=["wav", "mp3"])

# Process input
if st.button("Ask Question"):
    final_input_text = None

    if user_text:  # Text input takes priority
        final_input_text = user_text
        st.markdown(
            f'<div style="background-color:#e0f7fa;padding:10px;border-radius:5px;">'
            f'<strong>👤 You:</strong> {user_text}</div>',
            unsafe_allow_html=True
        )

    elif uploaded_audio:  # Process uploaded audio
        with st.spinner("Processing audio file..."):
            with open(upload_audio_path, "wb") as f:
                f.write(uploaded_audio.read())
            final_input_text = transcribe_audio(upload_audio_path)

        st.markdown(
            f'<div style="background-color:#e0f7fa;padding:10px;border-radius:5px;">'
            f'<strong>🎙️ You (Transcribed):</strong> {final_input_text}</div>',
            unsafe_allow_html=True
        )

    if final_input_text:
        # GET LLM RESPONSE
        with st.spinner(f'Getting response with {model_choice}...'):
            llm_response = get_llm_response(final_input_text, model_choice)

        st.markdown(
            f'<div style="background-color:#ffe0e0;padding:10px;border-radius:5px;margin:1rem 0rem;">'
            f'<strong>🤖 AI:</strong> {llm_response}</div>',
            unsafe_allow_html=True
        )

        # Convert text response to speech
        with st.spinner("Generating speech..."):
            generate_speech(llm_response, tts_audio_file_path)

        st.audio(tts_audio_file_path, format="audio/mp3", autoplay=True)
    else:
        st.warning("Please enter text or upload an audio file.")

