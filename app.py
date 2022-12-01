# coding:utf-8

import streamlit as st 

# # day 2
# st.write(f"Hello world!")

# # day 3
# st.header(f"st.button")
# if st.button(f"Say, hello"):
#     st.write("Why?")
# else:
#     st.write("Goodbye")

# day 5

import numpy as np 
import altair as alt 
import pandas as pd 

st.header(f"st.write")
st.write(f"Hello, *World!* : sunglasses:")

st.write(1234)


df = pd.DataFrame({
    'first': [1,2,3,4],
    'second': [10,20,30,40]
})

st.write(df)


st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c',
    tooltip=['a','b','c'])

st.write(c)