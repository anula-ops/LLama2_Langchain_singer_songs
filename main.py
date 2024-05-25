import streamlit as st
import langchain_singer

st.title("Singer Name and their songs Generator")

country = st.sidebar.selectbox("Pick a Country", ("India", "Italy", "China", "Iran","Dubai", "America", "Mexico", "Brazil","Russia"))

if country:
    response = langchain_singer.generate_singer_name_and_songs(country)
    st.header(response['singer_name'].strip())
    songs_list = response['songs'].strip().split(",")
    st.write("**Songs**")
    for song in songs_list:
        st.write("-", song)