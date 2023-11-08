import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

tab1, tab2, tab3 = st.tabs(["Home", "Dog", "Owl"])

with tab1:
   st.header("Home")
   title = st.text_input('Movie title', 'Life of Brian')
   st.write('The current movie title is', title)
  

with tab2:
   st.header("A dog")
 
with tab3:
   st.header("An owl")
 
