import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :red[Let's start tracking]")

st.markdown(""" 
- We can use this with command `mlflow.start_run()` and whatever we do inside of that indent will be tracked

- We can set the name of the run and log the different metrics and models. 

- All of the parameters and models are stored in files in the `mlruns` folder with each runs having seperate folders. you can open those files to see the stored data 
""")

code = """

with mlflow.start_run():

    print('Evaluating Popularity recommendation model...')
    popularity_model = PopularityRecommender(item_popularity_df, articles_df)
    metrics, pop_detailed_results_df = model_evaluator.evaluate_model(popularity_model)
    modelName, recall_5, recall_10 = metrics.values()

    
    mlflow.set_tag('mlflow.runName',modelName)
    #mlflow.log_param('any param',param_value)
    mlflow.log_metric('recall@5',recall_5)
    mlflow.log_metric('recall@10',recall_10)
    
    mlflow.sklearn.log_model(popularity_model, "model")
        """

col1, col2 = st.columns([10,1])
col1.code(code,"python")
btn = col2.button("Run", key = "1")
if btn:
    st.image("./hello-main/GIF/track-7.png", width = 650)

for i in range(2):
    st.text("")

st.text("After running this code, you will see something like this inside dashboard")
st.text("( Observe run name, metrics, duration , and model logged.)")

st.video("../GIF/track-9.mov")

st.text("""If you click on the run name, you’ll see something like the following:""")
st.image("./hello-main/GIF/track-11.png", width = 650)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Log the model")
