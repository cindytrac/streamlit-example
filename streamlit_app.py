import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

tab1, tab2, tab3 = st.tabs(["Home", "Dog", "Owl"])

with tab1:
   st.header("ERFT Dictionary")
   title = st.text_input('Acronym', 'e.g. BofA, ERFT')
   # st.write('Acronym', title)
  

with tab2:
   st.header("A dog")
 
with tab3:
   st.header("An owl")
 
