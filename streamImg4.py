
import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title('Image Processing with OpenCV and Streamlit')

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Convert uploaded file to an image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Convert image to OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    
    # Convert back to PIL Image for Streamlit display
    gray_image_pil = Image.fromarray(gray_image)
    
    st.image(gray_image_pil, caption='Grayscale Image.')
