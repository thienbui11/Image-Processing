import streamlit as st
#import lib.common as tools

st.set_page_config(
    page_title="Đồ án cuối kỳ",
    page_icon="🍀",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/847402/pexels-photo-847402.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("");
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


# logo_path = "./VCT.png"
# st.sidebar.image(logo_path, width=200)
st.title ("TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP.HCM")
st.title ("KHOA CÔNG NGHỆ THÔNG TIN")
st.title ("Môn học: Xử lý ảnh số")
st.title ("Báo cáo đồ án cuối kỳ")
st.title (" ")
st.header ("GVHD: ThS. Trần Tiến Đức")
st.header (" Mã lớp : DIPR430685_23_2_03")
st.header ("Học kỳ: 2")
st.header ("Năm học: 2023 - 2024")
st.markdown(
    """
    ## Sản phẩm
    Project cuối kỳ cho môn học xử lý ảnh số DIPR430685 dùng framework Streamlit.

    ### 8 chức năng có trong bài
    - 📙Giải phương trình bậc hai
    - 📔Phát hiện khuôn mặt
    - 📒Nhận dạng đối tượng yolo8
    - 📕Nhận dạng chữ viết tay MNIST
    - 📗Nhận dạng tối thiểu 5 loại đối tượng
    - 📘Xử lý ảnh
    - 📔Nhận dạng số ngón tay trên bàn tay
    - 📕Tăng giảm âm lượng bằng cử chỉ tay
    - 📒Nhận diện lửa
    - 📗Nhận diện dấu tay
    ## Thông tin sinh viên thực hiện
    - 👱Họ tên: Bùi Quang Thiện
    - 🔎MSSV: 21110656
    - 👦Họ tên: Nguyễn Quốc Thịnh
    - 🔎MSSV: 21110662
    """
)


