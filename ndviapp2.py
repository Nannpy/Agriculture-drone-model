import streamlit as st
import numpy as np
from PIL import Image
import cv2  # Import OpenCV for video processing
import matplotlib.pyplot as plt
import tempfile
import os

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

# ฟังก์ชันสำหรับการประมวลผลวิดีโอ
def process_video(video_path):
    stframe = st.empty()  # สร้างพื้นที่สำหรับแสดงผลวิดีโอ
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # แปลงภาพจาก BGR เป็น RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame_rgb)
        
        # คำนวณ NDVI
        ndvi_frame = calculate_ndvi(frame_pil)
        
        # แสดงผล NDVI
        fig, ax = plt.subplots()
        ax.imshow(ndvi_frame, cmap='RdYlGn')
        ax.set_title("NDVI Frame")
        stframe.pyplot(fig)
        
        # ลบการใช้ cv2.waitKey() เนื่องจาก Streamlit จัดการการแสดงผลอยู่แล้ว

    cap.release()

def main():
    st.title('NDVI Image/Video Converter')
    
    # อัปโหลดภาพหรือวิดีโอ
    uploaded_file = st.file_uploader("Choose an image or video...", type=["jpg", "jpeg", "png", "mp4", "mpeg", "mov"])
    
    if uploaded_file is not None:
        file_type = uploaded_file.type.split('/')[0]
        
        if file_type == 'image':
            # เปิดไฟล์ภาพ
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            
            # คำนวณ NDVI และแสดงผลลัพธ์
            st.write("Calculating NDVI...")
            ndvi_image = calculate_ndvi(image)
            display_ndvi(ndvi_image)
        
        elif file_type == 'video':
            # บันทึกไฟล์วิดีโอที่อัปโหลดลงในไฟล์ชั่วคราว
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            
            # ประมวลผลวิดีโอและแสดงผล NDVI สำหรับแต่ละเฟรม
            st.write("Processing video and calculating NDVI for each frame...")
            process_video(tfile.name)

if __name__ == "__main__":
    main()
