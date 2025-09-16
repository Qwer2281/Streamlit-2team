import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
df = pd.read_csv("data/data/heatwave_data.csv")

# 제목
st.title("📊 대한민국 폭염일수 시각화 대시보드")

# 연도 선택 (슬라이더)
years = sorted(df["year"].unique())
year = st.slider("연도 선택", int(min(years)), int(max(years)), int(min(years)))

# 선택된 연도 데이터
filtered = df[df["year"] == year]

# 지도 시각화 (Plotly)
fig = px.scatter_mapbox(
    filtered,
    lat="latitude",
    lon="longitude",
    size="heatwave_days",
    color="heatwave_days",
    hover_name="region",
    zoom=5,
    mapbox_style="carto-positron",
    title=f"{year}년 지역별 폭염일수"
)

st.plotly_chart(fig, use_container_width=True)
