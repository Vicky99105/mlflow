import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
import streamlit.components.v1 as components


st.markdown("""

    #### :blue[We have successfully built a Popularity based recommender system , but suppose we want to try out content based rec system]

    1. ##### We can change the model and run the code again

    - ##### `but we will loose the output and results from the old model`

    2. ##### We can create new cells below these to create a new model with the new model

    - ##### `but then when we have a lot of experiments in one file it will be really difficult finding the one we want to look at`

    3. ##### We can create new files for each experiment

    - ##### `but for actually comparing the results and outputs you'll still have to open each file and look into it closely`


        """)
    
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Silly things")
