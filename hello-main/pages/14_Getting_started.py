import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :red[Getting started with MLFlow]")

st.text("Install it, simply use pip command")

st.code("!pip install mlflow","python")

st.text("Import it")

st.code("import mlflow","python")

st.markdown(""" we'll start by setting up our experiment name under which we wanna perform all our work  
if not set, everything will be stored under experiment name "Default"
    """)

st.code(""" mlflow.set_experiment("article_reccomender_system")""","python")

st.markdown(""" By the time you run this command, you will start seeing a 
folder name `mlruns` inside your directory. """)

st.image("./hello-main/GIF/Track-1.png",width=300)

st.text("what these files and folder represent, we'll see it soon")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("MLFlow UI")

