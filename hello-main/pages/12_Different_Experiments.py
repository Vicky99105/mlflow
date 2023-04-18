import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.write("### :red[Content based filtering model]")

st.markdown("""
        Let's try a new model for recommending..

        Content-based filtering approaches leverage description or attributes from items the user has interacted to recommend similar items.  
        It depends only on the user previous choices,
        making this method robust to avoid the cold-start problem
          
        Here we are using a very popular technique in information retrieval (search engines) named TF-IDF.   
        This technique converts unstructured text into a vector structure, where each word is represented by a position in the vector, 
        and the value measures how relevant a given word is for an article
    """)

# code_str = '''#Ignoring stopwords (words with no semantics) from English and Portuguese (as we have a corpus with mixed languages)
# stopwords_list = stopwords.words('english') + stopwords.words('portuguese')

# #Trains a model whose vectors size is 5000, composed by the main unigrams and bigrams found in the corpus, ignoring stopwords
# vectorizer = TfidfVectorizer(analyzer='word',
#                      ngram_range=(1, 2),
#                      min_df=0.003,
#                      max_df=0.5,
#                      max_features=5000,
#                      stop_words=stopwords_list)

# item_ids = articles_df['contentId'].tolist()
# tfidf_matrix = vectorizer.fit_transform(articles_df['title'] + "" + articles_df['text'])
# tfidf_feature_names = vectorizer.get_feature_names()
# tfidf_matrix'''

# col1, col2 = st.columns([10,1])
# col1.code(code_str, language = "python")
# btn = col2.button("Run")
# if btn:
#     st.image("../GIF/CB-1.png", width = 600)


# st.markdown("""
#     To model the user profile, we take all the item profiles the user has interacted and average them. The average is weighted by the interaction strength, in other words, the articles the user has interacted the most (eg. liked or commented) will have a higher strength in the final user profile.
#     """)

# code_str = '''def get_item_profile(item_id):
#     idx = item_ids.index(item_id)
#     item_profile = tfidf_matrix[idx:idx+1]
#     return item_profile

# def get_item_profiles(ids):
#     item_profiles_list = [get_item_profile(x) for x in ids]
#     item_profiles = scipy.sparse.vstack(item_profiles_list)
#     return item_profiles

# def build_users_profile(person_id, interactions_indexed_df):
#     interactions_person_df = interactions_indexed_df.loc[person_id]
#     user_item_profiles = get_item_profiles(interactions_person_df['contentId'])
    
#     user_item_strengths = np.array(interactions_person_df['eventStrength']).reshape(-1,1)
#     #Weighted average of item profiles by the interactions strength
#     user_item_strengths_weighted_avg = np.sum(user_item_profiles.multiply(user_item_strengths), axis=0) / np.sum(user_item_strengths)
#     user_profile_norm = sklearn.preprocessing.normalize(user_item_strengths_weighted_avg)
#     return user_profile_norm

# def build_users_profiles(): 
#     interactions_indexed_df = interactions_train_df[interactions_train_df['contentId'] \
#                                                    .isin(articles_df['contentId'])].set_index('personId')
#     user_profiles = {}
#     for person_id in interactions_indexed_df.index.unique():
#         user_profiles[person_id] = build_users_profile(person_id, interactions_indexed_df)
#     return user_profiles
    
# '''

# col1, col2 = st.columns([10,1])
# col1.code(code_str, language = "python")
# btn = col2.button("Run", key = "2")


# code_str = '''user_profiles = build_users_profiles()
# len(user_profiles)
    
# '''

# col1, col2 = st.columns([10,1])
# col1.code(code_str, language = "python")
# btn = col2.button("Run", key = "3")
# if btn:
#     st.image("../GIF/CB-2.png", width = 600)

code_str = '''class ContentBasedRecommender:
    
    MODEL_NAME = 'Content-Based'
    
    def __init__(self, items_df=None):
        self.item_ids = item_ids
        self.items_df = items_df
        
    def get_model_name(self):
        return self.MODEL_NAME
        
    def _get_similar_items_to_user_profile(self, person_id, topn=1000):
        #Computes the cosine similarity between the user profile and all item profiles
        cosine_similarities = cosine_similarity(user_profiles[person_id], tfidf_matrix)
        #Gets the top similar items
        similar_indices = cosine_similarities.argsort().flatten()[-topn:]
        #Sort the similar items by similarity
        similar_items = sorted([(item_ids[i], cosine_similarities[0,i]) for i in similar_indices], key=lambda x: -x[1])
        return similar_items
        
    def recommend_items(self, user_id, items_to_ignore=[], topn=10, verbose=False):
        similar_items = self._get_similar_items_to_user_profile(user_id)
        #Ignores items the user has already interacted
        similar_items_filtered = list(filter(lambda x: x[0] not in items_to_ignore, similar_items))
        
        recommendations_df = pd.DataFrame(similar_items_filtered, columns=['contentId', 'recStrength']) \
                                    .head(topn)

        if verbose:
            if self.items_df is None:
                raise Exception('"items_df" is required in verbose mode')

            recommendations_df = recommendations_df.merge(self.items_df, how = 'left', 
                                                          left_on = 'contentId', 
                                                          right_on = 'contentId')[['recStrength', 'contentId', 'title', 'url', 'lang']]


        return recommendations_df
    
content_based_recommender_model = ContentBasedRecommender(articles_df)'''

col1, col2 = st.columns([10,1])
col1.code(code_str, language = "python")
btn = col2.button("Run", key = "5")
# if btn:
#     st.image("../Screenshot 2023-04-12 at 12.45.26 PM.png", width = 600)

code_str = '''print('Evaluating Content-Based Filtering model...')
cb_global_metrics, cb_detailed_results_df = model_evaluator.evaluate_model(content_based_recommender_model)
print('Global metrics:%s' % cb_global_metrics)
cb_detailed_results_df.head(5)'''

col1, col2 = st.columns([10,1])
col1.code(code_str, language = "python")
btn = col2.button("Run", key = "6")
if btn:
    st.image("../GIF/CB-3.png", width = 600)

st.text("""
With personalized recommendations of content-based filtering model,
we have a Recall@5 to about 0.162, which means that about 16% of interacted 
items in test set were ranked by this model among the top-5 items 
(from lists with 100 random items). And Recall@10 was 0.261 (52%). 
The lower performance of the Content-Based model compared to the 
Popularity model may indicate that users are not that fixed in content 
very similar to their previous reads.
""")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Tracking")
