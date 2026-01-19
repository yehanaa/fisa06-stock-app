# Import convention
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# .env에 있는 환경
my_name = os.getenv('MY_NAME')
st.header(my_name)

# 출력 메서드
st.text('Tushar-Aggarwal.com') # 화면에 출력 또는 입력을 받으려면 st.어쩌구()를 거쳐야 함
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''') # 수식을 출력하는 문법
st.write('Supreme Applcations by Tushar Aggarwal') # 알아서 안에 있는 내용을 변환
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')


# * optional kwarg unsafe_allow_html = True
hello = 1
# streamlit run 파일명.py
st.text('hello')

# 입력 메서드
st.button('Demo')

import pandas as pd
df = pd.DataFrame({'key' : [1, 2, 3]})
st.data_editor('Edit DF', df)
st.checkbox('Option 1')
st.radio('Pick Country:', ['France','Germany'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter Article')
st.number_input('Enter required number')
st.text_area('Entered article text')
st.date_input('Select date')
st.time_input('Select Time')
st.file_uploader('File CSV uploader')
st.download_button('Download Source data', data)
st.camera_input('Click a Snap')
st.color_picker('Pick a color')