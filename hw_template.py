import streamlit as st
import pandas as pd
import numpy as np

st.write("# My 1st SiS App")
st.write("Hello, *World!* :sunglasses:")


age = st.slider('How old are you?', 25, 130, 30)
st.write("I'm ", age, 'years old')

st.metric(label="Your saltotal savings should be:", value=age*5000)

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

df

st.experimental_data_editor(df)

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


a,b = st.columns(2)
with a:
    st.line_chart(rand_data())
with b:
    st.bar_chart(rand_data())

