


import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.write("### :red[Let's compare]")

st.markdown(""" Mlflow also provides function to compare these models with different plots""")


st.video("./hello-main/GIF/track-14.mov")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Search Query")
