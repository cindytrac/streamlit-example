import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Submit", "Upload", "About Project ACORN"])

with tab1:
   st.header("ERFT Dictionary")
   
   text_input = st.text_input(
        "Search for an acronym",
        label_visibility="visible",
        placeholder="e.g. ERFT"
    )
   

with tab2:
   st.header("Submit an Acronym")
   
   text_input1 = st.text_input(
        "Enter the ACRONYM you would like to add.",
        label_visibility="visible",
        placeholder="e.g. ERFT",
      value=" this acronym "
    )

   text_input2 = st.text_input(
        ("What does " + text_input1 + "stand for?"),
        label_visibility="visible",
        placeholder="e.g. Enterprise Risk and Finance Technology"
    )
 
with tab3:
   st.header("An owl")

with tab4:
   st.header("Project ACORN")
 
