import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
mean_days = pd.read_csv("data/mean_days.csv")
longest = pd.read_csv("data/longest_heatwave.csv")
first_last = pd.read_csv("data/first_last_heatwave.csv")

st.title("📊 폭염 분석 대시보드")

tab1, tab2, tab3 = st.tabs(["연도별 폭염일수", "최장 폭염", "폭염 시작·종료일"])

# --- Tab 1: 평균 폭염일수 ---
with tab1:
    st.subheader("연도별 총 폭염일수")
    fig, ax = plt.subplots()
    ax.plot(mean_days["연도"], mean_days["연합계"], marker="o")
    ax.set_xlabel("연도")
    ax.set_ylabel("총 폭염일수")
    ax.set_title("연도별 폭염일수 합계")
    st.pyplot(fig)

# --- Tab 2: 최장 폭염 ---
with tab2:
    st.subheader("연도별 최장 폭염 지속일수")
    fig, ax = plt.subplots()
    ax.bar(longest["연도"], longest["지속일수"], color="orange")
    ax.set_xlabel("연도")
    ax.set_ylabel("최장 폭염일수")
    ax.set_title("최장 폭염 (연속)")
    st.pyplot(fig)

# --- Tab 3: 시작/종료일 ---
with tab3:
    st.subheader("연도별 폭염 시즌 (시작일~종료일)")
    first_last["가장 빠른 날짜"] = pd.to_datetime(first_last["가장 빠른 날짜"])
    first_last["가장 늦은 날짜"] = pd.to_datetime(first_last["가장 늦은 날짜"])

    fig, ax = plt.subplots()
    for i, row in first_last.iterrows():
        ax.plot([row["가장 빠른 날짜"], row["가장 늦은 날짜"]],
                [row["연도"], row["연도"]],
                marker="o")
    ax.set_xlabel("날짜")
    ax.set_ylabel("연도")
    ax.set_title("연도별 폭염 시즌 길이")
    st.pyplot(fig)
