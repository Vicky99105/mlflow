import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.write("### :red[Popularity model]")

st.markdown("""
    
        A common (and usually hard-to-beat) baseline approach is the Popularity model.  
          
        __This model is not actually personalized__ - it simply recommends to a user the most popular items that the user has not previously consumed. 
        As the popularity accounts for the "wisdom of the crowds", it usually provides good recommendations, generally interesting for most people.

    """)

# code_str = '''#Computes the most popular items
# item_popularity_df = interactions_full_df.groupby('contentId')['eventStrength'].sum().sort_values(ascending=False).reset_index()
# item_popularity_df.head(5)'''

# col1, col2 = st.columns([10,1])
# col1.code(code_str, language = "python")
# btn = col2.button("Run")
# if btn:
#     st.image("../Screenshot 2023-04-12 at 12.37.55 PM.png", width = 400)



code_str = '''class PopularityRecommender:
    
    MODEL_NAME = 'Popularity'
    
    def __init__(self, popularity_df, items_df=None):
        self.popularity_df = popularity_df
        self.items_df = items_df
        
    def get_model_name(self):
        return self.MODEL_NAME
        
    def recommend_items(self, user_id, items_to_ignore=[], topn=10, verbose=False):
        # Recommend the more popular items that the user hasn't seen yet.
        recommendations_df = self.popularity_df[~self.popularity_df['contentId'].isin(items_to_ignore)] \
                               .sort_values('eventStrength', ascending = False) \
                               .head(topn)

        if verbose:
            if self.items_df is None:
                raise Exception('"items_df" is required in verbose mode')

            recommendations_df = recommendations_df.merge(self.items_df, how = 'left', 
                                                          left_on = 'contentId', 
                                                          right_on = 'contentId')[['eventStrength', 'contentId', 'title', 'url', 'lang']]


        return recommendations_df
    
'''

col1, col2 = st.columns([10,1])
col1.code(code_str, language = "python")
btn = col2.button("Run", key = "2")


code_str = '''print('Evaluating Popularity recommendation model...')
popularity_model = PopularityRecommender(item_popularity_df, articles_df)
pop_global_metrics, pop_detailed_results_df = model_evaluator.evaluate_model(popularity_model)
print('Global metrics:%s' % pop_global_metrics)
pop_detailed_results_df.head(5)'''

col1, col2 = st.columns([10,1])
col1.code(code_str, language = "python")
btn = col2.button("Run", key = "3")
if btn:
    st.image("../Screenshot 2023-04-12 at 12.45.26 PM.png", width = 600)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("What if...")
