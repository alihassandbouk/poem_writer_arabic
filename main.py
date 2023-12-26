import streamlit as st
from helper import Palm_request

st.title("شعر على السريع: ")
st.markdown('''# اكتب اي شعر على السريع 

            ''')
types = ["رثاء","مدح","هجاء","غزل عذري"]
type = st.selectbox("نوع الشعر",types)
name = st.text_input("اسم الشخص الذي تريد القصيدة عنه")
context = st.text_input(label="اكتب صفتين عن الشخص المستهدف:")
generate = st.button("اكتب:")

if generate and name and context and types:
    result = Palm_request(name=name,type=type,con=context)
    st.markdown(result)
