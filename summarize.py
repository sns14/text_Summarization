import os
import google.generativeai as genai
from config import API_KEY

# Configure the API
genai.configure(api_key=API_KEY)

def summarize_text(text):
    # Define the model and generate the summary
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Summarize the following text:\n\n{text}"
    response = model.generate_content(prompt)
    
    # Access the response content
    summary = response.candidates[0].content.parts[0].text 
    return summary
