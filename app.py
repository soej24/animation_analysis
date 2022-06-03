from tkinter.tix import COLUMN
from pyparsing import empty
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")
sp1,con1,sp2 = st.columns([0.3,1.0,0.3])
sp1,con2,con3,sp2 = st.columns([0.3,0.5,0.5,0.3])
sp1,con4,sp2 = st.columns([0.3,1.0,0.3])
sp1,con5,con6,sp2 = st.columns([0.3,0.5,0.5,0.3])
sp1,con7,sp2 = st.columns([0.3,1.0,0.3])
sp1,con8,con9,sp2 = st.columns([0.3,0.5,0.5,0.3])

def main() :

    with sp1 :
        empty()
   
    with con1 :
        df = pd.read_csv('data/anime.csv', index_col = 'Anime-PlanetID', encoding='UTF-8')
        df['Rating Score'] = df['Rating Score'].apply (int)

        st.title('애니메이션 검색 및 분석')
        st.markdown("***")
        image = Image.open('data/img/main_img.jpg')
        st.image(image)
        st.markdown("***")

    with con2 :
        tags = ['Action', 'Adventure', 'Comedy', 'Drama', 'Sports', 'Mecha','Romance', 'Fantasy', 'Horror',\
                    'Sci Fi', 'School Life','Work Life', 'Family','Short Episodes']
        choice_list = st.selectbox('장르를 선택하세요!', tags)

        st.markdown("***")
        score = st.radio(label = '평점을 선택하세요!', options = ['5점', '4점', '3점', '2점', '1점'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        type = st.radio(label = '타입을 선택하세요!', options = ['TV', 'Music', 'Web', 'Other', 'Movie', 'DVD'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    with con3 :
     
        if score == '5점' :
            score_last = 5.0

        if score == '4점' :
            score_last = 4.0

        if score == '3점' :
            score_last = 3.0

        if score == '2점' :
            score_last = 2.0

        if score == '1점' :
            score_last = 1.0     

        df_result= df.loc[ df['Tags'].str.contains(choice_list) & (df['Type'] == type) & (df['Rating Score'] == score_last), ]
        df_result = df_result.sort_index(ascending=False)
        st.dataframe(df_result)

    with con4 :
        st.markdown("***")
        st.subheader('내가 보고싶은 애니는?')
        column_name = sorted(list(df_result['Name'].unique()))
        # st.text(column_name)
        choice_list2 = st.selectbox('애니를 선택해 주세요!!', column_name)

        # 진열이가 가르켜준 코드
        # unique로 뽑으면 넘파이 array로 나와서 그걸 다시
        # 리스트로 바꿔서 저장해줘야 한다.
        # df1 = sorted(list(df['제조사명'].unique()))
        # choice = st.sidebar.selectbox('브랜드 선택', df1)

        # st.text(choice_list2)
        df_choice = df.loc[ df['Name'] == choice_list2, ]
        st.dataframe(df_choice)
        st.markdown("***")

    with con5 :

        # 선택한 데이터에서 인덱스 id값을 뽑는다.
        ani_id = df_choice.index[0]
        # st.text(ani_id)

        df_movie = pd.read_csv('data/ani_link.csv', index_col = 'm_id', encoding='UTF-8')        
        movie_choice = df_movie.loc[ani_id] # 동영상 id가 애니 id와 같은 데이터를 추출
        m_url = movie_choice['m_url']

        st.video(m_url) 
     
    with con6 :

        title_name = list(df_choice['Name'].unique())
        title_name = ' '.join(s for s in title_name)
        st.subheader(title_name)
 
        content = list(df_choice['Synopsis'].unique())
        content = ' '.join(s for s in content)
        st.markdown(content)

        url = list(df_choice['Url'].unique())
        url = ' '.join(s for s in url)
        link = url
        st.markdown(link, unsafe_allow_html=True)  
    
    with con7 :
        
        st.markdown("***")
        st.subheader("투표를 가장 많이 한 애니")

        vote_max = df.loc[ df['Number Votes'] == df['Number Votes'].max(), ]
        st.dataframe(vote_max)

        st.markdown("***") 
        st.subheader("투표를 가장 적게 한 애니")    

        vote_min = df.loc[ df['Number Votes'] == df['Number Votes'].min(), ]
        st.dataframe(vote_min)

        st.markdown("***")
        st.subheader("별점별 투표수 보기 차트")

    with con8 :

        fig2 = plt.figure()  
        sns.countplot(data=df, x='Rating Score')
        st.pyplot(fig2)


    with con9 :

        fig =  px.pie(df, names='Rating Score', values='Number Votes', title='별점별 투표수')
        st.plotly_chart(fig)

        st.markdown("***")  
        st.text('투표에 따른 총점 상관관계')

        st.markdown("***") 
        st.text('영화를 선택하면 그것이 긍정인지 부정인지')


    with sp1 :
        empty()

if __name__ == '__main__' :
    main()