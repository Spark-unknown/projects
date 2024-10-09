import streamlit as st
import hashlib
import time

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        # Create a unique hash by appending the current time
        unique_string = original_url + str(time.time())
        url_hash = hashlib.md5(unique_string.encode()).hexdigest()[:6]
        short_url = f"http://short.url/{url_hash}"
        self.url_mapping[short_url] = original_url
        return short_url

    def get_original_url(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")

# Create an instance of the URLShortener class
url_shortener = URLShortener()

# Streamlit app layout
st.title("URL Shortener")
original_url = st.text_input("Enter the URL to shorten")

if st.button("Shorten"):
    if original_url:
        short_url = url_shortener.shorten_url(original_url)
        st.success(f"Shortened URL: {short_url}")
    else:
        st.error("Please enter a URL to shorten.")

short_url_input = st.text_input("Enter the shortened URL to retrieve the original")

if st.button("Get Original URL"):
    original_url_result = url_shortener.get_original_url(short_url_input)
    st.write(original_url_result)
