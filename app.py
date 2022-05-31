import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# col1, col2 = st.columns([3, 1])
col3, col4 = st.columns(2)

def main() :

    #with col1 :
    df = pd.read_csv('data/anime.csv', encoding='UTF-8')
    df['Rating Score'] = df['Rating Score'].apply (int)

    st.title('애니메이션 검색 및 분석')
    st.markdown("***")
    st.text('동영상 들어갈 부분')
    st.video("https://youtu.be/Dqe0uuH8yi0")

    tags = ['Action', 'Adventure', 'Comedy', 'Drama', 'Sports', 'Mecha','Romance', 'Fantasy', 'Horror',\
                'Sci Fi', 'School Life','Work Life', 'Family','Short Episodes']
    st.markdown("***")
    choice_list = st.selectbox('장르를 선택하세요!', tags)

    # if choice_list != 'close' :
    #     result2 = df.loc[ df['Tags'].str.contains(choice_list), ]
    #     st.dataframe( result2 )

    score = st.radio(label = '평점을 선택하세요!', options = ['5점', '4점', '3점', '2점', '1점'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # if score != 'close' :       
        
    #     if score == '5점' :
    #         score = 5.0

    #     if score == '4점' :
    #         score = 4.0

    #     if score == '3점' :
    #         score = 3.0

    #     if score == '2점' :
    #         score = 2.0

    #     if score == '1점' :
    #         score = 1.0

    #     result3 = df.loc[ df['Rating Score'] == score, ]
    #     st.dataframe( result3 )

    type = st.radio(label = '타입을 선택하세요!', options = ['TV', 'Music', 'Web', 'Other', 'Movie', 'DVD'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if score == '5점' :
        score = 5.0

    if score == '4점' :
        score = 4.0

    if score == '3점' :
        score = 3.0

    if score == '2점' :
        score = 2.0

    if score == '1점' :
        score = 1.0

    st.markdown("***")
    df_result= df.loc[ (df['Tags'].str.contains(choice_list)) & (df['Type'].str.contains(type)) & (df['Rating Score'] == 5.0), ]
    st.dataframe(df_result)



    with col3 :
        st.text('여기는 세번째')
    with col4 :
        st.text('여기는 네번째')

    

    






    #df = pd.read_csv('data/anime.csv', encoding='UTF-8')
    #st.dataframe(df)



if __name__ == '__main__' :
    main()