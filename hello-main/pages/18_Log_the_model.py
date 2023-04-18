import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :red[Model logging]")

st.markdown(""" In the last slide we saw `mlflow.sklearn.log_model(popularity_model, "model")`.  

By doing so we are saving the actual model produced by the run.
That’s a very good level of convenience. You now have not only your trained model managed for
you (the model.pkl file), but you also have it’s dependencies automatically captured in three 
different flavours, i.e. conda.yaml, python_env.yaml and requirements.txt.  

Furthermore, you even have  copy-and-paste examples available for you, on how to load this model.

""")

st.image("./hello-main/GIF/track-12.png", width = 650)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("All together")
