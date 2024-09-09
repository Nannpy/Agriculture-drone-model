import streamlit as st
import numpy as np
from PIL import Image
import cv2
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

# ฟังก์ชันสำหรับประมวลผลวิดีโอ
def process_video(video_file):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    vid_cap = cv2.VideoCapture(tfile.name)
    frames = []
    
    while vid_cap.isOpened():
        ret, frame = vid_cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        ndvi_frame = calculate_ndvi(frame)
        frames.append(ndvi_frame)
    
    vid_cap.release()
    return frames

# ฟังก์ชันแสดง NDVI จากวิดีโอ
def display_video(frames):
    for frame in frames:
        plt.imshow(frame, cmap='RdYlGn')
        plt.colorbar()
        plt.title('NDVI Frame')
        st.pyplot(plt.gcf())

def main():
    st.title('NDVI Image and Video Converter')
    
    # สร้าง Sidebar สำหรับเลือกประเภทข้อมูล
    option = st.sidebar.selectbox('Select Data Type', ('Image', 'Video'))
    
    if option == 'Image':
        st.subheader('Upload an image to convert to NDVI')
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            # เปิดไฟล์ภาพ
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            
            # คำนวณ NDVI และแสดงผลลัพธ์
            st.write("Calculating NDVI...")
            ndvi_image = calculate_ndvi(image)
            display_ndvi(ndvi_image)
    
    elif option == 'Video':
        st.subheader('Upload a video to convert to NDVI')
        uploaded_video = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi"])
        
        if uploaded_video is not None:
            # ประมวลผลวิดีโอ
            st.video(uploaded_video)
            st.write("Processing video frames to NDVI...")
            frames = process_video(uploaded_video)
            display_video(frames)

if __name__ == "__main__":
    main()
