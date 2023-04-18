import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("### :red[MLFlow UI]")

st.markdown(""" 
MLflow provides the option to view all the runs and experiments on a web based ui that is really easy to use and see the logged data.

In the folder "mlruns" where you have this experiments

run the command `mlflow ui` this will start an ml flow ui server that is by default open at port 5000 on your localhost

or

127.0.0.1 you can change the port by using -p port_num along with the command eg: `mlflow ui -p 8899`

""")

st.image("./hello-main/GIF/track-4.png",width=700)

st.markdown(""" You can see our experiment name `article_recommender_system` 
here and other named `Default` but nothing has been logged yet""")

st.markdown(""" :blue[For the sake of in-browser experience, we will be using `ngrok` which will provide us a link through which we can visualize the same dashboard as of local system]""")

st.text("just run this code in collab cell")

code = """!pip install pyngrok --quiet

import mlflow

# run tracking UI in the background
get_ipython().system_raw("mlflow ui --port 5000 &") # run tracking UI in the background


# create remote tunnel using ngrok.com to allow local port access
# borrowed from https://colab.research.google.com/github/alfozan/MLflow-GBRT-demo/blob/master/MLflow-GBRT-demo.ipynb#scrollTo=4h3bKHMYUIG6

from pyngrok import ngrok

# Terminate open tunnels if exist
ngrok.kill()

# Setting the authtoken (optional)
# Get your authtoken from https://dashboard.ngrok.com/auth
NGROK_AUTH_TOKEN = "your auth token"
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Open an HTTPs tunnel on port 5000 for http://localhost:5000
ngrok_tunnel = ngrok.connect(addr="5000", proto="http", bind_tls=True)
print("MLflow Tracking UI:", ngrok_tunnel.public_url)"""

col1, col2 = st.columns([10,1])
col1.code(code,"python")
btn = col2.button("Run", key = "1")
if btn:
    st.image("./hello-main/GIF/track-5.png", width = 650)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col7.button('Next'):
        switch_page("What to track")

