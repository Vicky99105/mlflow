import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
import streamlit.components.v1 as components



st.write("#### :blue[Due to the circular nature of this process, its more about experimenting and trying out different things that may work]")

for i in range(3):
    st.text("")
col1, col2 = st.columns(2)

col1.markdown("""

        - ML is not just code. It is code plus data that we need to keep a track of. Data can be sourced from multiple storage units use different models and model hyperparameters 
        - Run the same code in a different environment

        - Model governance is another important aspect, where everything starting from experimentation to deployment is tracked for auditing purposes, where models are tested for speed, accuracy, drift while in production to avoid inaccuracy.


        """)

col2.image("../GIF/lif2.png") 

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page('ML is hard')