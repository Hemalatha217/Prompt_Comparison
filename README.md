# Prompt_Comparison

# Gemini AI Prompting Techniques

## Project Overview

Gemini AI Prompting Techniques is a Streamlit-based web application that demonstrates different prompting techniques using Google's Gemini Large Language Model (LLM). Users can select a prompting technique, enter a task, and generate AI-powered responses.

## Features

- Interactive Streamlit interface
- Multiple prompting techniques
- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Chain-of-Thought prompting
- Custom prompt input
- AI-generated responses using Gemini
- Secure API key management

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK

## Project Structure

    Prompt_Comparison/
    ├── app.py
    ├── llm.py
    ├── prompt_templates.py
    ├── requirements.txt
    └── README.md

## Installation

Clone the repository:

    git clone https://github.com/Hemalatha217/Prompt_Comparison.git

Navigate to the project directory:

    cd Prompt_Comparison

Install the dependencies:

    pip install -r requirements.txt

## API Key Configuration

1. Create a Gemini API key at https://aistudio.google.com/apikey
2. Open your application in Streamlit Community Cloud.
3. Navigate to the app settings and open Secrets.
4. Add the following configuration:

    GEMINI_API_KEY = "your_gemini_api_key"

Never upload your API key to GitHub.

## Run Locally

Start the Streamlit application:

    streamlit run app.py

## Deployment

1. Push the project files to GitHub.
2. Open https://share.streamlit.io/
3. Create a new Streamlit application.
4. Select the Prompt_Comparison repository.
5. Set `app.py` as the main file.
6. Add your Gemini API key under Secrets.
7. Deploy the application.

## Expected Output

Users can choose a prompting technique, enter a task, and view the generated prompt and Gemini AI response.

## Conclusion

This project demonstrates how different prompt engineering techniques can improve interactions with Google's Gemini AI through an interactive Streamlit application.
