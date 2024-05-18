# app.py
import streamlit as st

# HTMLファイルを読み込む
with open('index.html', 'r', encoding='utf8') as file:
    html_content = file.read()

# CSSファイルを読み込む
with open('style.css', 'r', encoding='utf8') as file:
    css_content = f'<style>{file.read()}</style>'

# HTMLとCSSを組み合わせて表示する
st.markdown(css_content + html_content, unsafe_allow_html=True)