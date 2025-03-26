from openai import OpenAI
import os
# from decouple import config
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
openai_api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI()

def transcribe_audio(file_path):
    # Open the audio file in binary mode
    with open(file_path, "rb") as audio_file:
        # Create the transcription using OpenAI's Whisper model
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text",
            language="en"  # Force transcription in English
        )
    return transcription
