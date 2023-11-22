import streamlit as st

import pandas as pd
import numpy as np

from names import names
import random


st.write("# My 1st Streamlit App")
st.write("Hello, *World!* :sunglasses:")

"This works, too"

age = st.slider('How old are you?', 25, 130, 30)
st.write("I'm ", age, 'years old')

totalSavings = value=age*5000
st.metric(label="Your total savings should be", value=totalSavings)

df = pd.DataFrame(
np.random.uniform(0,totalSavings,(10,5)),
columns=('col %d' % i for i in range(5)))

st.table(df)

# # # st.write(df)
df

df = pd.DataFrame(
    [
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

@st.cache_data
def rand_data():
    df = pd.DataFrame(
        np.random.uniform(0,totalSavings,(20,3)),
        columns=['2021', '2022', '2023'],
        index = random.sample(names, 20)
        )
    return df

# st.bar_chart(rand_data())
# st.line_chart(rand_data())

chart_type= st.selectbox("chart type",["line","bar"])

if chart_type == "line":
    st.line_chart(rand_data())
else:
    st.bar_chart(rand_data())

with st.form("my_form"):
   st.write("Enter your details")
   long_jump = st.slider("Long jump personal best [cm]", 0,900,300)
   
   olympics_on = st.toggle('Competed in the Olympics?')
   
   favorite_sports = st.multiselect(
    'What are your favorite Olympic sports?',
    ['Javelin', '110m with Hurdles', 'Marathon', 'Chess',
    'Aikido', 'Stone throwing', 'Streamlit Hackathon'],
    default='Streamlit Hackathon')
   
   accept_toc_val = st.checkbox("Please click to accept Terms & Conditions")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit"
                                    #  ,disabled=not accept_toc_val
                                     )
   if submitted:
       st.write("Long jump:", long_jump, "Sports:", favorite_sports, "TOCs", accept_toc_val)
       


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method for your reward",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)