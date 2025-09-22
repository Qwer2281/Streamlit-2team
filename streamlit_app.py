import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 데이터 로드
# -----------------------------
mean_days = pd.read_csv("data/mean_days.csv")
longest = pd.read_csv("data/longest_heatwave.csv")
first_last = pd.read_csv("data/first_last_heatwave.csv")

# 날짜 컬럼 변환
first_last["first_date"] = pd.to_datetime(first_last["first_date"])
first_last["last_date"] = pd.to_datetime(first_last["last_date"])

# 페이지 설정
st.set_page_config(page_title="Interactive Heatwave Dashboard", layout="wide")

# -----------------------------
# 사이드바 설정
# -----------------------------
st.sidebar.title("📊 대시보드 설정")

# Tab1: 연도 범위 슬라이더
year_min = int(mean_days["year"].min())
year_max = int(mean_days["year"].max())
year_range_tab1 = st.sidebar.slider(
    "Tab1: 연도 범위 선택",
    min_value=year_min,
    max_value=year_max,
    value=(year_min, year_max)
)

# Tab1: 특정 연도 선택
year_options_tab1 = mean_days["year"].unique()
selected_years_tab1 = st.sidebar.multiselect(
    "Tab1: 특정 연도 선택",
    options=year_options_tab1,
    default=list(year_options_tab1)
)

# -----------------------------
# 탭 설정
# -----------------------------
tab1, tab2, tab3 = st.tabs(["연도별 폭염일수", "최장 폭염", "폭염 시작·종료일"])

# -----------------------------
# Tab 1: 연도별 폭염일수
# -----------------------------
with tab1:
    st.subheader("연도별 폭염일수")
    filtered_data_tab1 = mean_days[
        (mean_days["year"] >= year_range_tab1[0]) &
        (mean_days["year"] <= year_range_tab1[1]) &
        (mean_days["year"].isin(selected_years_tab1))
    ]

    # 총 폭염일수 / 월별 보기 선택
    view_option_tab1 = st.radio(
        "Tab1: 보기 모드 선택",
        ["Total Heatwave Days", "Monthly Breakdown"]
    )

    fig_tab1 = px.line(
        filtered_data_tab1,
        x="year",
        y=["total", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
        labels={"value": "폭염일수", "variable": "월"},
        title="연도별 월별 폭염일수"
    ) if view_option_tab1 == "Monthly Breakdown" else px.line(
        filtered_data_tab1,
        x="year",
        y="total",
        labels={"total": "총 폭염일수"},
        title="연도별 총 폭염일수"
    )

    st.plotly_chart(fig_tab1)

# -----------------------------
# Tab 2: 최장 폭염
# -----------------------------
with tab2:
    st.subheader("최장 폭염")
    longest_year_options = longest["year"].unique()
    selected_longest_years = st.multiselect(
        "Tab2: 연도 선택",
        options=longest_year_options,
        default=list(longest_year_options)
    )
    filtered_longest = longest[longest["year"].isin(selected_longest_years)]

    fig_tab2 = px.bar(
        filtered_longest,
        x="year",
        y="duration",
        labels={"duration": "최장 폭염일수"},
        title="연도별 최장 폭염"
    )
    st.plotly_chart(fig_tab2)

# -----------------------------
# Tab 3: 폭염 시작·종료일
# -----------------------------
with tab3:
    st.subheader("폭염 시작·종료일")
    first_last_year_options = first_last["year"].unique()
    selected_first_last_years = st.multiselect(
        "Tab3: 연도 선택",
        options=first_last_year_options,
        default=list(first_last_year_options)
    )
    filtered_first_last = first_last[first_last["year"].isin(selected_first_last_years)]

    fig_tab3 = px.scatter(
        filtered_first_last,
        x="first_date",
        y="last_date",
        color="year",
        labels={"first_date": "시작일", "last_date": "종료일"},
        title="연도별 폭염 시작·종료일"
    )
    st.plotly_chart(fig_tab3)
