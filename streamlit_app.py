import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
df = pd.read_csv("heatwave_data.csv")

st.title("📊 지역별 폭염일수 변화 (2018~2022)")

# 연도 선택 슬라이더
year = st.slider("연도를 선택하세요", 
                 min_value=int(df["year"].min()), 
                 max_value=int(df["year"].max()), 
                 step=1, value=int(df["year"].min()))

# 선택된 연도의 데이터 필터링
df_year = df[df["year"] == year]

# Plotly 지도 시각화
fig = px.scatter_geo(
    df_year,
    lat="latitude",
    lon="longitude",
    text="region",  # 지역 이름 표시
    size="heatwave_days",  # 점 크기로 폭염일수 표현
    color="heatwave_days", # 색깔도 같이 표현
    projection="natural earth",
    color_continuous_scale="OrRd",
    title=f"{year}년 지역별 폭염일수"
)

st.plotly_chart(fig, use_container_width=True)
