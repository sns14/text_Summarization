import google.generativeai as genai
import os

# Configure the API
genai.configure(api_key=os.getenv('GEMINI_API_KEY')) 

def summarize_text(text):
    # Define the model and generate the summary
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Summarize the given text:\n\n{text}"
    response = model.generate_content(prompt)
    print(response)
    
    # Access the response content
    summary = response.candidates[0].content.parts[0].text 
    return summary
