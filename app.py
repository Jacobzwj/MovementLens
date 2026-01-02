import streamlit as st
import pandas as pd

st.title("MovementLens")

st.write("这是内置的社会运动数据分析工具。")

# 模拟读取你的Excel
# st.write(pd.read_csv("your_data.csv"))

user_input = st.text_input("搜索社会运动关键词:", "")

if user_input:
    st.write(f"正在为您检索关于 '{user_input}' 的信息...")
    # 这里之后会写 LLM Agent 的逻辑
