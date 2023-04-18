import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :red[Let’s build a recommender system]")


st.markdown("""

    We have been provided with two `CSV` files
    - __shared_articles.csv__ : Contains the information about article like sharing date, the original url, title, content, the article' lang and information about the user who shared the article.

    - __users_interactions.csv__ : Contains logs of user interactions on shared articles. It can be joined to articles_shared.csv by contentId column.

    """)

st.write("### :red[Task]")

st.markdown("""

        To build a recommender system to suggest best articles based on the query provided
        - `Note`: The preprocessing steps and other miscellaneous code is present in this [colab file](https://colab.research.google.com/drive/12-VMhSOz9_cHPnxfcvAW8fJGjkB04qsa#scrollTo=OUzrfb6MHh4B), since our main focus is `ML-Flow`.


        """)


col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("Popularity model")
