import streamlit as st   
import cv2
from PIL import Image  # Streamlit's file uploader returns the uploaded file as a binary stream, which PIL can open and process
import numpy as np    # OpenCV processes images as NumPy arrays. To apply OpenCV functions on an image, you need to convert it from the PIL format to a NumPy array.



# Title of the app
st.title('OpenCV and Streamlit')

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    # Convert uploaded file to an image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)   #streamlit takes RGB by default
    
    # Convert image to OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)    #opencv takes BGR befault
    

   # image_cv = cv2.imread(r'C:\Users\Vasu Jain\Desktop\web\project\myenv\project3\Nikon-D750-Image-Samples-2.jpg')
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('MyWindow',image_cv)
    # Display image using OpenCV functions (optional, for processing)
   # gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    st.image(image_cv, caption='Grayscale Image.', use_column_width=True, channels="GRAY")

    st.image(image_cv, caption='Processed Image.')
    image_cv_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)  #to remove color difference in both
    st.image(image_cv_rgb, caption='Processed Image.')

    



