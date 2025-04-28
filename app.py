import streamlit as st
import pandas as pd
import preprocessor, helper


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)
st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Olympic_rings_without_rims.svg/1200px-Olympic_rings_without_rims.svg.png')
user_menu = st.sidebar.radio(
    "Select a Option",
    ('Medal Tally', 'Overall Analysis', 'Country-Wisrr Analysis', 'Aythletes wise Analysis')
)


if user_menu =='Medal Tally':
    st.header("Medal Tally")
    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)