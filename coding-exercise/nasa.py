import requests
import streamlit as st
from pathlib import Path

API_KEY = 'DEMO_KEY'

url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'

response = requests.get(url)
data = response.json()

title = data['title']
image_url = data['url']
explanation = data['explanation']

download_path = Path('downloads/')
image_filename = Path(image_url).name
image_path = download_path.joinpath(image_filename)
response = requests.get(image_url)
with open(image_path, 'wb') as file:
    file.write(response.content)

st.title(title)
st.image(image=str(image_path))
st.write(explanation)

data
