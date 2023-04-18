import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
import streamlit.components.v1 as components



st.image("../Screenshot 2023-04-12 at 1.12.43 AM.png")

for i in range(3):
    st.text("")

st.markdown("""

    - ##### We can’t afford to re-implement each of these boxes for every model 
    - ##### Challenge is to generalize each set of boxes into coherent set of components or platform that will enable most of model on production
    """)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Let's build something")

