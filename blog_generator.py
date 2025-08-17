#pip install python-dotenv

import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "compound-beta-mini"

def generate_text(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        resp_json = response.json()
        
        if "results" in resp_json:
            return resp_json["results"][0].get("output_text", "")
        elif "choices" in resp_json:
            return resp_json["choices"][0]["message"]["content"]
        else:
            print("Unexpected response format:", resp_json)
            return None
    else:
        print("Error:", response.status_code, response.text)
        return None

# Example Usage
blog_prompt = "Write a blog post about benefits of AI in healthcare, 200 words."
blog_content = generate_text(blog_prompt)
print("=== Blog Output ===")
print(blog_content)

