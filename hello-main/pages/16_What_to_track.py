import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :blue[What to track !]")

st.markdown(""" 
Next, you can start to think about what do you want to keep track in your analysis/experiment. MLflow categorizes these into:

- ###### :red[__Parameters__ ]: Parameters are variables that you change/tweak when tuning your model.
` mlflow.log_param() `
- ###### :red[__Metrics__]: Metrics are values that you want to measure as a result of tweaking your parameters. Typical metrics that are tracked can be items like F1 score, RMSE, MAE etc.
`mlflow.log_metric()`
- ###### :red[__Artifacts__]: Artifacts are any other items that you wish to store. Typical artifacts to keep track of are PNGs of graphs,plots, confusion matrix, and also pickled model files.
`mlflow.log_artifact()`
""")

st.markdown("""

       ##### :blue[Can you name few things in each category for a recommender system ?] 

        """)

st.text_input("Type your answer here...")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Let's track")
