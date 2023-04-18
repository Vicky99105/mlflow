import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
import streamlit.components.v1 as components



st.markdown("""

    ##### Remember silly things, we used to do to maintain records

    """)

for i in range(1):
    st.text("")

st.text("writting results in notepad, saving hundreds of different models")
st.image("../Screenshot 2023-04-12 at 1.23.45 AM.png")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("The New Challenge")

