import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time

st.write("#### :red[How Wix solved this problem ?]")

for i in range(3):
    st.text("")

st.markdown("""

    - ###### Since this task heavily on machine learning models to make personalized workout recommendations for users, but John and his team were finding it increasingly difficult to manage the machine learning lifecycle.

    - ###### They were constantly experimenting with different models, tweaking hyperparameters, and trying out new algorithms. They had to keep track of all these different experiments, manage dependencies, and ensure that their models were working as expected.

    - ###### That's when they discovered MLFlow. With MLFlow, John and his team could easily track their experiments, compare different models, and share their work with each other

    
    """)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Intro to mlflow")
