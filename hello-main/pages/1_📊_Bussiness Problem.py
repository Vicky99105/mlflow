# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
import streamlit.components.v1 as components


tabs = ["Explore WIX", "Hope you got it", "Problem Statement"]
tabs1, tabs2, tabs3 = st.tabs(tabs)




#I'm trying

with tabs1:
        st.write("### Imagine ....🤔")

        st.write("You are `Vishal` working as a Data Scientist at `WIX`")
        
        html_str = """

                <html>
                <head>
                <title>Yearly Symbol Prices</title>
                </head>
                <frameset>
                <frame src='https://www.wix.com/'>
                </frameset>
                </html>

                """


        with st.expander("Explore Wix.com and list out some places where you think Wix is using Machine Learning ?? ", True):
                with st.form("form1",clear_on_submit = True):
                        ans = st.text_input("Type your answer here....")
                        submit = st.form_submit_button("submit")

        components.html(html_str, width = 700, height = 400)



with tabs2:
        st.write("### :blue[Hope you have covered most of these:]")

        st.markdown("""
        
                - ##### Churn and Premium prediction
                - ##### Template’s Semantic Search
                - ##### Logo Beauty ranking
                - ##### Auto Enhancement
                - ##### Spam classifier
                - ##### Super resolution
                - ##### Phishing Detection
                - ##### Object and Portrait segmentation

                
                """)


with tabs3:
        st.write("## Problem statement")

        st.markdown("""
        
                ###### :blue[Wix’s support organization is very big, around 1000 support agents maintaining 10,000 support article for user to build website better Can we help them using machine learning ?]

                """)

        # for i in range(3):
        #         st.text("")

        st.image("../GIF/giphy.gif")


        with st.expander("Can you suggest some solution to this problem ?", True):
                with st.form("form2",clear_on_submit = True):
                        ans = st.text_input("Type your answer here....")
                        submit = st.form_submit_button("submit")

        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        if col7.button('Next'):
                switch_page('Recommend it')