import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyCqxpCtMJE5xG-L3pClDHn6fNvLF-VlBs4"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("List 5 planets each with an interesting fact")
print(response.text)

response = model.generate_content("what are top 5 frequently used emojis?")
print(response.text)