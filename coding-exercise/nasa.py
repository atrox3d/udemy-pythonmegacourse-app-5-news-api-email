import requests
import streamlit as st

API_KEY = 'DEMO_KEY'

url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}Y'

response = requests.get(url)
data = response.json()

title = data['title']
image_url = data['url']
explanation = data['explanation']

st.title(title)
st.image(image=image_url, caption=explanation)

data
