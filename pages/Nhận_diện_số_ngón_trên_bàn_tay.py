import streamlit as st
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time
st.set_page_config(page_title="Đếm số ngón tay trên bàn tay", page_icon="🖐️")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
[data-testid="stSidebar"] > div:first-child {
    background : #262730;
    background-position: center;
}
</style>
"""
st.title('Đếm số ngón tay')

def process_frame(img, detector, classifier, labels, offset=20, imgSize=300):
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        for hand in hands:
            x, y, w, h = hand['bbox']

            # Ensure that the region to be cropped is within bounds
            if 0 <= y - offset < img.shape[0] and 0 <= x - offset < img.shape[1] and y + h + offset < img.shape[0] and x + w + offset < img.shape[1]:
                imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

                dimension = h if h > w else w
                k = imgSize / dimension

                if h > w:
                    wCal = math.ceil(k * w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    wGap = math.ceil((imgSize - wCal) / 2)
                    imgWhite[:, wGap:wCal + wGap] = imgResize
                else:
                    hCal = math.ceil(k * h)
                    imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                    hGap = math.ceil((imgSize - hCal) / 2)
                    imgWhite[hGap:hCal + hGap, :] = imgResize

                prediction, index = classifier.getPrediction(imgWhite, draw=False)

                # Ensure that the index is within the valid range of labels
                if 0 <= index < len(labels):
                    rect_color = (255, 0, 255)
                    cv2.rectangle(imgOutput, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50), rect_color, cv2.FILLED)
                    cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
                    cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), rect_color, 4)

    return imgOutput

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# local_css("./pages/css/style.css")

def main():

    FRAME_WINDOW = st.image([])

    VIDEO_PATH = 0  # Set to the appropriate vikdeo path if not using the default camera
    MODEL_PATH = "./model/finger_counting_model.h5"
    LABELS_PATH = "./model/labels.txt"

    cap = cv2.VideoCapture(VIDEO_PATH)
    detector = HandDetector(maxHands=2)
    classifier = Classifier(MODEL_PATH, LABELS_PATH)

    offset = 20
    imgSize = 300
    labels = ["One", "Two", "Three", "Four", "Five"]
    start_button = st.button("Start Recognition")

    if start_button:
        while cap.isOpened():
            success, img = cap.read()
            if not success:
                break

            img_output = process_frame(img, detector, classifier, labels, offset=offset, imgSize=imgSize)
            FRAME_WINDOW.image(img_output, channels="BGR", use_column_width=True)

            # Introduce a delay to control frame rate
            time.sleep(0.05)  # Adjust the sleep duration as needed

    # Release resources
    cap.release()

if __name__ == "__main__":
    main()