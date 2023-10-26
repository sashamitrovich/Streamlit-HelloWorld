import streamlit as st
import pandas as pd
import numpy as np


   
st.write("# My 1st Streamlit App")
st.write("Hello, *World!* :sunglasses:")

age = st.slider('How old are you?', 25, 130, 30)
st.write("I'm ", age, 'years old')

st.metric(label="Your total savings should be:", value=age*5000)

df = pd.DataFrame(
np.random.randn(10, 5),
columns=('col %d' % i for i in range(5)))

st.table(df)

# st.write(df)
# df

df = pd.DataFrame(
    [
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


def rand_data():
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return df

# st.bar_chart(rand_data())
# st.line_chart(rand_data())

chart_type= st.selectbox("chart type",["line","bar"])

if chart_type == "line":
    st.line_chart(rand_data())
else:
    st.bar_chart(rand_data())

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)