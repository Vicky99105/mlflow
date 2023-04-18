import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.write("### :red[ML Flow]")

st.markdown("""

        MLFLow is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. 

        MLFLow currently offers four components:

        
        """)

for i in range(3):
    st.text("")


st.image("../Screenshot 2023-04-12 at 1.36.34 AM.png")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Different Experiments")
