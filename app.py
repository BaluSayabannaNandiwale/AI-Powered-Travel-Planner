import streamlit as st
from langchain import LangChain
import requests
import os

# Set up Google GenAI API key
GOOGLE_GENAI_API_KEY = os.getenv('GOOGLE_GENAI_API_KEY')

# Initialize LangChain
langchain = LangChain()

# Define the function to get travel options
def get_travel_options(source, destination):
    # Placeholder for LangChain and Google GenAI integration
    response = requests.post(
        'https://genai.googleapis.com/v1/models/text-davinci-003:generateText',
        headers={'Authorization': f'Bearer {GOOGLE_GENAI_API_KEY}'},
        json={
            'prompt': f'Provide travel options from {source} to {destination} including cab, train, bus, and flights with estimated costs.',
            'max_tokens': 150
        }
    )
    travel_options = response.json()
    return travel_options

# Streamlit UI
st.set_page_config(page_title='AI-Powered Travel Planner', page_icon='✈️')
st.title('AI-Powered Travel Planner')

st.markdown("""
<style>
    body {
        background-color: #f0f2f6;
        font-family: Arial, sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1 {
        color: #333333;
        text-align: center;
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin: 0.5em 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    button {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
    .error {
        color: red;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

source = st.text_input('Enter source location')
destination = st.text_input('Enter destination location')

if st.button('Get Travel Options'):
    if source and destination:
        with st.spinner('Fetching travel options...'):
            travel_options = get_travel_options(source, destination)
        st.success('Travel options fetched successfully!')
        st.json(travel_options)
    else:
        st.error('Please enter both source and destination locations')
