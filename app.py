import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

col1, col2 = st.columns([2,1])

def main() :

    df = pd.read_csv('data/anime.csv', encoding='UTF-8')

    st.title('애니메이션 검색 및 분석')
    st.markdown("***")
    st.text('동영상 들어갈 부분')
    st.video("https://youtu.be/Dqe0uuH8yi0")

    st.markdown("***")


    type = st.radio(label = '타입을 선택하세요!', options = ['Null', 'TV', 'Music', 'Web', 'Other', 'Movie', 'DVD'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if type != 'Null' :    
        result = df.loc[ df['Type'].str.contains(type), ]
        st.dataframe( result )

    tags = ['Null','Action', 'Adventure', 'Comedy', 'Drama', 'Shounen', 'Sports', 'Mecha',\
            'Romance', 'Fantasy', 'Horror', 'Sports', 'Sports', 'Mecha', 'Sci Fi', 'School Life',\
            'Work Life', 'Family', 'Demons', 'Zombies','Anima','Tsundere', 'Short Episodes']
    st.markdown("***")
    choice_list = st.selectbox('장르를 선택하세요!', tags)

    if choice_list != 'Null' :
        result2 = df.loc[ df['Tags'].str.contains(choice_list), ]
        st.dataframe( result2 )

    st.markdown("***")
    score = st.radio(label = '평점을 선택하세요!', options = ['Null','All', 'Very Positive', 'Mostly Positive', 'Mixed', 'Overwhelmingly Positive'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

 
    

    






    #df = pd.read_csv('data/anime.csv', encoding='UTF-8')
    #st.dataframe(df)



if __name__ == '__main__' :
    main()