import google.generativeai as genai
import PIL.Image
img = PIL.Image.open('image.jpg')


genai.configure(api_key='AIzaSyCbrGlCX60mFMpwmmB_jYJGZs7M21PpTj4')


model = genai.GenerativeModel('gemini-pro-vision')

response1 = model.generate_content(["what is the answer", img])

print(response1.text)