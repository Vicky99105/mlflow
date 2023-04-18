import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
import streamlit.components.v1 as components


st.write("## :blue[Well....]")

col1, col2 = st.columns(2)

st.markdown("""

       ##### Building a recommender system might be easy. But other than training model..
        
        """)

st.image("./hello-main/Screenshot 2023-04-11 at 11.10.04 PM.png")


for i in range(3):
    st.text("")

col1, col2 = st.columns(2)

st.markdown("""

       ##### :red[What other challenges do you think comes with the problem ?] 

        """)

st.text_input("Type your answer here...", placeholder = "Take the hint from the image shown...")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page('Process')