import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :red[Log them all...]")

st.markdown(""" let's create a general function to apply tracking and call all the models together""")

code = """

def create_experiment(experiment_name, model_name, run_metrics, model,special_tag=None,run_params=None):
    mlflow.set_experiment(experiment_name)
    
    with mlflow.start_run():
        mlflow.set_tag('mlflow.runName',model_name)
        if not run_params == None:
            for param in run_params:
                mlflow.log_param(param, run_params[param])
            
        for metric in run_metrics:
          if metric!="modelName":
            mlflow.log_metric(metric, run_metrics[metric])
        
        mlflow.sklearn.log_model(model, "model")
        print(modelName)
        mlflow.set_tags({"tag2":special_tag, "tag3":"Production"})
            
    print('Run - %s is logged to Experiment - %s' %(model_name, experiment_name))
        """


col1, col2 = st.columns([10,1])
col1.code(code,"python")
btn = col2.button("Run", key = "1")



code = """

popularity_model = PopularityRecommender(item_popularity_df, articles_df)
content_based_recommender_model = ContentBasedRecommender(articles_df)
cf_recommender_model = CFRecommender(cf_preds_df, articles_df)
hybrid_recommender_model = HybridRecommender(content_based_recommender_model, cf_recommender_model, articles_df,
                                             cb_ensemble_weight=1.0, cf_ensemble_weight=100.0)

models = [popularity_model, content_based_recommender_model,cf_recommender_model, hybrid_recommender_model ]

for model in models:
  metrics, results_df = model_evaluator.evaluate_model(model)
  model_name, recall_5, recall_10 = metrics.values()
  
  create_experiment("article_recommender_system", model_name, metrics, model,"general flow")


        """


col1, col2 = st.columns([10,1])
col1.code(code,"python")
btn = col2.button("Run", key = "2")

st.text("you will see all the models logged inside dashboard")

st.image("../GIF/track-13.png", width = 650)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Let's compare")
