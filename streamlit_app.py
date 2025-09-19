import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
mean_days = pd.read_csv("data/mean_days.csv")
longest = pd.read_csv("data/longest_heatwave.csv")
first_last = pd.read_csv("data/first_last_heatwave.csv")

st.title("📊 Heatwave Analysis Dashboard")

tab1, tab2, tab3 = st.tabs(["Annual Heatwave Days", "Longest Heatwave", "Heatwave Start & End"])

# --- Tab 1: 평균 폭염일수 ---
with tab1:
    st.subheader("Total Heatwave Days by Year")
    fig, ax = plt.subplots()
    # 컬럼명을 영어로 매핑
    ax.plot(mean_days["year"], mean_days["total"], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Heatwave Days")
    ax.set_title("Annual Total Heatwave Days")
    st.pyplot(fig)

# --- Tab 2: 최장 폭염 ---
with tab2:
    st.subheader("Longest Heatwave Duration by Year")
    fig, ax = plt.subplots()
    ax.bar(longest["year"], longest["duration"], color="orange")
    ax.set_xlabel("Year")
    ax.set_ylabel("Longest Heatwave Days")
    ax.set_title("Longest Consecutive Heatwave")
    st.pyplot(fig)

# --- Tab 3: 시작/종료일 ---
with tab3:
    st.subheader("Heatwave Season by Year (Start ~ End)")
    # 영어 컬럼으로 변환
    first_last["first_date"] = pd.to_datetime(first_last["first_date"])
    first_last["last_date"] = pd.to_datetime(first_last["last_date"])

    fig, ax = plt.subplots()
    for i, row in first_last.iterrows():
        ax.plot([row["first_date"], row["last_date"]],
                [row["year"], row["year"]],
                marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Year")
    ax.set_title("Heatwave Season Length by Year")
    st.pyplot(fig)
