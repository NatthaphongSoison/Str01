import streamlit as st

st.header("Natthaphong Soison")
st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('ณัฐพงษ์ สร้อยสน ')
st.subheader('สาขาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/12.jpg')
with col2:
    st.image('./pic/13.jpg')
