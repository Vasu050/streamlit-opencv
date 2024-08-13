import streamlit as st
from PIL import Image

# Title of the app
st.title('Image Fit Example')

# Upload image file
uploaded_file = st.file_uploader(r"C:\Users\Vasu Jain\Desktop\web\project\myenv\project3\Nikon-D750-Image-Samples-2.jpg",type="jpg")

if uploaded_file is not None:
    # Convert uploaded file to an image
    image = Image.open(uploaded_file)
    
    # Display the image, fitting it to the column width
    st.image(image, caption='Fixed Size Image', use_column_width=True)



