import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time

import streamlit.components.v1 as components


st.write("## :red[Build a Recommender System 🤖]")

st.write("##### We can build a recommender system to find the most relevant support article based on query")

st.image("../Screenshot 2023-04-11 at 11.04.56 PM.png")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page('Identify the challenge')