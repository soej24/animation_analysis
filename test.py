import streamlit as st

search_term = st.text_input('Search term', value='streamlit')

col1, col2 = st.beta_columns([2,1])

with col1:
    from_date = st.selectbox('1 month ago', options=['A', 'B'])

with col2:
    limit = st.number_input('Limit', value=10000)


col3, col4, col5 = st.beta_columns(3)

with col3:
    min_replies = st.number_input('Minimum replies', value=0)
with col4:
    min_retweets = st.number_input('Minimum retweets', value=0)
with col5:
    min_hearts = st.number_input('Minimum hearts', value=0)