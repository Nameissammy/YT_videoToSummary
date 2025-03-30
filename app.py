from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


# function to get youtube video id
def get_video_id(url):
    return url.split("watch?v=")[-1]


st.title("YT Video to Summary")
url = st.text_input("Enter YT video Link")

video_id = get_video_id(url)

if st.button("Summaries"):
    # getting transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # concating all text into a single string
    transcript_joined = " ".join([line["text"] for line in transcript])

    prompt = f"You are a summarizer who summarises youtube video content. This is the content: {transcript_joined}"

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    # client = genai.Client(api_key = api_key)
    # response = client.models.generate_content(
    #     model = "gemini-2.0-flash",
    #     contents = prompt
    # )
    response.text
