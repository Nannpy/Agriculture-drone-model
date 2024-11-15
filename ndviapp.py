import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import tempfile

def calculate_ndvi(image):
    image = np.array(image)
    red = image[:, :, 0].astype(float)
    nir = image[:, :, 1].astype(float)
    ndvi = (nir - red) / (nir + red)
    return ndvi

def display_ndvi(ndvi):
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar()
    plt.title('NDVI')
    st.pyplot(plt.gcf()) 

def main():
    st.title('NDVI Image Converter')
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png",'mp4','mpeg','mov'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        st.write("Calculating NDVI...")
        ndvi_image = calculate_ndvi(image)
        display_ndvi(ndvi_image)

if __name__ == "__main__":
    main()
