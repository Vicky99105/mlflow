import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time 


st.write("## :red[New Problem]")

st.markdown(
    """

    ###### To build, deploy, maintain and monitor ML models in production with minimal engineering efforts



    """)

with st.expander("Do you have any suggestions ?", True):
    with st.form("form2",clear_on_submit = True):
            ans = st.text_input("Type your answer here....")
            submit = st.form_submit_button("submit")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Wix's Solution")
