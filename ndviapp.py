import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import tempfile

# ฟังก์ชันสำหรับคำนวณ NDVI
def calculate_ndvi(image):
    image = np.array(image)
    red = image[:, :, 0].astype(float)
    nir = image[:, :, 1].astype(float)
    ndvi = (nir - red) / (nir + red)
    return ndvi

# ฟังก์ชันแสดงภาพ NDVI ด้วย Matplotlib
def display_ndvi(ndvi):
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar()
    plt.title('NDVI')
    st.pyplot(plt.gcf())  # ใช้ st.pyplot เพื่อแสดงภาพใน Streamlit

def main():
    st.title('NDVI Image Converter')
    
    # อัปโหลดภาพ
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png",'mp4','mpeg','mov'])
    
    if uploaded_file is not None:
        # เปิดไฟล์ภาพ
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # คำนวณ NDVI และแสดงผลลัพธ์
        st.write("Calculating NDVI...")
        ndvi_image = calculate_ndvi(image)
        display_ndvi(ndvi_image)

if __name__ == "__main__":
    main()
