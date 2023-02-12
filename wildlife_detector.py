import streamlit as st
import time
import pandas as pd
import numpy as np
import cv2 as cv
import cvlib
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
import csv
chart_data = pd.read_csv("raw_data.csv")
count = pd.read_csv("count.csv")

st.title("Wildlife Detector")
if 'wildlife_detector' not in st.session_state:
    st.session_state['wildlife_detector'] = 0
list_of_wildlife = ['person', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']
def picture_process(img_file):
    count =+ 1
    with open ("temp.png","wb") as f:
        f.write(img_file.getbuffer())
    
    img = cv.imread("temp.png")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    bbox, label, conf = cvlib.detect_common_objects(img)
    
    for i in range(len(label)):
        if label[i] not in list_of_wildlife:
            bbox.pop(i)
            label.pop(i)
            conf.pop(i)
    output_image = draw_bbox(img, bbox, label, conf)
    st.session_state.wildlife_detector = len(label)
    return output_image
file_upload = st.file_uploader("Upload a file", type = ['png'])
if file_upload:
    with open ("picture.jpg","wb") as f:
        f.write(file_upload.getbuffer())
    img = cv.imread("picture.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    bbox, label, conf = cvlib.detect_common_objects(img)
    for i in range(len(label)):
        if label[i] not in list_of_wildlife:
            bbox.pop(i)
            label.pop(i)
            conf.pop(i)
    output_image = draw_bbox(img, bbox, label, conf)
    st.image(output_image)
    st.session_state.wildlife_detector = len(label)
picture = st.camera_input('Webcam')
if picture:
    st.image(picture_process(picture))
st.sidebar.write('number of wildlife detected', st.session_state.wildlife_detector)
chart_data.iloc[count.iloc[0].iloc[0]].iloc[1] = st.session_state.wildlife_detector
st.sidebar.line_chart.pd.DataFrame([chart_data.iloc[0].iloc[1:],chart_data.iloc[1].iloc[1:]],columns=[chart_data.iloc[0].iloc[0],chart_data.iloc[1],chart_data.iloc[0]])

# .streamlit/secrets.toml

public_gsheets_url = "https://docs.google.com/spreadsheets/d/1XlMC0ZBxMOoV4ippzbLLDFG31v-nqmz_cWa5akj8kz0/edit?usp=sharing"