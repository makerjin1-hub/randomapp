import random
import streamlit as st

# 웹앱 제목
st.title("🍚 오늘의 점심 메뉴 추천")

# 점심 메뉴 리스트
menus = [
    "김치찌개",
    "돈까스",
    "제육볶음",
    "비빔밥",
    "햄버거",
    "떡볶이",
    "파스타",
    "초밥",
    "마라탕",
    "칼국수"
]

# 버튼을 누르면 랜덤으로 메뉴 추천
if st.button("오늘의 점심 메뉴 추천받기"):
    menu = random.choice(menus)
    st.success(f"오늘의 점심 메뉴는 '{menu}'입니다!")
