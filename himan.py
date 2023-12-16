import streamlit as st
from streamlit_option_menu import option_menu
with open("Solid-Waste.pdf", "rb") as file:
    btn = st.download_button(
    label="Download Solid Waste pdf",
    data=file,
    file_name="Solid-Waste.pdf",
    mime="pdf"
    )