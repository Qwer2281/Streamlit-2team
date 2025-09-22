import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
mean_days = pd.read_csv("data/mean_days.csv")
longest = pd.read_csv("data/longest_heatwave.csv")
first_last = pd.read_csv("data/first_last_heatwave.csv")

# 날짜 컬럼 변환
first_last["first_date"] = pd.to_datetime(first_last["first_date"])
first_last["last_date"] = pd.to_datetime(first_last["last_date"])

# 페이지 설정
st.set_page_config(page_title="Interactive Heatwave Dashboard", layout="wide")

# 사이드바 설정
st.sidebar.title("📊 대시보드 설정")
year_range = st.sidebar.slider(
    "연도 범위 선택", int(mean_days["year"].min()), int(mean_days["year"].max()), (2015, 2025)
)
selected_years = st.sidebar.multiselect(
    "특정 연도 선택", options=mean_days["year"].unique(), default=list(range(2015, 2026))
)

# Tab 설정
tab1, tab2, tab3 = st.tabs(["연도별 폭염일수", "최장 폭염", "폭염 시작·종료일"])

# Tab 1: 연도별 폭염일수
with tab1:
    st.subheader("연도별 폭염일수")
    filtered_data = mean_days[
        (mean_days["year"] >= year_range[0])
        & (mean_days["year"] <= year_range[1])
        & (mean_days["year"].isin(selected_years))
    ]
    fig = px.line(
        filtered_data,
        x="year",
        y=["total", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
        labels={"value": "폭염일수", "variable": "월"},
        title="연도별 월별 폭염일수"
    )
    st.plotly_chart(fig)

# Tab 2: 최장 폭염
with tab2:
    st.subheader("최장 폭염")
    selected_year = st.selectbox("연도 선택", options=longest["year"].unique())
    filtered_longest = longest[longest["year"] == selected_year]
    fig = px.bar(
        filtered_longest,
        x="year",
        y="duration",
        labels={"duration": "최장 폭염일수"},
        title=f"{selected_year}년 최장 폭염"
    )
    st.plotly_chart(fig)

# Tab 3: 폭염 시작·종료일
with tab3:
    st.subheader("폭염 시작·종료일")
    selected_years_tab3 = st.multiselect(
        "연도 선택", options=first_last["year"].unique(), default=list(range(2015, 2026))
    )
    filtered_first_last = first_last[first_last["year"].isin(selected_years_tab3)]
    fig = px.scatter(
        filtered_first_last,
        x="first_date",
        y="last_date",
        color="year",
        labels={"first_date": "시작일", "last_date": "종료일"},
        title="폭염 시작·종료일"
    )
    st.plotly_chart(fig)
