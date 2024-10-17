import streamlit as st

from PIL import Image
def main():
    # Set the title of the app

    st.title("Welcome to the Churn App")
    image = Image.open('telecom.jpeg')

# Display the image in Streamlit
    st.image(image, use_column_width=True)

