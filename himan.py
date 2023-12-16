import streamlit as st
from streamlit_option_menu import option_menu
st.header("Himanshu's personal website")
st.subheader("PPts and Pdf's")
with open("Solid-Waste.pdf", "rb") as file:
    btn = st.download_button(
    label="Download Solid Waste pdf",
    data=file,
    file_name="Solid-Waste.pdf",
    mime="pdf"
    )
st.write()
st.write("All PPTs [link](https://bit.ly/aiml-3-1)")
st.write("Leetcode  [profile](https://leetcode.com/Himanshu_parida)")
st.write("Github  [profile](https://github.com/Himanshu6623)")
st.write()
data = st.file_uploader('File uploader')
st.download_button('On the dl', data)
