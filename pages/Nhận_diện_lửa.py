import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
st.set_page_config(page_title="Nhận diện lửa")

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
st.markdown(page_bg_img,unsafe_allow_html=True)

st.title('Nhận diện lửa')
# FRAME_WINDOW = st.imakge([])


MODEL_PATH = "./model/fire_model.h5"
fire_detector = cv2.CascadeClassifier('./model/fire_cascade.xml')

# Tải mô hình .h5
model = load_model(MODEL_PATH, compile=False)

class_name = ['FIRE', 'NON-FIRE']

# Hàm tiền xử lý đầu vào để phù hợp với mô hình
def preprocess_input(image):
    image = cv2.resize(image, (28, 28))
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)
    return image

cam = cv2.VideoCapture(0)
while True:
    is_connect, im = cam.read()
    if is_connect:
        grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        fires = fire_detector.detectMultiScale(grey, 1.3, 5)
        for x, y, w, h in fires:
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi = im[y+3:y+h-3, x+3:x+w-3]

            # Tiền xử lý dữ liệu đầu vào
            input_data = preprocess_input(roi)

            # Dự đoán với mô hình .h5
            predictions = model.predict(input_data)
            result = np.argmax(predictions)

            # Hiển thị nhãn dự đoán lên hình ảnh
            cv2.putText(im, class_name[result], (x+15, y-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 2)
            
            if class_name[result] == 'FIRE':
                print("FIRE")
                pass
            else:
                print("NON FIRE")
                pass

        cv2.imshow('FRAME', im)
    else:
        print("Cannot read camera.")
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
