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

from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page
import os

st.session_state['time_taken'] = 0

LOGGER = get_logger(__name__)




def run():
    st.set_page_config(
        page_title="What will we do?",
        page_icon="👋",
    )


    st.write("## :red[INTRODUCTION TO ML Flow] 👋")


    st.sidebar.success("Let's start the Topic")

    col1,col2 = st.columns(2)

    with col1:

        st.write("##### Hold your tea and get ready to cover 😎")
        st.markdown(
            """
            - ##### A real life business Problem 📋
            - ##### Teeny Tiny of Theory 📚
            - ##### Bit about Recommender System 🤖
            - ##### A take away Challenge 🧑‍💻


        """
        )
    
    with col2:

        file_path = "path/to/file.txt"

        st.image("./GIF/intro.gif")

    for i in range(3):
        st.text("")

    st.write("##### ⏱️:  30 min")

    col1, col2, col3, col4 = st.columns(4)
    if col4.button('Shall we Start??'):
        switch_page('Bussiness Problem')

if __name__ == "__main__":
    run()
