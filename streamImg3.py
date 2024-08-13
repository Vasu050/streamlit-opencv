import streamlit as st
from PIL import Image

# Title of the app
st.title('Image and Column Example')

# Create columns
col1, col2 = st.columns(2)

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Convert uploaded file to an image
    image = Image.open(uploaded_file)
    
    # Display the image in the first column
    with col1:
        st.image(image, caption='Image in Column 1', use_column_width=True)
    
    # Display a different text in the second column
    with col2:
        st.write("This is Column 2. The image is in Column 1.")
