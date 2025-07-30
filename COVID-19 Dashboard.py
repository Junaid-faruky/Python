import pandas as pd
import streamlit as st

df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
st.title("COVID-19 Dashboard")
st.line_chart(df[df["location"] == "India"]["new_cases"].dropna())
