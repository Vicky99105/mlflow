import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :red[MLFlow Tracking]")

st.markdown("""
    - ###### As you go through your experiments you’d like keep track of things like the hyperparameters you’ve tried, the metrics you’ve got, which notebooks or pieces of code executed those experiments, when they were executed, by whom, etc. MLflow Tracking just got you covered.
    - ###### But before it, let’s understand two terms that we will use throughout

      - ###### `Runs` : A run is a collection of parameters, metrics, labels, and artifacts related to the training process of a machine learning model.

      - ###### An `experiment` is the basic unit of MLflow organization. All MLflow runs belong to an experiment. For each experiment, you can analyze and compare the results of different runs

        
        """)


col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Getting started")

