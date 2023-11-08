import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Submit an Acronym", "Parse a Document", "About Project ACORN"])

with tab1:
   title = st.text_input('Input the ACRONYM you want to add.', 'e.g. BofA, ERFT')
   

with tab2:
   st.header("ERFT Dictionary")
   
   text_input = st.text_input(
        "Enter the ACRONYM you would like to add",
        label_visibility="visible",
        placeholder="placeholder"
    )
 
with tab3:
   st.header("An owl")

with tab4:
   st.header("Project ACORN")
 
