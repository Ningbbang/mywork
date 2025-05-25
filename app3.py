import streamlit as st
import pandas as pd

df = pd.read_csv('workhour.csv')
st.dataframe(df)