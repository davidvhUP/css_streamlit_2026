# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("Hello2")

st.markdown("# This is also a heading")
st.markdown("## Markdown is much :rainbow[better looking]")
st.markdown("""
            Does **bold** work?
            How about :rainbow[rainbow]?
            """)

st.write("Hello, Streamlit!")

st.latex("\\alpha^2 = \\sigma x")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")
