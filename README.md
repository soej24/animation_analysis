# Animation analysis
## (애니메이션 검색 및 분석)
- 데이터 출처 : https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020
- 장르, 별점, 타입별 애니검색
- 관련 오프닝 동영상, 소개, anime-planet 사이트 연결
- 투표가 가장 많은 애니
- 투표가 가장 적은 애니
<br /><br /><br />
![title](./data/img/main_img.jpg)
<br /><br />

## 1. 애니메이션 검색
- 장르 : Action, Adventure, Comedy, Drama, Sports, Mecha, Romance, Fantasy, Horror, Family
- 평점 : 5점, 4점, 3점, 2점, 1점
- 타입 : TV, Music, Web, Other, Movie, DVD
- 옵션 선택에 따른 애니 리스트를 보여줍니다.
- 데이터가 없는경우 '검색된 데이터가 없습니다' 예외처리

#####  옵션별 선택하는 Code
```js
        tags = ['Action', 'Adventure', 'Comedy', 'Drama', 'Sports', 'Mecha','Romance', 'Fantasy', 'Horror','Family']
        choice_list = st.selectbox('장르를 선택하세요!', tags)

        st.markdown("***")
        score = st.radio(label = '평점을 선택하세요!', options = ['5점', '4점', '3점', '2점', '1점'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        type = st.radio(label = '타입을 선택하세요!', options = ['TV', 'Music', 'Web', 'Other', 'Movie', 'DVD'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

```
<br />

#####  예외처리 후, 데이터가 있으면 보여주는 Code
```js
        if df_result.empty :
            st.text('')
            st.text('')                         
            st.text('검색된 데이터가 없습니다!!')
        else :
            st.dataframe(df_result)  
```
<br />

## 2. 내가 보고싶은 애니는?
- 옵션 선택에 따른 애니 리스트를 셀렉트박스로 받아와
  유저가 원하는 보고싶은 애니를 쉽게 선택할수 있습니다.
- 선택된 애니와 관련된 동영상, 제목, 간단한 설명 출력
- 동영상은 유튜브에서 링크를 가져와 url 관련 csv 파일 만들고
  애니와 ID값을 통일시켜 불러오도록 하였습니다.
- 링크를 누르면 해당 애니의 소개 사이트로 이동합니다.

## 3. 투묘를 가장 많이 한 애니
- 투표를 가장 많이 한 애니를 보여줍니다.

## 4. 투표를 가장 적헤 한 애니
- 투표를 가장 적게 한 애니를 보여줍니다.

## 5. 별점별 투표수 보기 차트
- 데이터 시각화를 위해 plotly(플로틀리) 사용
<br />

## programming language / graphic tool
- [ Python ] [ Pandas ] [ Streamlit ] [ AWS ec2 ] [ Visuil Studio Code ] [ Photoshop ]
<br />

## Link   
- [🚗 Visit EASYME.md's Repo](https://github.com/soej24/animation_analysis/blob/main/README.md)   
- [🙋‍♂️ Visit ONE:A's Github](https://github.com/soej24/animation_analysis)